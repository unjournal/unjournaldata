#!/usr/bin/env python3
"""Apply blog labels while retaining already-published computed snapshots.

Run after rendering a clean source archive. The baseline must be an archive of
origin/gh-pages. This is an editorial release: historical R results are retained;
new prose pages and the approved aggregate-hours page come from the fresh build.
"""
import argparse
import html
import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import quote


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True, help='Clean website source directory')
    parser.add_argument('--published', type=Path, required=True, help='Extracted gh-pages baseline')
    parser.add_argument('--built', type=Path, required=True, help='Fresh Quarto output directory')
    args = parser.parse_args()
    if not (args.published / 'posts.html').is_file() or not (args.built / 'posts.html').is_file():
        raise ValueError('Both directories must contain the blog listing')
    preserved = []
    for source in sorted((args.source / 'posts').glob('*/index.qmd')):
        text = source.read_text()
        if '```{r' not in text or re.search(r'^draft:\s*true\s*$', text, re.M):
            continue
        slug = source.parent.name
        baseline = args.published / 'posts' / slug
        target = args.built / 'posts' / slug
        old_html = (baseline / 'index.html').read_text()
        label = re.search(r'^generation:\s*"([^"]+)"\s*$', text, re.M).group(1)
        note = next(line for line in text.splitlines() if line.startswith('**Production:'))
        rendered_note = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html.escape(note))
        old_html = re.sub(r'<p(?: class="production-note")?><strong>Production[^<]*</strong>.*?</p>\s*', '', old_html, count=1, flags=re.S)
        header = re.search(r'<header id="title-block-header"[^>]*>.*?</header>', old_html, re.S)
        if not header:
            raise ValueError(f'Missing title block in {slug}')
        old_html = old_html[:header.end()] + '\n<p class="production-note">' + rendered_note + '</p>\n' + old_html[header.end():]
        chip = ('<a href="../../posts.html#category=' + quote(label) + '">'
                '<div class="quarto-category">' + html.escape(label) + '</div></a>')
        if not re.search(r'<div class="quarto-category">\s*' + re.escape(html.escape(label)) + r'\s*</div>', old_html):
            old_html = old_html.replace('<div class="quarto-categories">', '<div class="quarto-categories">' + chip, 1)
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(baseline, target)
        (target / 'index.html').write_text(old_html)
        preserved.append('posts/' + slug + '/')
    # Keep resources referenced by the historical HTML, alongside newly built libraries.
    if (args.published / 'site_libs').exists():
        for resource in (args.published / 'site_libs').rglob('*'):
            target = args.built / resource.relative_to(args.published)
            if resource.is_file() and not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(resource, target)
    # Frozen computations can restore a listing script from an older Quarto.
    # Match the runtime to the Quarto version that generated the current markup.
    quarto_paths = subprocess.check_output(['quarto', '--paths'], text=True).splitlines()
    listing_assets = Path(quarto_paths[1]) / 'projects/website/listing'
    for name in ['quarto-listing.js', 'list.min.js']:
        target = args.built / 'site_libs/quarto-listing' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(listing_assets / name, target)
    # Search must describe the retained snapshots and must drop the replaced survey text.
    before = json.loads((args.published / 'search.json').read_text())
    after = json.loads((args.built / 'search.json').read_text())
    def retained(item):
        return any(item.get('href', '').startswith(prefix) for prefix in preserved)
    search = [item for item in after if not retained(item)] + [item for item in before if retained(item)]
    (args.built / 'search.json').write_text(json.dumps(search, ensure_ascii=False, indent=2))
    # An excluded draft can otherwise be copied as a resource by a listing reference.
    draft = args.built / 'posts/ratings-reliability-2026'
    if draft.exists():
        shutil.rmtree(draft)
    if list(args.built.rglob('*.qmd')):
        raise ValueError('Unexpected source documents in publication output')
    print('Preserved published results; added labels:', ', '.join(preserved))


if __name__ == '__main__':
    main()
