# Next.js Documentation Site - The Unjournal

A Next.js 14 documentation website that fetches content from Coda using the Coda API export feature.

## Features

- **Next.js 14 App Router** with TypeScript
- **Incremental Static Regeneration (ISR)** - pages revalidate every hour
- **Academic journal styling** - serif headings, sans-serif body, 65ch width
- **React-markdown** rendering with GitHub Flavored Markdown
- **Tailwind CSS** with @tailwindcss/typography plugin
- **Coda API integration** - async export with polling

## Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   Create `.env.local` with:
   ```bash
   CODA_API_KEY=your_api_key_here
   CODA_DOC_ID=0KBG3dSZCs
   CODA_API_BASE_URL=https://coda.io/apis/v1
   ```

3. **Run development server:**
   ```bash
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000)

4. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

## Deployment to Vercel

### Option 1: Vercel GitHub Integration (Recommended)

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"New Project"** → **"Import Git Repository"**
3. Select your repository: `unjournal/unjournaldata`
4. Configure project:
   - **Root Directory:** `nextjs-docs`
   - **Framework Preset:** Next.js (auto-detected)
5. Add **Environment Variables:**
   - `CODA_API_KEY`: Your Coda API key
   - `CODA_DOC_ID`: `0KBG3dSZCs`
   - (Optional) `CODA_API_BASE_URL`: `https://coda.io/apis/v1`
6. Click **"Deploy"**

### Option 2: Vercel CLI

```bash
npm install -g vercel
vercel login
vercel --prod
```

When prompted:
- Set root directory to `nextjs-docs`
- Add environment variables via Vercel dashboard

## Current Status (PoC)

### Known Limitations

The Coda API **only supports exporting "canvas" pages**, not "embed" pages. Current status:

| Route | Page Name | Status | Reason |
|-------|-----------|--------|--------|
| `/docs/evaluator-request` | Wellbeing PQ: Request to evaluators | ✅ Works | Canvas page |
| `/docs/wellbeing-pq` | Wellbeing PQ | ❌ Error | Embed page (not exportable) |
| `/docs/research-scoping` | Research scoping: Wellbeing | ❌ Error | Embed page (not exportable) |

**Error pages show gracefully** with a clear message explaining the issue.

### To Add More Pages

Edit `src/lib/config.ts` and add canvas-type pages from your Coda document:

```typescript
export const PAGE_MAPPINGS: Record<string, { docId: string; pageId: string }> = {
  'your-slug': {
    docId: 'dIEzDONWdb',
    pageId: 'canvas-YourPageId', // Must be contentType: "canvas"
  },
};
```

## Project Structure

```
nextjs-docs/
├── src/
│   ├── app/
│   │   ├── layout.tsx          # Root layout with fonts
│   │   ├── page.tsx            # Home page
│   │   ├── globals.css         # Tailwind + custom styles
│   │   └── docs/
│   │       └── [slug]/
│   │           └── page.tsx    # Dynamic route with ISR
│   ├── lib/
│   │   ├── coda-api.ts         # Coda async export client
│   │   ├── config.ts           # Slug mappings + ISR config
│   │   └── types.ts            # TypeScript interfaces
│   └── components/
│       └── MarkdownRenderer.tsx # React-markdown wrapper
├── public/                     # Static assets
├── .env.local                  # Local env vars (gitignored)
├── .env.example                # Template for env vars
├── package.json                # Dependencies
├── tailwind.config.ts          # Typography + academic styling
└── next.config.js              # Security headers
```

## Technologies

- **Next.js 14.2** - React framework with App Router
- **TypeScript 5.3** - Type safety
- **Tailwind CSS 3.4** - Utility-first CSS
- **@tailwindcss/typography** - Beautiful prose styling
- **react-markdown 9.0** - Markdown rendering
- **remark-gfm** - GitHub Flavored Markdown
- **rehype-raw & rehype-sanitize** - HTML support with security

## Configuration

### ISR Revalidation

Pages revalidate every **1 hour** (3600 seconds). To change:

```typescript
// src/lib/config.ts
export const REVALIDATE_INTERVAL = 3600; // Change this value
```

### Academic Styling

Customize fonts and typography in `tailwind.config.ts`:

```typescript
fontFamily: {
  serif: ['Merriweather', 'Georgia', 'serif'],  // Headings
  sans: ['Inter', 'system-ui', 'sans-serif'],   // Body text
},
```

## Automated Deployment

GitHub Actions workflow at `.github/workflows/deploy-nextjs-docs.yml`:

- **Triggers:** Push to main (nextjs-docs changes) + daily rebuild at 6 AM UTC
- **Note:** Currently configured for Vercel CLI deployment
- **Recommended:** Use Vercel GitHub Integration instead (simpler, no secrets needed)

## Troubleshooting

### Build Errors

**"CODA_API_KEY environment variable is not set"**
- Add API key to `.env.local` (local) or Vercel dashboard (production)

**"Only canvas pages can be exported"**
- The Coda page has `contentType: "embed"` - choose a different page with `contentType: "canvas"`

### Runtime Errors

**"Export timeout"**
- Coda API is slow or down - ISR will retry on next revalidation

**"Failed to fetch content"**
- Check API key validity
- Verify page IDs are correct
- Check Coda API status

## License

© 2025 The Unjournal. All rights reserved.
