//---------------------JS DE LOS BOTONES PARA SELECCIONAR LAS HABITACIONES------------------------

// Funciones para cambiar la visualizacion de los botones y ocultar informacion ademas de dar el color que avisa que boton esta activo.

document.addEventListener("DOMContentLoaded", function() {
    const santiagoRestBtn = document.querySelector(".santiago-rest-btn");
    const vinaRestBtn = document.querySelector(".vina-rest-btn");
    const santiagoRestContent = document.querySelector(".santiago-rest");
    const vinaRestContent = document.querySelector(".vina-rest");
    const buttons = document.querySelectorAll(".btn-resto");

    function handleButtonClick(button, showContent, hideContents) {
        // Remover clase activa de todos los botones
        buttons.forEach(btn => btn.classList.remove("active"));

        // Añadir clase activa al botón clicado
        button.classList.add("active");

        // Mostrar el contenido correspondiente
        showContent.style.display = "block";
        hideContents.forEach(content => content.style.display = "none");
    }

    santiagoRestBtn.addEventListener("click", function() {
        handleButtonClick(santiagoRestBtn, santiagoRestContent, [vinaRestContent]);
    });

    vinaRestBtn.addEventListener("click", function() {
        handleButtonClick(vinaRestBtn, vinaRestContent, [santiagoRestContent]);
    });

    // Mostrar el contenido de Santiago por defecto
    handleButtonClick(santiagoRestBtn, santiagoRestContent, [vinaRestContent]);
});


// ---------------------FIN JS DE LOS BOTONES PARA SELECCIONAR LAS HABITACIONES---------------------