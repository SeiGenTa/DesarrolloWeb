//STATUS VARIABLES
let status_region = false;
let status_comuna = false;
let status_tipoPedido = false;
let status_descripcion = false;
let status_cantidad = false;
let status_name = false;
let status_email = false;
let status_numeroCelular = true; //es el unico opcional

//Todas las id de la pagina
const idRegion = document.getElementById('regiones');
const idComuna = document.getElementById('comunas');
const idTipoDonacion = document.getElementById('tipe-order')
const idDescripcion = document.getElementById('descripcion')
const idCantida = document.getElementById('cantidad')
const idName = document.getElementById('name')
const idEmail = document.getElementById('email')
const idNumero = document.getElementById('number-phone')
const ventanaEmergente = document.getElementById('ventana-emergente');
const form = document.getElementById('formulario')
const buton = document.getElementById('buttonValidate')

//Seleccion de comuna
let predReg = '<option value="0">Seleccione región</option>';
let predCom = '<option value="0">Seleccione región</option>';

fetch('/get_regions')
	.then(function(response){
		return response.json();
	})
	.then(function(data) {
		dataRegions = [];
		data.forEach(element => {
			dataRegions.push(element);
		});
	for(i = 0; i < dataRegions.length; i++){
		predReg += '<option value="' + dataRegions[i][0] + '">' + dataRegions[i][1] + '</option>';
	}
    console.log("se consiguio")
	idRegion.innerHTML = predReg;
})

//Cambio de las comunas segun la region
function createComunaSelect(){
	var val = document.getElementById('regiones').value;
	if (val != 0){
		idRegion.style.border = "2px solid rgba(0,0,0,0.2)";
        status_region = true;
        predCom = '<option value="0">Seleccione comuna</option>'
		fetch('/get_communes', {method: 'POST', headers: {'Content-Type': 'application/json'},
			body: JSON.stringify({'inf':idRegion.value})
		})
		.then(function(response) {
			return response.json();
		})
		.then(
			function(data) {
				console.log(data);
				dataCommunes = [];
				predCom = '<option value="0">Seleccione comuna</option>';
				data.forEach(element => {
					dataCommunes.push(element);
				});
				for(i = 0; i < dataCommunes.length; i++){
					predCom += '<option value="' + dataCommunes[i][1] + '">' + dataCommunes[i][2] + '</option>';
				}
				idComuna.innerHTML = predCom;
			}
		)
	}
    else {
		idRegion.style.border = "2px solid red";
		predCom = '<option value="0">Seleccione región</option>'
    	status_region = false;
	}
	idComuna.innerHTML = predCom;
}

//validacion de la comuna
function validationComuna(){
    if (idComuna.value != 0) {
        status_comuna = true;
        idComuna.style.border = "2px solid rgba(0,0,0,0.2)";
    }
    else {
        status_comuna = false;
        idComuna.style.border = "2px solid red"
    }
}

//validacion del tipo de donacion
function validationTipo(){
    if (idTipoDonacion.value != 0) {
        status_tipoPedido = true;
        idTipoDonacion.style.border = "2px solid rgba(0,0,0,0.2)";
    }
    else{
        status_tipoPedido = false;
        idTipoDonacion.style.border = "2px solid red"
    } 
}

//validacion de descripcion
function validacionDescripcion(){
    if (idDescripcion.value == ''){
        status_descripcion = false;
        idDescripcion.style.border = "2px solid red"
    } else if (idDescripcion.value.length > 250){
        status_descripcion = false;
        idDescripcion.style.border = "2px solid red"
    } else{
        status_descripcion = true;
        idDescripcion.style.border = "2px solid rgba(0,0,0,0.2)";
    }
}

//validacion de la cantidad
function validateCantidad(){
	const isNumber = /^[0-9]+[a-zA-Z]{0,3}$/;
	if (!isNumber.test(idCantida.value)){
		alert("inserte cantidad valida (por ejemplo 10L)");
		idCantida.value = '';
		idCantida.style.border = "2px solid red";
        status_cantidad = false;
		return;
	}
	const numberCant = parseInt(idCantida.value);
	if (numberCant < 0){
		alert('Inserte valor valido');
		idCantida.value = '';
		idCantida.style.border = "2px solid red";
        status_cantidad = false;
		return;
	}
	if (idCantida.value.length > 10){
		alert("se excedio largo maximo de paramatro");
		idCantida.value = '';
		idCantida.style.border = "2px solid red";
        status_cantidad = false;
		return
	}
	idCantida.style.border = "2px solid rgba(0,0,0,0.2)";
    status_cantidad = true;
	return;
}

//validacion del nombre
function validateName(){
    if (idName.value.length < 3){
        idName.style.border = "2px solid red";
        status_name = false;
        idName.value = '';
    }
    else{
        status_name = true;
        idName.style.border = "2px solid rgba(0,0,0,0.2)";
    }
}

//Validate email
function validaEmail(){
	const regexEmail = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
	const emailIngresado = idEmail.value

	if(!regexEmail.test(emailIngresado)){
		alert('Formato de email no valido');
		idEmail.value = '';
		idEmail.style.border = "2px solid red";
        status_email = false;
		return;
	}
	if (emailIngresado.length > 80){
		idEmail.style.border = "2px solid red";
        status_email = false;
		return;
	}
	idEmail.style.border = "2px solid rgba(0,0,0,0.2)";
    status_email = true;
	return;
}

//Validacion del numero
function validateNumberPhone(){
	const regexTelefono = /^\+569\d{8}$/;
	const numeroTelefono = idNumero.value;
	if (numeroTelefono == ''){
		idNumero.style.border = "2px solid rgba(0,0,0,0.2)";
        status_numeroCelular = true;
	}else if (!regexTelefono.test(numeroTelefono)) {
		idNumero.value = '';
		alert('El número de teléfono ingresado no es válido');
		idNumero.style.border = "2px solid red";
        status_numeroCelular = false;
	}else if (numeroTelefono.length > 15){
		alert('El número de teléfono demasiado largo');
		idNumero.style.border = "2px solid red";
        status_numeroCelular = false;
	}else{
	console.log('El número de teléfono ingresado es válido');
	idNumero.style.border = "2px solid rgba(0,0,0,0.2)";
    status_numeroCelular = true;
	return;
    }
}

buton.addEventListener('click',function(evento) {
	evento.preventDefault();

	console.log("se esta ejecutando")

	let validate = true;
	if (!status_region){
		validate = false;
		createComunaSelect()
	}
	if (!status_comuna){
		validate = false;
		validationComuna()
	}
	if (!status_tipoPedido){
		validate = false;
		validationTipo()
	}if	(!status_descripcion){
		validate = false;
		validacionDescripcion()
	}if	(!status_cantidad){
		validate = false;
		validateCantidad()
	}if	(!status_name){
		validate = false;
		validateName();
	}if (!status_email){
		validate = false;
		validaEmail()
	}if	(!status_numeroCelular){
		validate = false;
		validateNumberPhone()
	}

	
	if (validate){
		console.log("se confirmo");
		ventanaEmergente.style.display = "block";
	}
})

function aceptated(n){
	if (n == 1) form.submit();
	else ventanaEmergente.style.display = "None";
}
