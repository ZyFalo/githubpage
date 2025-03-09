//// filepath: c:\Users\User\Desktop\albumDjango\album\static\js\main.js
// Función para alternar el tema
function toggleTheme() {
    const body = document.getElementById("bodyElement");
    body.classList.toggle("bg-dark-custom");
    body.classList.toggle("text-light-custom");
    body.classList.toggle("bg-light");
    body.classList.toggle("text-dark");

    // Guardar el estado del tema en localStorage
    if (body.classList.contains("bg-dark-custom")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Aplicar el tema guardado al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        const body = document.getElementById("bodyElement");
        body.classList.add("bg-dark-custom", "text-light-custom");
        body.classList.remove("bg-light", "text-dark");
    }
});