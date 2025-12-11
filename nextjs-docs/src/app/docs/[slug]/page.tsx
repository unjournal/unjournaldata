import { notFound } from 'next/navigation';
import { fetchCodaPageContent } from '@/lib/coda-api';
import { PAGE_MAPPINGS, REVALIDATE_INTERVAL } from '@/lib/config';
import MarkdownRenderer from '@/components/MarkdownRenderer';
import type { PageParams } from '@/lib/types';

// Enable Incremental Static Regeneration (ISR)
export const revalidate = REVALIDATE_INTERVAL;

// Generate static params at build time for all known slugs
export async function generateStaticParams() {
  return Object.keys(PAGE_MAPPINGS).map((slug) => ({
    slug,
  }));
}

// Generate metadata for SEO
export async function generateMetadata({ params }: PageParams) {
  const { slug } = await params;

  // Humanize slug for title
  const title = slug
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');

  return {
    title: `${title} | The Unjournal Documentation`,
    description: `Documentation for ${title}`,
  };
}

export default async function DocPage({ params }: PageParams) {
  const { slug } = await params;

  // Validate slug and get page info
  const pageInfo = PAGE_MAPPINGS[slug];
  if (!pageInfo) {
    notFound();
  }

  const { docId, pageId } = pageInfo;

  // Fetch content from Coda API (server-side only)
  let content: string;
  try {
    content = await fetchCodaPageContent(docId, pageId);
  } catch (error) {
    console.error(`Failed to fetch content for slug "${slug}" (docId: ${docId}, pageId: ${pageId}):`, error);
    return (
      <div className="max-w-[65ch] mx-auto px-6 py-12">
        <div className="prose prose-slate max-w-none">
          <h1 className="font-serif text-4xl font-bold mb-4 text-red-600">
            Error Loading Content
          </h1>
          <p className="font-sans text-gray-700 leading-relaxed">
            Unable to fetch documentation for &quot;{slug}&quot;. Please try again later.
          </p>
          <p className="font-sans text-sm text-gray-500 mt-4">
            Error details: {error instanceof Error ? error.message : 'Unknown error'}
          </p>
        </div>
      </div>
    );
  }

  return (
    <article className="max-w-[65ch] mx-auto px-6 py-12">
      <div className="prose prose-slate prose-lg max-w-none">
        <MarkdownRenderer content={content} />
      </div>
    </article>
  );
}
