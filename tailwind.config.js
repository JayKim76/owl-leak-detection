/** @type {import('tasc.config.js')} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#0F172A',   // Deep Navy (Trust)
          secondary: '#334155', // Slate (Professional)
          accent: '#06B6D4',    // Cyan (AI/Tech)
          success: '#10B981',
        },
        surface: {
          background: '#F8FAFC',
          card: '#FFFFFF',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Lexend', 'sans-serif'],
      },
      borderRadius: {
        'brand': '0.75rem',
      }
    },
  },
  plugins: [],
}