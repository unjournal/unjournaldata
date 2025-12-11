/** @type {import('next').NextConfig} */
const nextConfig = {
  // Ensure server-side environment variables are available
  env: {
    CODA_DOC_ID: process.env.CODA_DOC_ID,
  },

  // Security headers
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'strict-origin-when-cross-origin',
          },
        ],
      },
    ];
  },

  // Optimize for production
  reactStrictMode: true,

  // Image optimization (if using images from Coda)
  images: {
    domains: ['coda.io', 'codahosted.io'],
  },
};

module.exports = nextConfig;
