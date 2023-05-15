//Configuracion inicial
const reg = document.getElementById('regiones');
const comunas = document.getElementById('comunas');
const boxFech = document.getElementById('fecha-disponibilidad');
const fileInput = document.getElementById('fotos');
const emailInput = document.getElementById('email_donante');
const direction = document.getElementById('direction');
const fechaInput = document.getElementById('fecha');
const number_phone = document.getElementById("number-phone");
const idCantida = document.getElementById('cantidad');
const tipeDonation = document.getElementById('tipe-donation');
const nameDonate = document.getElementById('name_donante');
const ventanaEmergente = document.getElementById('ventana-emergente');
const description = document.getElementById('descripcion')
const condicionDeRetiro = document.getElementById('condiciones')
const button = document.getElementById('buttonValidate')
const form = document.getElementById('formulario')

const emeReg = document.getElementById('emergenteRegion')
const emeCom = document.getElementById('emergenteCommune')
const emeDir = document.getElementById('emergentedirection')
const emeType = document.getElementById('emergentetype')
const emeAmount = document.getElementById('emergenteAmount')
const emeDate = document.getElementById('emergenteDate')
const emeDes = document.getElementById('emergenteDescription')
const emeCond = document.getElementById('emergenteCondition')
const emePhoto = document.getElementById('emergentePhotos')
const emeName = document.getElementById('emergenteName')
const emeEmail = document.getElementById('emergenteEmail')
const emeNum = document.getElementById('emergenteNumber')

dataRegions = []
dataCommunes = []

let predReg = '<option value="0">Seleccione región</option>';
let predCom = '<option value="0">Seleccione comuna</option>';

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
	reg.innerHTML = predReg;
})

reg.innerHTML = predReg;
comunas.innerHTML = predCom;

let validate_reg = false;
let validate_com = false;
let validate_calleNum = false;
let validate_tipe = false;
let validate_cantidad = false;
let validate_date_disp = false;
let validate_file = false;
let validate_name = false;
let validate_email = false;
let validate_number = false;

//Cambio de las comunas segun la region
function validateReg(){
	let val = reg;
	if (val.value != 0){	
		reg.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_reg = true; //a la vez lo validaremos
		fetch('/get_communes', {method: 'POST', headers: {'Content-Type': 'application/json'},
			body: JSON.stringify({'inf':reg.value})
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
				comunas.innerHTML = predCom;
			}
		)
	}
	else{
		reg.style.border = "2px solid red";
		validate_reg = false; //Si lo dejan vacio esto no estara validado
	}
}
reg.addEventListener('input', (event) => {validateReg()});

function validateComuna(){
	const val = comunas;
	if (val.value != 0){	
		dataCommunes.forEach(element =>{
			if (val.value == element[1]){
				validate_com = true; //a la vez lo validaremos
				val.style.border = "2px solid rgba(0,0,0,0.2)";
			}})
	}
	else{
		val.style.border = "2px solid red";
		validate_reg = false; //Si lo dejan vacio esto no estara validado
	}
}
comunas.addEventListener('input', (event) => {validateComuna()});

function validateDirection(){
	const val = direction;
	if (val.value == ""){
		val.style.border = "2px solid red";
		validate_calleNum = false; //Si lo dejan vacio esto no estara validado
	}
	else if (val.value.length > 80){
		alert('Se excedio el largo maximo de parametro')
		val.style.border = "2px solid red";
		val.value = '';
		validate_calleNum = false;
	}
	else{
		val.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_calleNum = true; //a la vez lo validaremos
	}
}
direction.addEventListener('input', (event) => {validateDirection()});


function validateTypeDonation(){
	const val = tipeDonation;
	if (val.value == '0'){
		val.style.border = "2px solid red";
		validate_tipe = false; //Si lo dejan vacio esto no estara validado
	}
	else{
		val.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_tipe = true; //a la vez lo validaremos
	}
}
tipeDonation.addEventListener('input', (event) => {validateTypeDonation()});

function validateCantidad(){
	const val = idCantida;
	const isValidate = /^[0-9]+[a-zA-Z]{0,3}$/;
	if (!isValidate.test(val.value)){
		alert("inserte cantidad valida (por ejemplo 10L)");
		val.value = '';
		val.style.border = "2px solid red";
		validate_cantidad = false; //Si lo dejan vacio esto no estara validado
		return
	}
	const numberCant = parseInt(idCantida.value);
	if (numberCant < 0){
		alert('Inserte valor valido');
		idCantida.value = '';
		idCantida.style.border = "2px solid red";
        status_cantidad = false;
		return;
	}
	else{
		val.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_cantidad = true; //a la vez lo validaremos
	}
}
idCantida.addEventListener('change', (event) => {validateCantidad()});

