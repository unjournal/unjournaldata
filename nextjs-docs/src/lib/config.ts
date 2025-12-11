// Slug to Coda Page ID mappings
// These pages are within the "Unjournal: Public Pages" document (dIEzDONWdb)
export const PAGE_MAPPINGS: Record<string, { docId: string; pageId: string }> = {
  'wellbeing-pq': {
    docId: 'dIEzDONWdb',
    pageId: 'canvas-b7onPg8sEH', // "Wellbeing PQ"
  },
  'evaluator-request': {
    docId: 'dIEzDONWdb',
    pageId: 'canvas-BBuWnEh2Yw', // "Wellbeing PQ: Request to evaluators"
  },
  'research-scoping': {
    docId: 'dIEzDONWdb',
    pageId: 'canvas-mfacGkBgmh', // "Research scoping: Wellbeing"
  },
};

export const VALID_SLUGS = Object.keys(PAGE_MAPPINGS);

// ISR configuration (revalidation interval in seconds)
export const REVALIDATE_INTERVAL = 3600; // 1 hour

// Academic styling constants
export const PROSE_CONFIG = {
  maxWidth: '65ch',
  serifFont: 'Merriweather',
  sansFont: 'Inter',
};
