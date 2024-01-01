const dropDownBtn = document.querySelectorAll("[data-dropDown-btn]");

function toggleDropDown(dropDownId) {
	const dropDown = document.querySelector(
		`[data-dropDown-list="${dropDownId}"]`
	);
	console.log(dropDown);

	dropDown.classList.toggle("invisible");
	dropDown.classList.toggle("opacity-0");
}

dropDownBtn.forEach((el) => {
	el.addEventListener("click", (e) => {
		const dropDownId = e.target.getAttribute("data-dropDown-btn");
		console.log(e.target);

		toggleDropDown(dropDownId);
	});
});

const dropDownItems = document.querySelectorAll("[data-dropDown-item]");

function chooseServing(event) {
	const productId = event.target.getAttribute("product-id");
	const serving = event.target.getAttribute("item-value");
	const btn = document.querySelector(`[data-dropDown-btn="${productId}"]`);
	btn.innerHTML = `
	${serving} servings
	<span class="material-symbols-outlined text-lg">
	expand_more
	</span>`;

	toggleDropDown(productId);
}

dropDownItems.forEach((el) => {
	el.addEventListener("click", chooseServing);
});
