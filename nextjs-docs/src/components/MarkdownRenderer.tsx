'use client';

import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';

interface MarkdownRendererProps {
  content: string;
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm]}
      rehypePlugins={[rehypeRaw, rehypeSanitize]}
      components={{
        // Customize headings with academic styling
        h1: ({ children }) => (
          <h1 className="font-serif text-4xl font-bold mb-6 mt-8 text-gray-900">
            {children}
          </h1>
        ),
        h2: ({ children }) => (
          <h2 className="font-serif text-3xl font-bold mb-4 mt-8 text-gray-900">
            {children}
          </h2>
        ),
        h3: ({ children }) => (
          <h3 className="font-serif text-2xl font-semibold mb-3 mt-6 text-gray-900">
            {children}
          </h3>
        ),
        // Customize paragraphs with comfortable reading
        p: ({ children }) => (
          <p className="font-sans leading-relaxed mb-6 text-gray-800">
            {children}
          </p>
        ),
        // Customize links
        a: ({ href, children }) => (
          <a
            href={href}
            className="text-blue-600 hover:text-blue-800 underline"
            target={href?.startsWith('http') ? '_blank' : undefined}
            rel={href?.startsWith('http') ? 'noopener noreferrer' : undefined}
          >
            {children}
          </a>
        ),
        // Customize code blocks
        code: ({ children, className }) => {
          const isInline = !className;
          if (isInline) {
            return (
              <code className="bg-gray-100 px-1.5 py-0.5 rounded text-sm font-mono text-gray-800">
                {children}
              </code>
            );
          }
          return (
            <code className={className}>
              {children}
            </code>
          );
        },
        // Customize pre blocks
        pre: ({ children }) => (
          <pre className="bg-gray-50 border border-gray-200 rounded-lg p-4 overflow-x-auto mb-6">
            {children}
          </pre>
        ),
        // Customize lists
        ul: ({ children }) => (
          <ul className="list-disc list-inside mb-6 space-y-2">
            {children}
          </ul>
        ),
        ol: ({ children }) => (
          <ol className="list-decimal list-inside mb-6 space-y-2">
            {children}
          </ol>
        ),
        // Customize blockquotes
        blockquote: ({ children }) => (
          <blockquote className="border-l-4 border-blue-500 pl-4 italic my-6 text-gray-700">
            {children}
          </blockquote>
        ),
      }}
    >
      {content}
    </ReactMarkdown>
  );
}
