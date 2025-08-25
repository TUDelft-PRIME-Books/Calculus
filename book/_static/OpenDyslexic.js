AccessibilitySVG = `<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%;">
<path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="var(--pst-color-text-muted)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 9L12 10M17 9L12 10M12 10V13M12 13L10 18M12 13L14 18" stroke="var(--pst-color-text-muted)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12 7C11.7239 7 11.5 6.77614 11.5 6.5C11.5 6.22386 11.7239 6 12 6C12.2761 6 12.5 6.22386 12.5 6.5C12.5 6.77614 12.2761 7 12 7Z" fill="var(--pst-color-text-muted)" stroke="var(--pst-color-text-muted)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`

document.addEventListener("DOMContentLoaded", () => {
    const headerEnd = document.querySelector(".article-header-buttons");
    if (headerEnd) {
        const button = document.createElement("button");
        button.id = "AcccessibilityID";
        button.className = "btn btn-sm nav-link pst-navbar-icon pst-js-only";
        button.title = "Acccessibility menu";
        button.innerHTML = `<span style="display: inline-flex; align-items: center; justify-content: center; width: 1.2em; height: 1.2em;">${AccessibilitySVG}</span>`;

        headerEnd.prepend(button);
    }
});