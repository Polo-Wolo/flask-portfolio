module.exports = {
  content: [
    "./templates/**/*.{html,htm}",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'raisin': '#17171D',
        'pantone': '#4472ca',
        'jet': "#1F1F24",
        'dim': "#3A3A40",
      },
      fontFamily: {
        'sulphur': ['Sulphur Point', 'sans-serif'],
        'mitr': ['Mitr', 'sans-serif'],
      },
      transitionProperty: {
        'width': 'width',
      },
    },
  },
  plugins: [],
}
