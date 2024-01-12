const dropDownBtn = document.querySelectorAll("[data-dropDown-btn]");

function toggleDropDown(dropDownId) {
	const dropDown = document.querySelector(
		`[data-dropDown-list="${dropDownId}"]`
	);
	dropDown.classList.toggle("invisible");
	dropDown.classList.toggle("opacity-0");
}

dropDownBtn.forEach((el) => {
	el.addEventListener("click", (e) => {
		const dropDownId = e.target.getAttribute("data-dropDown-btn");
		toggleDropDown(dropDownId);
	});
});

const dropDownItems = document.querySelectorAll("[data-dropDown-item]");

function chooseServing(event) {
	const productId = event.target.getAttribute("product-id");
	const serving = event.target.getAttribute("item-value");
	const btn = document.querySelector(`[data-dropDown-btn="${productId}"]`);
	const listContainer = document.querySelector(
		`[data-dropDown-list="${productId}"]`
	);
	listContainer.setAttribute("data-dropDown-serving", serving);
	btn.innerHTML = `
	${serving} servings
	<span class="material-symbols-outlined text-lg">
	expand_more
	</span>`;

	toggleDropDown(productId);
}

function updatePrice(event) {
	const price = event.target.getAttribute("item-price");
	const pricing = document.querySelector("[data-pricing]");

	pricing.textContent = `${price} DH`;
	pricing.setAttribute("data-price", price);
}

dropDownItems.forEach((el) => {
	el.addEventListener("click", (e) => {
		chooseServing(e);
		updatePrice(e);
	});
});
