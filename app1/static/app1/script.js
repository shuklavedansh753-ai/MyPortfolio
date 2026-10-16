
document.addEventListener("DOMContentLoaded", () => {
    const animatedElements = document.querySelectorAll(
        "#about, #experience .experience-card, " +
        "#skills .skills span, #projects .project-card, #contact"
    );

    // Gracefully show everything if animation is unsupported.
    if (!("IntersectionObserver" in window)) {
        animatedElements.forEach((element) => {
            element.classList.add("is-visible");
        });
        return;
    }

    const observer = new IntersectionObserver(
        (entries, observerInstance) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observerInstance.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.12
        }
    );

    animatedElements.forEach((element, index) => {
        element.classList.add("reveal");
        element.style.setProperty(
            "--reveal-delay",
            `${(index % 5) * 90}ms`
        );
        observer.observe(element);
    });
});
