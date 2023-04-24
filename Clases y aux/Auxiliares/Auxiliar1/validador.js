const validadorMail = (mail) => mail && mail.includes('@') // funcion forma de flecha

const validadorNombreApellido = (nombre) => {
  let valido = false // definicion de variables
  if (nombre && nombre.length > 4) {
    valido = true
  }
  return valido
}

function tieneNumeros(str) { // funcion forma antigua
  return /\d/.test(str)
}

const validadorContrasena = (pswd) => {
  // arreglos
  const malas = [
    '1234',
    'admin1',
    'odio a mis Aux >:(2'
  ]

  // tambien existen diccionarios o JSON
  let dict = {
    a: 1,
    b: "Hola",
    c: (el) => console.log(el)
  }

  return tieneNumeros(pswd) && !malas.includes(pswd)
}

const validarForm = () => {
  console.log('Enviando...') // imprimir en consola

  // obtener elementos del DOM por el ID
  let emailInput = document.getElementById('email')
  let nombreInput = document.getElementById('nombre')
  let apellidoInput = document.getElementById('apellido')
  let pswdInput = document.getElementById('contrasenna')
  
  
  let msg = ''
  
  if (!validadorMail(emailInput.value)) {
    msg += 'Mail malo!\n'
    emailInput.style.borderColor = 'red' // cambiar estilo con JS!!
  } else {
    emailInput.style.borderColor = ''
  }
  
  if (!validadorNombreApellido(nombreInput.value)) {
    msg += 'Nombre malo!\n'
    nombreInput.style.borderColor = 'red'
  } else {
    nombreInput.style.borderColor = ''
  }
  
  if (!validadorNombreApellido(apellidoInput.value)) {
    msg += 'Apellido malo!\n'
    apellidoInput.style.borderColor = 'red'
  } else {
    apellidoInput.style.borderColor = ''
  }
  
  if (!validadorContrasena(pswdInput.value)) {
    msg += 'Contraseña mala!\n'
    pswdInput.style.borderColor = 'red'
  } else {
    pswdInput.style.borderColor = ''
  }
  
  if (msg === '') {
    msg = 'Felicidades ya tienes una cuenta!'
  }
  alert(msg) // alertas JS
}