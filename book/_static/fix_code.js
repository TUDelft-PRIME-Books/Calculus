window.addEventListener("DOMContentLoaded", () => {
    window.onbeforeunload = null;

    window.addEventListener = new Proxy(window.addEventListener, {
        apply(target, thisArg, args) {
            if (args[0] === "beforeunload") {
                return; // block
            }
            return Reflect.apply(target, thisArg, args);
        }
    });
});