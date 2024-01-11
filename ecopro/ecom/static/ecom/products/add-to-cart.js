const btns = document.querySelectorAll("[data-add-to-cart-btn]");

btns.forEach((btn) => {
	btn.addEventListener("click", () => {
		const flavor = document
			.querySelector("[data-flavors-list]")
			.getAttribute("data-flavor-value");

		let quantity = Number(document.querySelector("#quantity-value").value);

		if (isNaN(quantity) === true || quantity < 1) quantity = 1;

		const productId = Number(btn.getAttribute("data-product-id"));

		if (productId <= 0 || isNaN(productId)) {
			console.log("please set product id", productId);
			return;
		}

		const price = Number(
			document.getElementById("product-price").getAttribute("data-price")
		);

		const data = {
			flavor,
			productId,
			quantity,
			price,
		};
	});
});
