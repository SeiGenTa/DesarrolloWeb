const start = Date.now()
const log = (v) => console.log(`${v} \n Tiempo transcurrido: ${Date.now() - start} ms`)

// const funcionLenta = () => {
//   let i = 0
//   while (i < 1000000000) { i++ }
//   return 'Funcion lenta termino'
// }

// log('Paso 1')
// log(funcionLenta())
// log('Paso 2')

const funcionLentaAsync = () => {
  return Promise.resolve().then(() => {
    let i = 0
    while (i < 1000000000) { i++ }
    return 'Funcion lenta termino'
  })
}

log('Paso 1')
funcionLentaAsync().then(log)
log('Paso 2')
