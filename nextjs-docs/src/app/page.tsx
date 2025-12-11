import Link from 'next/link';
import { PAGE_MAPPINGS } from '@/lib/config';

export default function Home() {
  const pages = Object.keys(PAGE_MAPPINGS);

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <div className="prose prose-slate prose-lg max-w-none">
        <h1 className="font-serif text-4xl font-bold mb-6">
          Welcome to The Unjournal Documentation
        </h1>

        <p className="font-sans leading-relaxed text-gray-700 mb-8">
          Access comprehensive documentation and resources for The Unjournal project.
          All content is dynamically fetched from our Coda knowledge base.
        </p>

        <h2 className="font-serif text-2xl font-bold mb-4 mt-8">
          Available Documentation
        </h2>

        <div className="grid gap-4 not-prose">
          {pages.map((slug) => {
            const title = slug
              .split('-')
              .map(word => word.charAt(0).toUpperCase() + word.slice(1))
              .join(' ');

            return (
              <Link
                key={slug}
                href={`/docs/${slug}`}
                className="block p-6 border border-gray-200 rounded-lg hover:border-blue-500 hover:shadow-md transition-all"
              >
                <h3 className="font-serif text-xl font-semibold text-gray-900 mb-2">
                  {title}
                </h3>
                <p className="font-sans text-sm text-gray-600">
                  View documentation →
                </p>
              </Link>
            );
          })}
        </div>

        <div className="mt-12 p-6 bg-blue-50 border border-blue-200 rounded-lg">
          <h3 className="font-serif text-lg font-semibold text-blue-900 mb-2">
            About This Site
          </h3>
          <p className="font-sans text-sm text-blue-800 leading-relaxed">
            This documentation site uses Next.js with Incremental Static Regeneration (ISR)
            to fetch content from Coda. Pages are updated automatically every hour
            to ensure fresh content while maintaining fast load times.
          </p>
        </div>
      </div>
    </div>
  );
}
