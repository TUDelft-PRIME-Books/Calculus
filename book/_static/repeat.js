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

async function replaceWithTransition(oldElement, newElement) {
	if (!oldElement || !newElement) {
		return;
	}
	oldElement.replaceWith(newElement);
}

document.addEventListener("DOMContentLoaded", async () => {
	const repeatElements = document.querySelectorAll("div.admonition.repeat");

	for (const element of repeatElements) {
		const titleParagraph = element.querySelector("p.admonition-title");
		if (!titleParagraph) {
			continue;
		}

		const titleLink = titleParagraph.querySelector("a");
		if (!titleLink) {
			continue;
		}

		const href = titleLink.getAttribute("href");
		if (!href) {
			continue;
		}

		const referenceUrl = new URL(href, window.location.href);
		const targetId = decodeURIComponent(referenceUrl.hash.replace("#", ""));
		if (!targetId) {
			continue;
		}

		let referencedElement = null;
		const referencedPageUrl = `${referenceUrl.origin}${referenceUrl.pathname}${referenceUrl.search}`;
		const currentPageUrl = `${window.location.origin}${window.location.pathname}${window.location.search}`;

		if (referencedPageUrl === currentPageUrl) {
			referencedElement = document.getElementById(targetId);
		} else {
			const response = await fetch(referenceUrl.href);
			if (!response.ok) {
				continue;
			}

			const html = await response.text();
			const doc = new DOMParser().parseFromString(html, "text/html");
			referencedElement = doc.getElementById(targetId);
		}

		if (referencedElement) {
			const replacement = elementFromHTML(referencedElement.outerHTML);
			if (!replacement) {
				continue;
			}

			await replaceWithTransition(element, replacement);
			await renderInsertedMath(replacement);
		}
	}
});
