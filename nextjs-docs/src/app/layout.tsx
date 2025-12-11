import type { Metadata } from 'next';
import { Inter, Merriweather } from 'next/font/google';
import './globals.css';

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

const merriweather = Merriweather({
  weight: ['400', '700'],
  subsets: ['latin'],
  variable: '--font-merriweather',
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'The Unjournal Documentation',
  description: 'Documentation and resources for The Unjournal',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${merriweather.variable}`}>
      <body className="font-sans antialiased">
        <header className="border-b border-gray-200 bg-white">
          <div className="max-w-7xl mx-auto px-6 py-4">
            <h1 className="text-2xl font-serif font-bold text-gray-900">
              The Unjournal Documentation
            </h1>
          </div>
        </header>
        <main className="min-h-screen">
          {children}
        </main>
        <footer className="border-t border-gray-200 bg-gray-50 mt-16">
          <div className="max-w-7xl mx-auto px-6 py-8 text-center text-sm text-gray-600">
            <p>
              © {new Date().getFullYear()} The Unjournal. All rights reserved.
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}
