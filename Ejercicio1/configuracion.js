let valAct = document.getElementById("contador")
const buttonSuma = document.getElementById("btn-suma")
const buttonRest = document.getElementById("btn-resta")

let n = 0 // contado
const suma = () => {
    n += 1
    valAct.innerHTML = n;
}
const resta = () => {
    n += -1
    valAct.innerHTML = n
};

buttonRest.onclick = function (){
    resta()
}
buttonSuma.onclick = function (){
    suma()
}