/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./ecopro/ecom/templates/**/*.html",
		"./ecopro/ecom/static/**/*.css",
		,
		"./ecopro/ecom/static/**/*.js",
	],
	theme: {
		extend: {
			fontFamily: {
				body: "Inter",
				header: "Bebas Neue",
			},
			backgroundImage: {
				"left-triangle": "linear-gradient(45deg, #F87171 6%, #0a0a0a 6%)",
				"right-triangle": "linear-gradient(45deg, #0a0a0a 94%, #F472B6 0%)",
			},
		},
	},
	plugins: [require("@tailwindcss/forms")],
};
