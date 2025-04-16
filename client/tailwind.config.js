/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{html,js,svelte,ts}'],
    theme: {
      extend: {
        colors: {
          green: {
            600: '#2E7D32', // Primary - Forest Green
          },
          blue: {
            500: '#0288D1', // Secondary - Soft Blue
          },
          amber: {
            500: '#F59E0B', // Accent - Warm Orange/Gold
          },
          gray: {
            300: '#D1D5DB', // Light neutral
            600: '#4B5563', // Medium neutral
          },
        },
        boxShadow: {
          sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
          DEFAULT: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
          md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
          lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
          xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        },
        fontFamily: {
            sans: ['Inter', 'system-ui', 'sans-serif'],
          },
          animation: {
            blob: "blob 7s infinite",
          },
          keyframes: {
            blob: {
              "0%": {
                transform: "scale(1)",
              },
              "33%": {
                transform: "scale(1.1)",
              },
              "66%": {
                transform: "scale(0.9)",
              },
              "100%": {
                transform: "scale(1)",
              },
            },
      },
    },
    plugins: [],
  }
}