const servingInput = document.querySelectorAll("[data-serving-option]");

servingInput.forEach((el) => {
	el.addEventListener("change", () => {
		const checkedServingInput = document.querySelector(
			"[data-serving-option]:checked"
		);
		const price = checkedServingInput.getAttribute("data-serving-price");

		const pricing = document.querySelector("#product-price");
		pricing.setAttribute("data-price", price);
		pricing.textContent = `${price} DH`;
	});
});