//Validacion fecha
function validaFecha(){
	const fechaIngresada = fechaInput.value;
	const regexFecha = /^(\d{4})-(\d{2})-(\d{2})$/;
	
	if (!regexFecha.test(fechaIngresada)) {
		alert('Formato de fecha no valido');
		fechaInput.value = '';
		fechaInput.style.border = "2px solid red";
		validate_date_disp = false;
		return;
	}
	
	const [_, anio, mes, dia] = regexFecha.exec(fechaIngresada);
    const fechaSeleccionada = new Date(anio, mes-1, dia);
	const fecha = new Date();
    fechaActual = new Date(fecha.getFullYear(), fecha.getMonth() ,fecha.getDate());
    
    if (fechaSeleccionada.getFullYear() != anio || fechaSeleccionada.getMonth() + 1 != mes || fechaSeleccionada.getDate() != dia) {
		alert('La fecha ingresada no es válida');
		fechaInput.value = '';
		fechaInput.style.border = "2px solid red";
		validate_date_disp = false;
		return;
	}
	else if (fechaSeleccionada < fechaActual){
		alert('La fecha ingresada debe ser mayor o igual a la fecha actual');
		fechaInput.value = '';
		fechaInput.style.border = "2px solid red";
		validate_date_disp = false;
		return;
	}
	fechaInput.style.border = "2px solid rgba(0,0,0,0.2)";
	validate_date_disp = true;
};
fechaInput.addEventListener('change', (event) => {validaFecha()});

function validationFiles(){
	const selectedFiles = fileInput.files;
	if (selectedFiles.length < 1) {
		alert('Debe seleccionar al menos 1 archivo');
		fileInput.style.border = "2px solid red";
		fileInput.value = '';
		validate_file = false;
		return;
	}
	if (selectedFiles.length > 3) {
		alert('Solo puede seleccionar hasta 3 archivos');
		fileInput.style.border = "2px solid red";
		fileInput.value = '';
		validate_file = false;
		return;
	}
	fileInput.style.border = "2px solid rgba(0,0,0,0.2)";
	validate_file = true;
	return;
}
fileInput.addEventListener('change', (event) => {validationFiles()});

function validateName(){
	const val = nameDonate;
	if (val.value.length < 3){	
		val.style.border = "2px solid red";
		validate_name = false; //a la vez lo validaremos
		alert("Nombre demasiado corto");
		val.value = '';
	}
	else if(val.value.length > 80){
		val.style.border = "2px solid red";
		validate_name = false; //a la vez lo validaremos
		alert("Nombre demasiado largo");
		val.value = '';
	}
	else{
		val.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_name = true; //Si lo dejan vacio esto no estara validado
	}
}
nameDonate.addEventListener('change', (event) => {validateName()});

function validateEmail(){
	const regexEmail = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
	const emailIngresado = emailInput.value

	if(!regexEmail.test(emailIngresado)){
		alert('Formato de email no valido');
		emailInput.value = '';
		emailInput.style.border = "2px solid red";
		validate_email = false;
	}
	else if (emailIngresado.length > 80){
		alert('Email demasiado largo');
		emailInput.style.border = "2px solid red";
		validate_email = false;
	}
	else {
		emailInput.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_email = true;
	}
}
emailInput.addEventListener('change', (event) => {validateEmail()});

function validateNumberCont(){
	const regexTelefono = /^\+569\d{8}$/;
	const numeroTelefono = number_phone.value;
	if (numeroTelefono == ''){
		number_phone.style.border = "2px solid red";
		validate_number = false;
	}
	else if (!regexTelefono.test(numeroTelefono)) {
		number_phone.value = '';
		alert('El número de teléfono ingresado no es válido');
		number_phone.style.border = "2px solid red";
		validate_number = false;
	}
	else if (numeroTelefono.length > 15){
		alert('El número de teléfono demasiado largo');
		number_phone.style.border = "2px solid red";
		validate_number = false;
	}
	else{
		number_phone.style.border = "2px solid rgba(0,0,0,0.2)";
		validate_number = true;
	}
}
number_phone.addEventListener('change', (event) => validateNumberCont())

function validateLenght(direc){
	if (direc.value.length >= 80){
		direc.value = ''
		direc.style.border = "2px solid red";
		alert('Demasiado largo')
		return false
	}
	else {
		direc.style.border = "2px solid rgba(0,0,0,0.2)";
		return true
	}
}
description.addEventListener("input",(event) => validateLenght(description))
condicionDeRetiro.addEventListener("input",(event) => validateLenght(condicionDeRetiro))

button.addEventListener('click',function(evento) {
	evento.preventDefault();
	let validate = true;

	if (!validate_reg){
		validateReg();
		validate=false;
	}
	if (!validate_com ){
		validateComuna();
		 validate=false;
	}
	if (!validate_calleNum){
		validateDirection();
		validate=false;
	}
	if (!validate_tipe){
		validateTypeDonation();
		validate=false;
	}
	if (!validate_cantidad){
		validateCantidad();
		validate=false;
	}
	if (!validate_date_disp){
		validaFecha();
		validate=false;
	}
	if (!validate_file){
		validationFiles();
		validate=false;
	}
	if (!validate_name){
		validateName();
		validate=false;
	}
	if (!validate_email){
		validateEmail();
		validate=false;
	}
	if (!validate_number){
		validateNumberCont();
		validate=false;
	}
	if (!validateLenght(description)){
		alert("Descripcion no valida");
		validate=false;
	}
	if (!validateLenght(condicionDeRetiro)){
		alert("Condicion no valida");
		validate=false;
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