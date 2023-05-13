informacionDonancion = {
    "Region":"Región del Libertador Gral. Bernardo O’Higgins", 
    "Comuna":"Pichilemu",
    "Calle":"Cahuil 787",
    "Tipo":"Frutas",
    "Cantidad":"10u",
    "Fotos":["photo1.jpg","photo2.jpg"],
    "Fecha":"2023-04-18",
    "Descripcion":"Esto es una donacion de 10 Sandias maduritas para su consumo",
    "Nombre":"Juan Esteban Maran",
    "Email":"juanEMaran@gmail.com",
    "Numero":"+569 347854234"
}

const idRegion      = document.getElementById("infReg");
const idComuna      = document.getElementById("infComuna");
const idCalle       = document.getElementById("infCalle");
const idTipo        = document.getElementById("infTipo");
const idCantidad    = document.getElementById("infCant");
const idFotos       = document.getElementById("infFotos");
const idFecha       = document.getElementById("infFecha");
const idDescripcion = document.getElementById("infDescr");
const idNombre      = document.getElementById("infNomb");
const idEmail       = document.getElementById("infEmail");
const idNumero      = document.getElementById("infNumero");

function main(){
    idRegion.innerHTML = informacionDonancion.Region;
    idComuna.innerHTML = informacionDonancion.Comuna;
    idCalle.innerHTML = informacionDonancion.Calle;
    idTipo.innerHTML = informacionDonancion.Tipo
    idCantidad.innerHTML = informacionDonancion.Cantidad

    const length = (informacionDonancion.Fotos).length;
    let text = '';
    for (i = 0; i < length; i++){
        text += '<img onclick="agrandarImagen('+i+')" class:"fotos_informacion" src="../photos/'+(informacionDonancion.Fotos)[i]+'">';
    }

    idFotos.innerHTML = text;
    idFecha.innerHTML = informacionDonancion.Fecha;
    idDescripcion.innerHTML = informacionDonancion.Descripcion;
    idNombre.innerHTML = informacionDonancion.Nombre;
    idEmail.innerHTML = informacionDonancion.Email;
    idNumero.innerHTML = informacionDonancion.Numero;
}

main()

const ventanaEmergente = document.getElementById("ventana-emergente");
function agrandarImagen(i){
    ventanaEmergente.innerHTML ='<img src=i>';
    ventanaEmergente.style.display = 'block';
}

function desaparecer(){
    ventanaEmergente.style.display = 'None';
}