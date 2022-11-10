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
      saturate: {
        85: '.85',
      },
      keyframes: {
        wiggle: {
          '0%, 50%': { transform: 'rotate(-15deg)' },
          '25%': { transform: 'rotate(15deg)' },
        }
      },
      animation: {
        wiggle: 'wiggle 1s ease-in-out infinite',
      }
    },
  },
  plugins: [],
}
