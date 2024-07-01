//JS DEL CONTENIDO BASE

// menú desplegable y barra derecha 

let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.header .navbar');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}

// Fin menú desplegable y barra derecha 

// FIN JS DEL CONTENIDO BASE