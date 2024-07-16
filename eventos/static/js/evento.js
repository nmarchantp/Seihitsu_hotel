// Funciones para cambiar la visualizacion de los botones y ocultar informacion

document.addEventListener("DOMContentLoaded", function() {
    const normalBtn = document.querySelector(".normal-btn");
    const superBtn = document.querySelector(".super-btn");
    const premiumBtn = document.querySelector(".premium-btn");
    const normalContent = document.querySelector(".normal");
    const superContent = document.querySelector(".super");
    const premiumContent = document.querySelector(".premium");
    const buttons = document.querySelectorAll(".btn-room");

    function handleButtonClick(button, showContent, hideContents) {
        // Remover clase activa de todos los botones
        buttons.forEach(btn => btn.classList.remove("active"));

        // Añadir clase activa al botón clicado
        button.classList.add("active");

        // Mostrar el contenido correspondiente
        showContent.style.display = "block";
        hideContents.forEach(content => content.style.display = "none");
    }

    normalBtn.addEventListener("click", function() {
        handleButtonClick(normalBtn, normalContent, [superContent, premiumContent]);
    });

    superBtn.addEventListener("click", function() {
        handleButtonClick(superBtn, superContent, [normalContent, premiumContent]);
    });

    premiumBtn.addEventListener("click", function() {
        handleButtonClick(premiumBtn, premiumContent, [normalContent, superContent]);
    });

    // Mostrar el contenido normal por defecto
    handleButtonClick(normalBtn, normalContent, [superContent, premiumContent]);
});
