/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './django_ledger/templates/**/*.html',
    './static_custom/**/*.js',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'dark-bg': '#0a0a0a',
        'dark-card': '#1a1a1a',
        'dark-border': '#2a2a2a',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
