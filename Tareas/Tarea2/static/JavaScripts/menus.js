const table = document.getElementById('table-ord-dona'); // selecciona la tabla
table.addEventListener('click', function(event) {
    let target = event.target; // selecciona el elemento clicado
    while (target.nodeName !== 'TR') { // encuentra el padre tr
        target = target.parentNode;
    }
    let url = target.getAttribute('data-url'); // lee la URL de la fila
    if (url) { // si se encuentra la URL, redirige al usuario
        window.location.href = url;
    }
});

