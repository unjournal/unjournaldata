import type { ExportInitResponse } from './types';

const CODA_API_KEY = process.env.CODA_API_KEY!;
const CODA_DOC_ID = process.env.CODA_DOC_ID!;
const BASE_URL = process.env.CODA_API_BASE_URL || 'https://coda.io/apis/v1';

// Validate environment variables
if (!CODA_API_KEY) {
  throw new Error('CODA_API_KEY environment variable is not set');
}

if (!CODA_DOC_ID) {
  throw new Error('CODA_DOC_ID environment variable is not set');
}

/**
 * Fetches content from a Coda page using the async export API
 *
 * This implements a 3-step process:
 * 1. Initiate export (POST to /docs/{docId}/pages/{pageId}/export)
 * 2. Poll status URL until complete
 * 3. Download content from downloadLink
 *
 * @param docId - The Coda document ID
 * @param pageId - The Coda page ID within the document
 * @returns The markdown content of the page
 */
export async function fetchCodaPageContent(docId: string, pageId: string): Promise<string> {
  // Step 1: Initiate export
  const initResponse = await fetch(
    `${BASE_URL}/docs/${docId}/pages/${pageId}/export`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${CODA_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        outputFormat: 'markdown',
      }),
      next: { revalidate: 3600 }, // Use Next.js ISR caching
    }
  );

  if (!initResponse.ok) {
    const errorText = await initResponse.text();
    throw new Error(
      `Failed to initiate Coda export for page ${pageId}: ${initResponse.statusText} - ${errorText}`
    );
  }

  const initData = await initResponse.json() as ExportInitResponse;
  const statusUrl = initData.href;

  console.log(`[Coda Export] Initiated export for page ${pageId}, status URL: ${statusUrl}`);

  // Step 2: Poll for completion
  const maxAttempts = 60; // Increased from 30
  const pollInterval = 2000; // 2 seconds (increased from 1 second)
  let attempts = 0;

  while (attempts < maxAttempts) {
    await new Promise(resolve => setTimeout(resolve, pollInterval));

    const statusResponse = await fetch(statusUrl, {
      headers: {
        'Authorization': `Bearer ${CODA_API_KEY}`,
      },
      next: { revalidate: 3600 },
    });

    // Handle 404 during initial processing (Coda API quirk)
    if (statusResponse.status === 404) {
      console.log(`[Coda Export] Attempt ${attempts + 1}/${maxAttempts}: Status 404 (still processing)`);
      attempts++;
      continue;
    }

    if (!statusResponse.ok) {
      throw new Error(
        `Export status check failed for page ${pageId}: ${statusResponse.statusText}`
      );
    }

    const statusData = await statusResponse.json() as ExportInitResponse;
    console.log(`[Coda Export] Attempt ${attempts + 1}/${maxAttempts}: Status = ${statusData.status}`);

    if (statusData.status === 'complete' && statusData.downloadLink) {
      // Step 3: Download content
      const contentResponse = await fetch(statusData.downloadLink, {
        next: { revalidate: 3600 },
      });

      if (!contentResponse.ok) {
        throw new Error(
          `Failed to download content for page ${pageId}: ${contentResponse.statusText}`
        );
      }

      const content = await contentResponse.text();
      console.log(`[Coda Export] Successfully downloaded ${content.length} characters for page ${pageId}`);
      return content;
    }

    if (statusData.status === 'failed') {
      throw new Error(`Coda export failed for page ${pageId}`);
    }

    attempts++;
  }

  throw new Error(
    `Export timeout for page ${pageId} - exceeded maximum polling attempts (${maxAttempts})`
  );
}
