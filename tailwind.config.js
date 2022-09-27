/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}",
  "./cart/**/*.{html,js}",
  "./checkout/**/*.{html,js}",
  "./store/**/*.{html,js}",
  "./user_account/**/*.{html,js}",],
  theme: {
    extend: {},
  },
  plugins: [
    require('tw-elements/dist/plugin'),
  ]
  }
