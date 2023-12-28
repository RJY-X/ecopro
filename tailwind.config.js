/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./ecopro/ecom/templates/**/*.html","./ecopro/ecom/static/**/*.css",,"./ecopro/ecom/static/**/*.js"],
  theme: {
    extend: {fontFamily: {
      'body': "Inter",'header': 'Bebas Neue'    },},
  },
  plugins: [],
}

