import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['Merriweather', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '65ch',
            h1: {
              fontFamily: 'Merriweather, Georgia, serif',
              fontWeight: '700',
              lineHeight: '1.2',
              marginBottom: '0.5em',
            },
            h2: {
              fontFamily: 'Merriweather, Georgia, serif',
              fontWeight: '700',
              marginTop: '2em',
              marginBottom: '0.75em',
            },
            h3: {
              fontFamily: 'Merriweather, Georgia, serif',
              fontWeight: '600',
            },
            p: {
              fontFamily: 'Inter, system-ui, sans-serif',
              lineHeight: '1.75',
              marginBottom: '1.25em',
            },
            a: {
              color: '#2563eb',
              textDecoration: 'underline',
              '&:hover': {
                color: '#1d4ed8',
              },
            },
            code: {
              backgroundColor: '#f3f4f6',
              padding: '0.25rem 0.4rem',
              borderRadius: '0.25rem',
              fontWeight: '400',
            },
            'code::before': {
              content: '""',
            },
            'code::after': {
              content: '""',
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};

export default config;
