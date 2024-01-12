import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const cookies = new universalCookie(null, { path: "/" });

const btns = document.querySelectorAll("[data-add-to-cart-btn]");

function getData(btn) {
	const flavor = document
		.querySelector("[data-flavors-list]")
		.getAttribute("data-flavor-value");

	let quantity = Number(document.querySelector("#quantity-value").value);

	const productId = Number(btn.getAttribute("data-product-id"));

	const price = Number(
		document.getElementById("product-price").getAttribute("data-price")
	);

	const serving = document.querySelector("[data-serving-option]:checked").value;

	if (isNaN(quantity) === true || quantity < 1) quantity = 1;

	if (productId <= 0 || isNaN(productId)) {
		console.log("please set product id", productId);
		return;
	}
	return {
		flavor,
		productId,
		quantity,
		price,
		serving,
	};
}

async function addToCart(data) {
	const csrftoken = cookies.get("csrftoken");
	console.log("🚀 ~ token ~", csrftoken);
	const url = "http://127.0.0.1:8000/cart/add_to_cart";
	const method = "POST";
	const headers = {
		"Content-Type": "application/json",
		"X-CSRFToken": csrftoken,
	};

	const res = await fetch(url, {
		method,
		headers,
		body: JSON.stringify(data),
	});

	json = await res.json();

	console.log(json);
}

btns.forEach((btn) => {
	btn.addEventListener("click", () => {
		const data = getData(btn);
		console.log("🚀 ~ data ~", data);
		addToCart(data);
	});
});
