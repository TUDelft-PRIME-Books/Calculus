(() => {
    const IFRAME_SELECTOR = "iframe.prime-applet";

    // Afstand buiten viewport voordat een iframe wordt verwijderd.
    const ROOT_MARGIN = "1500px"; // close the defaults in Chrome

    class ManagedIframe {
        constructor(iframe) {
            this.loaded = false;
            this.iframe = iframe;

            // Bewaar originele markup
            this.attributes = {};
            for (const attr of iframe.attributes) {
                this.attributes[attr.name] = attr.value;
            }

            this.placeholder = document.createElement("div");
            this.placeholder.className = "prime-applet-placeholder";

            this.currentHeight = null;
            this.currentWidth = null;

            iframe.addEventListener(
                "load",
                () => {
                    this.loaded = true;
                    this.installResizeObserver();
                    this.captureSize();
                },
                { once: true }
            );
        }

        installResizeObserver() {
            if (this.resizeObserver) {
                this.resizeObserver.disconnect();
            }

            this.resizeObserver = new ResizeObserver(() => {
                this.captureSize();
            });

            this.resizeObserver.observe(this.iframe);
        }

        captureSize() {
            if (!this.iframe?.isConnected) {
                return;
            }

            const rect = this.iframe.getBoundingClientRect();

            if (rect.height > 0) {
                this.currentHeight = rect.height;
                this.placeholder.style.height =
                    `${this.currentHeight}px`;
            }

            if (rect.width > 0) {
                this.currentWidth = rect.width;
                this.placeholder.style.width =
                    `${this.currentWidth}px`;
            }
        }

        unload() {

            if (!this.loaded) {
                return;
            }

            if (!this.iframe?.isConnected) {
                return;
            }

            this.captureSize();

            if (this.resizeObserver) {
                this.resizeObserver.disconnect();
            }

            this.iframe.replaceWith(this.placeholder);

            this.iframe.remove();
        }

        reload() {

            if (!this.placeholder.isConnected) {
                return;
            }

            const iframe = document.createElement("iframe");

            for (const [name, value] of Object.entries(this.attributes)) {
                iframe.setAttribute(name, value);
            }

            if (this.currentHeight) {
                iframe.style.height = `${this.currentHeight}px`;
            }

            this.placeholder.replaceWith(iframe);

            this.iframe = iframe;

            iframe.addEventListener(
                "load",
                () => {
                    this.installResizeObserver();
                    this.captureSize();
                },
                { once: true }
            );
        }
    }

    const initialize = () => {
        const managedIframes = new Map();

        let count = 0;
        document.querySelectorAll(IFRAME_SELECTOR).forEach((iframe) => {
            managedIframes.set(iframe, new ManagedIframe(iframe));
            count++;
        });
        console.log("Total number of managed iframes:", count);

        const observer = new IntersectionObserver(
            (entries) => {
                for (const entry of entries) {
                    const element = entry.target;

                    let managed = managedIframes.get(element);

                    if (!managed) {
                        for (const candidate of managedIframes.values()) {
                            if (candidate.placeholder === element) {
                                managed = candidate;
                                break;
                            }
                        }
                    }

                    if (!managed || !managed.loaded) {
                        continue;
                    }

                    if (entry.isIntersecting) {
                        if (managed.placeholder.isConnected) {
                            managed.reload();

                            observer.unobserve(managed.placeholder);
                            observer.observe(managed.iframe);
                        }
                    } else {
                        if (managed.iframe.isConnected) {
                            managed.unload();

                            observer.unobserve(managed.iframe);
                            observer.observe(managed.placeholder);
                        }
                    }
                }
            },
            {
                root: null,
                rootMargin: ROOT_MARGIN,
                threshold: 0
            }
        );

        for (const managed of managedIframes.values()) {
            observer.observe(managed.iframe);
        }
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initialize, { once: true });
    } else {
        initialize();
    }
})();