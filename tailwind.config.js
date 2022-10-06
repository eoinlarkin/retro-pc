/** @type {import('tailwindcss').Config} */
module.exports = {
  important: true,
  content: ["./templates/*.{html,js}",
  "./templates/**/*.{html,js}",
  "./cart/**/*.{html,js}",
  "./checkout/**/*.{html,js}",
  "./store/**/*.{html,js}",
  "./user_account/**/*.{html,js}",],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'yellow': '#D97706',
      'blue': '#235789',
      'black': '#000000',
      'white': '#F4F4F5',
      'red': '#9B1D20',
      'green': '#3F8D48',
      'pure-white': '#FFF',
      'gray': '#cbd5e1'
    },
  },
  plugins: [
    require('tw-elements/dist/plugin'),
  ]
  }
