//---------------------JS DE LOS BOTONES PARA SELECCIONAR LAS HABITACIONES------------------------

// Funciones para cambiar la visualizacion de los botones y ocultar informacion ademas de dar el color que avisa que boton esta activo.

document.addEventListener("DOMContentLoaded", function() {
    const normalBtn = document.querySelector(".normal-btn");
    const superBtn = document.querySelector(".super-btn");
    const premiumBtn = document.querySelector(".premium-btn");
    const normalContent = document.querySelector(".normal");
    const superContent = document.querySelector(".super");
    const premiumContent = document.querySelector(".premium");
    const buttons = document.querySelectorAll(".btn-room");

    // con esta funcion activamos y desactivamos los demas botones.

    function handleButtonClick(button, showContent, hideContents) {
        // Remueve la clase activa de todos los botones
        buttons.forEach(btn => btn.classList.remove("active"));

        // Añadade la clase activa al botón clicado
        button.classList.add("active");

        // Muestra el contenido correspondiente
        showContent.style.display = "block";
        hideContents.forEach(content => content.style.display = "none");
    }

    // con esto nos indica que boton esta mostando y en [] cuales esta ocultando

    normalBtn.addEventListener("click", function() {
        handleButtonClick(normalBtn, normalContent, [superContent, premiumContent]);
    });

    superBtn.addEventListener("click", function() {
        handleButtonClick(superBtn, superContent, [normalContent, premiumContent]);
    });

    premiumBtn.addEventListener("click", function() {
        handleButtonClick(premiumBtn, premiumContent, [normalContent, superContent]);
    });

    // Muestra el contenido normal por defecto para que exista informacion al cargar la pagina.
    handleButtonClick(normalBtn, normalContent, [superContent, premiumContent]);
});

// ---------------------FIN JS DE LOS BOTONES PARA SELECCIONAR LAS HABITACIONES---------------------