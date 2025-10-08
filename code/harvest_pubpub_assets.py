#!/usr/bin/env python3
"""Harvest PubPub markdown and PDF exports for all pubs in a community.

This script reaches out to the public PubPub GraphQL API to enumerate every
pub that belongs to the ``unjournal.pubpub.org`` community (by default) and
downloads both Markdown and PDF exports for each pub.  The PubPub platform
does not retain generated exports indefinitely, so the script first requests
fresh export jobs and then polls the export status until the rendered asset is
ready before downloading it.

Because the public API schema is not versioned, the script introspects the
GraphQL schema at runtime and dynamically discovers the query and mutation
fields that it needs.  This keeps the implementation resilient to minor schema
changes (for example, renaming connection fields) without having to hard-code
exact operation names.

Example
-------

.. code-block:: bash

    python code/harvest_pubpub_assets.py --output-dir ./pubpub_exports

The script will create ``pubpub_exports`` (if necessary) and populate it with
``<pub-slug>.md`` and ``<pub-slug>.pdf`` files.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import pathlib
import time
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import requests


# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------

LOGGER = logging.getLogger("harvest_pubpub")


# ---------------------------------------------------------------------------
# GraphQL plumbing
# ---------------------------------------------------------------------------

INTROSPECTION_QUERY = """
query PubPubIntrospection {
  __schema {
    types {
      kind
      name
      fields(includeDeprecated: false) {
        name
        args {
          name
          type { kind name ofType { kind name ofType { kind name } } }
        }
        type { kind name ofType { kind name ofType { kind name } } }
      }
      inputFields {
        name
        type { kind name ofType { kind name ofType { kind name } } }
      }
      interfaces { name }
      enumValues(includeDeprecated: false) { name }
      possibleTypes { name }
    }
    queryType { name fields { name args { name type { kind name ofType { kind name } } } type { kind name ofType { kind name } } } }
    mutationType { name fields { name args { name type { kind name ofType { kind name } } } type { kind name ofType { kind name } } } }
  }
}
"""


class GraphQLError(RuntimeError):
    """Raised when the GraphQL API reports an error."""


class GraphQLClient:
    """Thin wrapper around :mod:`requests` for interacting with GraphQL."""

    def __init__(self, endpoint: str, session: Optional[requests.Session] = None):
        self.endpoint = endpoint
        self.session = session or requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "unjournal-harvest-script/1.0 (+https://unjournal.org)",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def execute(self, query: str, variables: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        LOGGER.debug("Executing GraphQL query: %s", query)
        response = self.session.post(self.endpoint, json=payload, timeout=60)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise GraphQLError(f"HTTP error: {exc}") from exc

        try:
            data = response.json()
        except json.JSONDecodeError as exc:
            raise GraphQLError("Server returned non-JSON response") from exc

        if "errors" in data and data["errors"]:
            raise GraphQLError(str(data["errors"]))

        return data.get("data", {})


# ---------------------------------------------------------------------------
# Schema helpers
# ---------------------------------------------------------------------------


def _unwrap_type(type_obj: Mapping[str, Any]) -> Mapping[str, Any]:
    """Return the innermost named type description."""

    current = type_obj
    while current and current.get("kind") in {"NON_NULL", "LIST"}:
        current = current.get("ofType") or {}
    return current or {}


def _format_type(type_obj: Mapping[str, Any]) -> str:
    """Generate a printable representation of a GraphQL type."""

    kind = type_obj.get("kind")
    name = type_obj.get("name")
    inner = type_obj.get("ofType")
    if kind == "NON_NULL" and inner:
        return f"{_format_type(inner)}!"
    if kind == "LIST" and inner:
        return f"[{_format_type(inner)}]"
    return name or ""


def _build_selection(
    type_obj: Mapping[str, Any],
    types_index: Mapping[str, Mapping[str, Any]],
    depth: int = 0,
    visited: Optional[Dict[str, int]] = None,
    max_depth: int = 3,
) -> str:
    """Create a GraphQL selection set for ``type_obj``.

    The selection focuses on scalars and shallow object relationships without
    arguments so that the response stays compact but still contains the data we
    need.  ``__typename`` is included for every object to make downstream
    traversal easier.
    """

    visited = visited or {}
    base = _unwrap_type(type_obj)
    kind = base.get("kind")
    name = base.get("name")

    if not base or kind in {"SCALAR", "ENUM"}:
        return ""

    if kind in {"OBJECT", "INTERFACE", "UNION"}:
        depth_key = f"{name}:{depth}"
        previous_depth = visited.get(name)
        if previous_depth is not None and previous_depth <= depth:
            return ""
        visited[name] = depth

        selections: List[str] = ["__typename"]

        if kind == "UNION" or kind == "INTERFACE":
            for possible in base.get("possibleTypes", []):
                possible_name = possible.get("name")
                if not possible_name:
                    continue
                inner = types_index.get(possible_name)
                if not inner:
                    continue
                fragment = _build_selection(inner, types_index, depth + 1, visited, max_depth)
                if fragment:
                    selections.append(f"... on {possible_name} {fragment}")
            return "{ " + " ".join(selections) + " }"

        # Plain object
        type_def = types_index.get(name, {})
        fields = type_def.get("fields", [])

        if depth >= max_depth:
            scalar_fields = [f["name"] for f in fields if not f.get("args") and _unwrap_type(f["type"]).get("kind") in {"SCALAR", "ENUM"}]
            selections.extend(sorted(set(scalar_fields)))
            return "{ " + " ".join(selections) + " }"

        for field in fields:
            field_name = field.get("name")
            if not field_name or field.get("args"):
                continue
            field_type = field.get("type", {})
            child_selection = _build_selection(field_type, types_index, depth + 1, visited, max_depth)
            if child_selection:
                selections.append(f"{field_name} {child_selection}")
            else:
                base_kind = _unwrap_type(field_type).get("kind")
                if base_kind in {"SCALAR", "ENUM"}:
                    selections.append(field_name)

        return "{ " + " ".join(dict.fromkeys(selections)) + " }"

    return ""


# ---------------------------------------------------------------------------
# Data extraction helpers
# ---------------------------------------------------------------------------


def _traverse(data: Any) -> Iterable[Mapping[str, Any]]:
    """Yield every mapping contained anywhere in ``data``."""

    if isinstance(data, Mapping):
        yield data
        for value in data.values():
            yield from _traverse(value)
    elif isinstance(data, (list, tuple)):
        for item in data:
            yield from _traverse(item)


def _collect_by_typename(data: Any, typename: str) -> List[Mapping[str, Any]]:
    """Return all mapping nodes whose ``__typename`` matches ``typename``."""

    matches: List[Mapping[str, Any]] = []
    for node in _traverse(data):
        if node.get("__typename") == typename:
            matches.append(node)
    return matches


def _collect_enum_values(schema_types: Mapping[str, Mapping[str, Any]], name_fragment: str) -> Dict[str, str]:
    """Return enum values whose type name contains ``name_fragment``."""

    results: Dict[str, str] = {}
    for type_name, type_def in schema_types.items():
        if type_def.get("kind") != "ENUM":
            continue
        if name_fragment.lower() not in type_name.lower():
            continue
        for value in type_def.get("enumValues", []) or []:
            val_name = value.get("name")
            if val_name:
                results[val_name.upper()] = val_name
    return results


# ---------------------------------------------------------------------------
# Pub and export discovery
# ---------------------------------------------------------------------------


def discover_community_data(
    client: GraphQLClient,
    schema: Mapping[str, Any],
    hostname: str,
    types_index: Mapping[str, Mapping[str, Any]],
) -> Any:
    """Fetch community data for ``hostname`` using an appropriate query."""

    query_fields = schema.get("queryType", {}).get("fields", [])

    subdomain = hostname.split(".")[0]
    value_map = {
        "hostname": hostname,
        "host": hostname,
        "domain": hostname,
        "url": f"https://{hostname}",
        "slug": subdomain,
        "communityslug": subdomain,
        "subdomain": subdomain,
        "name": subdomain,
    }

    for field in query_fields:
        field_name = field.get("name")
        if not field_name or "community" not in field_name.lower():
            continue
        args = field.get("args", [])
        selection = _build_selection(field.get("type", {}), types_index, max_depth=2)
        if not selection:
            continue

        # Build variables for arguments we can satisfy.
        variable_defs: List[str] = []
        variable_assignments: List[str] = []
        variables: Dict[str, Any] = {}
        missing_required = False

        for arg in args:
            arg_name = arg.get("name")
            if not arg_name:
                continue
            arg_type_obj = arg.get("type", {})
            arg_type = _format_type(arg_type_obj)
            required = arg_type.endswith("!")
            value = value_map.get(arg_name.lower())
            if value is None:
                if required:
                    missing_required = True
                    break
                continue
            variables[arg_name] = value
            variable_defs.append(f"${arg_name}: {arg_type}")
            variable_assignments.append(f"{arg_name}: ${arg_name}")

        if missing_required or (not variables and args):
            continue

        def_clause = f"({', '.join(variable_defs)})" if variable_defs else ""
        arg_clause = f"({', '.join(variable_assignments)})" if variable_assignments else ""
        gql = f"query{def_clause} {{ {field_name}{arg_clause} {selection} }}"

        try:
            LOGGER.debug("Attempting community query %s", field_name)
            data = client.execute(gql, variables)
        except GraphQLError:
            continue

        payload = data.get(field_name)
        if payload is not None:
            communities = _collect_by_typename(payload, "Community")
            for community in communities:
                identity_values = {
                    str(community.get("domain")),
                    str(community.get("hostname")),
                    str(community.get("url")),
                    str(community.get("slug")),
                    str(community.get("subdomain")),
                }
                if hostname in identity_values or f"https://{hostname}" in identity_values or subdomain in identity_values:
                    LOGGER.info("Using community query '%s'", field_name)
                    return community

            LOGGER.info("Using community query '%s' without explicit filtering", field_name)
            return payload

    raise GraphQLError("Unable to find community query in schema")


def extract_pubs(community_payload: Any) -> List[Mapping[str, Any]]:
    """Extract pub objects from the raw community payload."""

    pubs = _collect_by_typename(community_payload, "Pub")
    unique: Dict[str, Mapping[str, Any]] = {}
    for pub in pubs:
        slug = pub.get("slug")
        pub_id = pub.get("id")
        if slug and pub_id:
            unique[(slug, pub_id)] = pub
    return list(unique.values())


@dataclass
class ExportJob:
    """Represents a queued export for a Pub."""

    id: str
    status: str
    download_url: Optional[str]


def _identify_export_mutation(
    schema: Mapping[str, Any], types_index: Mapping[str, Mapping[str, Any]]
) -> Tuple[str, Mapping[str, Any]]:
    mutation_type = schema.get("mutationType")
    if not mutation_type:
        raise GraphQLError("GraphQL schema exposes no mutations; cannot request exports")

    for field in mutation_type.get("fields", []):
        field_name = field.get("name", "")
        if "export" not in field_name.lower():
            continue
        args = field.get("args", [])
        arg_names = {arg.get("name"): arg for arg in args}
        if not arg_names:
            continue
        if not any(name for name in arg_names if name and ("pub" in name or "input" in name.lower())):
            continue
        selection = _build_selection(field.get("type", {}), types_index, max_depth=2)
        if not selection:
            continue
        return field_name, {
            "field": field,
            "selection": selection,
        }

    raise GraphQLError("Could not locate an export mutation in the schema")


def _build_export_value(
    arg_name: str,
    arg_type: Mapping[str, Any],
    types_index: Mapping[str, Mapping[str, Any]],
    pub_id: str,
    format_value: str,
    version_id: Optional[str],
) -> Optional[Any]:
    type_name = _unwrap_type(arg_type).get("name")
    if not type_name:
        return None

    lower_name = arg_name.lower()
    if lower_name in {"pubid", "pub", "id"}:
        return pub_id
    if lower_name in {"format", "type", "exporttype"}:
        return format_value
    if lower_name in {"versionid", "pubversionid"} and version_id:
        return version_id

    type_def = types_index.get(type_name)
    if not type_def or type_def.get("kind") != "INPUT_OBJECT":
        return None

    payload: Dict[str, Any] = {}
    for input_field in type_def.get("inputFields", []) or []:
        input_name = input_field.get("name")
        if not input_name:
            continue
        value = _build_export_value(
            input_name,
            input_field.get("type", {}),
            types_index,
            pub_id,
            format_value,
            version_id,
        )
        if value is not None:
            payload[input_name] = value

    return payload or None


def _build_export_arguments(
    field: Mapping[str, Any],
    types_index: Mapping[str, Mapping[str, Any]],
    pub_id: str,
    format_value: str,
    version_id: Optional[str] = None,
) -> Tuple[Dict[str, Any], str, str]:
    variables: Dict[str, Any] = {}
    definitions: List[str] = []
    assignments: List[str] = []

    for arg in field.get("args", []):
        arg_name = arg.get("name")
        if not arg_name:
            continue
        value = _build_export_value(arg_name, arg.get("type", {}), types_index, pub_id, format_value, version_id)
        arg_type = arg.get("type", {})
        type_repr = _format_type(arg_type)
        if value is None:
            if type_repr.endswith("!"):
                raise GraphQLError(
                    f"Cannot build export mutation arguments; missing required value for '{arg_name}'"
                )
            continue
        variables[arg_name] = value
        definitions.append(f"${arg_name}: {type_repr}")
        assignments.append(f"{arg_name}: ${arg_name}")

    return variables, ", ".join(definitions), ", ".join(assignments)


def _select_export_enum(
    types_index: Mapping[str, Mapping[str, Any]],
    target: str,
) -> str:
    enum_values = _collect_enum_values(types_index, "Export")
    for enum_value in enum_values:
        if target.upper() in enum_value:
            return enum_values[enum_value]
    raise GraphQLError(f"Unable to find export enum value for {target}")


def _collect_exports(payload: Mapping[str, Any]) -> List[ExportJob]:
    jobs = _collect_by_typename(payload, "Export")
    results: List[ExportJob] = []
    for job in jobs:
        job_id = job.get("id")
        status = job.get("status") or ""
        download_url = job.get("downloadUrl") or job.get("downloadURL")
        if job_id and status:
            results.append(ExportJob(id=job_id, status=status, download_url=download_url))
    return results


def request_export(
    client: GraphQLClient,
    mutation_name: str,
    mutation_meta: Mapping[str, Any],
    types_index: Mapping[str, Mapping[str, Any]],
    pub_id: str,
    format_value: str,
    version_id: Optional[str] = None,
) -> ExportJob:
    field = mutation_meta["field"]
    variables, definitions, assignments = _build_export_arguments(field, types_index, pub_id, format_value, version_id)
    if not variables:
        raise GraphQLError("Export mutation does not accept any recognizable arguments")

    def_clause = f"({definitions})" if definitions else ""
    arg_clause = f"({assignments})" if assignments else ""
    selection = mutation_meta["selection"]
    gql = f"mutation{def_clause} {{ {mutation_name}{arg_clause} {selection} }}"

    try:
        data = client.execute(gql, variables)
    except GraphQLError as exc:
        raise GraphQLError(f"Unable to request export for pub {pub_id}: {exc}") from exc

    payload = data.get(mutation_name)
    if not payload:
        raise GraphQLError(f"Export mutation '{mutation_name}' returned no data")

    exports = _collect_exports(payload)
    if not exports:
        raise GraphQLError("Export request succeeded but no export job was returned")

    return exports[0]


def _identify_export_query(schema: Mapping[str, Any], types_index: Mapping[str, Mapping[str, Any]]) -> Tuple[str, Mapping[str, Any]]:
    query_type = schema.get("queryType", {})
    for field in query_type.get("fields", []):
        field_name = field.get("name", "")
        if "export" not in field_name.lower():
            continue
        args = field.get("args", [])
        if not any(arg.get("name") for arg in args):
            continue
        selection = _build_selection(field.get("type", {}), types_index, max_depth=2)
        if not selection:
            continue
        return field_name, {"field": field, "selection": selection}

    raise GraphQLError("Failed to identify export lookup query")


def fetch_export_status(
    client: GraphQLClient,
    query_name: str,
    query_meta: Mapping[str, Any],
    export_id: str,
) -> ExportJob:
    field = query_meta["field"]
    selection = query_meta["selection"]
    arg = next((a for a in field.get("args", []) if a.get("name")), None)
    if not arg:
        raise GraphQLError("Export status query is missing arguments")
    arg_name = arg.get("name")
    arg_type = _format_type(arg.get("type", {}))
    gql = f"query(${arg_name}: {arg_type}) {{ {query_name}({arg_name}: ${arg_name}) {selection} }}"
    data = client.execute(gql, {arg_name: export_id})
    payload = data.get(query_name)
    if not payload:
        raise GraphQLError(f"Export status query '{query_name}' returned no data")
    exports = _collect_exports(payload)
    if not exports:
        raise GraphQLError("No export job found in status response")
    return exports[0]


def wait_for_export(
    client: GraphQLClient,
    query_name: str,
    query_meta: Mapping[str, Any],
    job: ExportJob,
    poll_interval: float = 5.0,
    timeout: float = 300.0,
) -> ExportJob:
    deadline = time.time() + timeout
    current = job
    while time.time() < deadline:
        LOGGER.debug("Export %s status: %s", current.id, current.status)
        status_lower = current.status.lower()
        if current.download_url and current.status.lower() in {"done", "completed", "ready", "finished", "succeeded"}:
            return current
        if status_lower in {"failed", "error", "cancelled", "canceled"}:
            raise GraphQLError(f"Export {current.id} failed with status {current.status}")
        time.sleep(poll_interval)
        current = fetch_export_status(client, query_name, query_meta, current.id)
    raise TimeoutError(f"Export {current.id} did not complete within {timeout} seconds")


# ---------------------------------------------------------------------------
# File operations
# ---------------------------------------------------------------------------


def write_binary(target: pathlib.Path, content: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as handle:
        handle.write(content)


def download_asset(session: requests.Session, url: str) -> bytes:
    response = session.get(url, timeout=120)
    response.raise_for_status()
    return response.content


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------


def harvest(
    output_dir: pathlib.Path,
    hostname: str = "unjournal.pubpub.org",
    graphql_endpoint: str = "https://api.pubpub.org/graphql",
) -> None:
    LOGGER.info("Starting harvest for community %s", hostname)

    client = GraphQLClient(graphql_endpoint)
    schema_data = client.execute(INTROSPECTION_QUERY)["__schema"]
    types_index = {type_def["name"]: type_def for type_def in schema_data.get("types", []) if type_def.get("name")}

    community_payload = discover_community_data(client, schema_data, hostname, types_index)
    pubs = extract_pubs(community_payload)
    if not pubs:
        raise GraphQLError("No pubs were discovered for the target community")

    LOGGER.info("Discovered %d pubs", len(pubs))

    mutation_name, mutation_meta = _identify_export_mutation(schema_data, types_index)
    query_name, query_meta = _identify_export_query(schema_data, types_index)

    pdf_enum = _select_export_enum(types_index, "PDF")
    markdown_enum = _select_export_enum(types_index, "MARKDOWN")

    session = client.session

    for pub in pubs:
        slug = pub.get("slug")
        pub_id = pub.get("id")
        version = pub.get("currentVersion", {}).get("id") or pub.get("latestVersion", {}).get("id")
        title = pub.get("title", slug)
        if not slug or not pub_id:
            LOGGER.warning("Skipping pub without slug or id: %s", title)
            continue

        LOGGER.info("Processing pub '%s' (%s)", title, slug)

        for export_label, enum_value, extension in (
            ("markdown", markdown_enum, "md"),
            ("pdf", pdf_enum, "pdf"),
        ):
            try:
                job = request_export(
                    client,
                    mutation_name,
                    mutation_meta,
                    types_index,
                    pub_id,
                    enum_value,
                    version,
                )
                LOGGER.info("Requested %s export (%s) for pub %s", export_label, job.id, slug)
                finished_job = wait_for_export(client, query_name, query_meta, job)
                asset = download_asset(session, finished_job.download_url)
            except Exception as exc:  # noqa: BLE001
                LOGGER.error("Failed to download %s export for %s: %s", export_label, slug, exc)
                continue

            output_path = output_dir / f"{slug}.{extension}"
            write_binary(output_path, asset)
            LOGGER.info("Saved %s export to %s", export_label, output_path)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=pathlib.Path,
        default=pathlib.Path("pubpub_exports"),
        help="Directory where exported assets should be stored.",
    )
    parser.add_argument(
        "--hostname",
        default="unjournal.pubpub.org",
        help="PubPub community hostname to harvest.",
    )
    parser.add_argument(
        "--graphql-endpoint",
        default="https://api.pubpub.org/graphql",
        help="GraphQL endpoint to query.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging verbosity.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    logging.basicConfig(level=getattr(logging, args.log_level))
    output_dir = args.output_dir
    if not isinstance(output_dir, pathlib.Path):
        output_dir = pathlib.Path(os.fspath(output_dir))
    harvest(output_dir=output_dir, hostname=args.hostname, graphql_endpoint=args.graphql_endpoint)


if __name__ == "__main__":
    main()

