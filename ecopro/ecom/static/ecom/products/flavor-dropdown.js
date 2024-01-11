const dropDownBtn = document.querySelector("#flavor-btn");

function toggleDropDown() {
	const flavorsList = document.querySelector(`[data-flavors-list]`);

	flavorsList.classList.toggle("invisible");
	flavorsList.classList.toggle("opacity-0");
}

dropDownBtn.addEventListener("click", (e) => {
	const btnIcon = document.querySelector("#flavor-btn-icon");

	toggleDropDown();
	btnIcon.classList.toggle("rotate-180");
});

const flavors = document.querySelectorAll("[data-flavor-item]");

function changeElementText(selector, text) {
	const el = document.querySelector(selector);

	el.textContent = text;
}

function selectFlavor(event) {
	const flavor = event.target
		.closest("[data-flavor-item]")
		.getAttribute("data-flavor-value");

	return flavor;
}

function selectFlavorImageURLs(event) {
	const pickedFlavor = event.target.closest("[data-flavor-item]");

	return {
		sm: pickedFlavor.getAttribute("data-flavor-img-small"),
		md: pickedFlavor.getAttribute("data-flavor-img-medium"),
		lg: pickedFlavor.getAttribute("data-flavor-img-large"),
	};
}

function setFlavorImage(selector, url) {
	const image = document.querySelector(selector);

	image.src = url;
}

function setFlavorValue(flavor) {
	const flavorsList = document.querySelector(`[data-flavors-list]`);

	flavorsList.setAttribute("data-flavor-value", flavor);
}

flavors.forEach((el) => {
	el.addEventListener("click", (e) => {
		const flavor = selectFlavor(e);
		toggleDropDown();
		changeElementText("#flavor-btn-text", flavor);
		changeElementText("#sub-headline", flavor);
		setFlavorValue(flavor);

		const urls = selectFlavorImageURLs(e);
		setFlavorImage("#flavor-btn-img", urls.sm);
		setFlavorImage("#flavor-img-md", urls.md);
		setFlavorImage("#flavor-img-lg", urls.lg);
	});
});
