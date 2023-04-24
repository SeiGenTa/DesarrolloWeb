informacion={
    "Region":"Región del Libertador Gral. Bernardo O’Higgins",
    "Comuna":"San Fernando",
    "Tipo":"Otros",
    "Descripcion":"Necesitamos leche para mis 3 hijos",
    "Cantidad":"10L",
    "Nombre":"Ricardo Arjonas",
    "Email":"ricardArjArtis@gmail.cl",
    "Numero":"+569 34564523",
}

const idRegion      = document.getElementById("region");
const idComuna      = document.getElementById("Comuna");
const idTipo        = document.getElementById("tipo");
const idCantidad    = document.getElementById("cantidad");
const idDescripcion = document.getElementById("descripcion");
const idNombre      = document.getElementById("nombre");
const idEmail       = document.getElementById("email");
const idNumero      = document.getElementById("numero");

function main(){
    idRegion.innerHTML = informacion.Region;
    idComuna.innerHTML = informacion.Comuna;
    idTipo.innerHTML = informacion.Tipo
    idCantidad.innerHTML = informacion.Cantidad
    idDescripcion.innerHTML = informacion.Descripcion;
    idNombre.innerHTML = informacion.Nombre;
    idEmail.innerHTML = informacion.Email;
    idNumero.innerHTML = informacion.Numero;
}

main()