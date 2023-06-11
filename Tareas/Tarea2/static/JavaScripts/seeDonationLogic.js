const ventanaEmergente = document.getElementById("ventana-emergente");
function agrandarImagen(i){
    console.log('wea')
    ventanaEmergente.innerHTML ='<img class="granFoto" src='+i+'>';
    ventanaEmergente.style.display = 'block';
}

function desaparecer(){
    ventanaEmergente.style.display = 'None';
}