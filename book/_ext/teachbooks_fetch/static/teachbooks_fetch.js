async function renderInsertedMath(node) {
	if (!node) {
		return;
	}

	if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
		await window.MathJax.typesetPromise([node]);
		return;
	}

	if (window.MathJax && window.MathJax.Hub && typeof window.MathJax.Hub.Queue === "function") {
		window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, node]);
	}
}

function elementFromHTML(html) {
	const template = document.createElement("template");
	template.innerHTML = html.trim();
	return template.content.firstElementChild;
}

function handleFetchFailure(element, titleParagraph, titleLink) {
	// Update title to show fetch failed, keeping the original link if it exists
	if (titleLink) {
		titleParagraph.innerHTML = "Failed to fetch ";
		// Reactivate the original link
		titleLink.setAttribute("href", titleLink.dataset.fetchHref || titleLink.getAttribute("href"));
		titleLink.removeAttribute("aria-disabled");
		titleLink.style.color = "";
		titleLink.style.textDecoration = "";
		titleLink.style.cursor = "";
		titleParagraph.appendChild(titleLink.cloneNode(true));
		
	} else {
		titleParagraph.innerHTML += " failed";
	}

	// Remove all child elements except the title paragraph
	const children = Array.from(element.children);
	children.forEach(child => {
		if (child !== titleParagraph) {
			child.remove();
		}
	});

	// Add a new paragraph with failure message
	const failureParagraph = document.createElement("p");
	failureParagraph.textContent = "Fetching failed.";
	element.appendChild(failureParagraph);

	// Add a class to indicate fetch failure for styling
	element.classList.add("failed-to-fetch");
}

async function replaceWithTransition(oldElement, newElement) {
	if (!oldElement || !newElement) {
		return;
	}
	oldElement.replaceWith(newElement);
}

async function processfetchElement(element) {
	const titleParagraph = element.querySelector("p.admonition-title");
	if (!titleParagraph) {
		return;
	}

	const titleLink = titleParagraph.querySelector("a");
	if (!titleLink) {
		handleFetchFailure(element, titleParagraph, null);
		return;
	}

	const href = titleLink.getAttribute("href") || titleLink.dataset.fetchHref;
	if (!href) {
		handleFetchFailure(element, titleParagraph, titleLink);
		return;
	}

	const referenceUrl = new URL(href, window.location.href);
	const targetId = decodeURIComponent(referenceUrl.hash.replace("#", ""));
	if (!targetId) {
		handleFetchFailure(element, titleParagraph, titleLink);
		return;
	}

	let referencedElement = null;
	const referencedPageUrl = `${referenceUrl.origin}${referenceUrl.pathname}${referenceUrl.search}`;
	const currentPageUrl = `${window.location.origin}${window.location.pathname}${window.location.search}`;

	if (referencedPageUrl === currentPageUrl) {
		referencedElement = document.getElementById(targetId);
	} else {
		const response = await fetch(referenceUrl.href);
		if (!response.ok) {
			handleFetchFailure(element, titleParagraph, titleLink);
			return;
		}

		const html = await response.text();
		const doc = new DOMParser().parseFromString(html, "text/html");
		referencedElement = doc.getElementById(targetId);
	}

	if (referencedElement) {
		const replacement = elementFromHTML(referencedElement.outerHTML);
		if (!replacement) {
			handleFetchFailure(element, titleParagraph, titleLink);
			return;
		}

		await replaceWithTransition(element, replacement);
		await renderInsertedMath(replacement);
	} else {
		handleFetchFailure(element, titleParagraph, titleLink);
	}
}

document.addEventListener("DOMContentLoaded", async () => {
	const fetchElements = document.querySelectorAll("div.admonition.fetch");

	for (const element of fetchElements) {
		const titleParagraph = element.querySelector("p.admonition-title");
		const titleLink = titleParagraph ? titleParagraph.querySelector("a") : null;
		if (element.classList.contains("click-to-fetch")) {
			if (titleLink) {
				const manualHref = titleLink.getAttribute("href");
				if (manualHref) {
					titleLink.dataset.fetchHref = manualHref;
				}
				titleLink.removeAttribute("href");
				titleLink.setAttribute("aria-disabled", "true");
				titleLink.style.color = "inherit";
				titleLink.style.textDecoration = "none";
				titleLink.style.cursor = "inherit";
				titleLink.addEventListener("click", (event) => {
					event.preventDefault();
				});
			}

			element.addEventListener("click", async (event) => {
				event.preventDefault();
				if (element.dataset.fetchLoading === "1") {
					return;
				}
				element.dataset.fetchLoading = "1";
				try {
					await processfetchElement(element);
				} finally {
					delete element.dataset.fetchLoading;
				}
			}, { once: true });
			continue;
		}

		if (!element.classList.contains("cancel-fetch") && !element.classList.contains("click-to-fetch") && !element.classList.contains("failed-to-fetch")) {
			await processfetchElement(element);
		}
	}
});
