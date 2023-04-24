var ejemplo = [
    {"id": 1,"comuna": "Pichilemu", "tipo": "Verduras","descripcion":"Son muchas cositas", "cantidad": "10","nombre": "Simon Jara"},
    {"id": 2,"comuna": "Santiago", "tipo": "Otros","descripcion":"Comidas de todo tipo!", "cantidad": "10","nombre": "Almirante don"},
    {"id": 3,"comuna": "Rancagua", "tipo": "Frutas","descripcion":"Sandias en grandes cantidades", "cantidad": "10","nombre": "Juan tilla"},
    {"id": 4,"comuna": "Melipilla", "tipo": "Otros","descripcion":"Carne", "cantidad": "10","nombre": "Ricardo risas"},
    {"id": 5,"comuna": "Valparaiso", "tipo": "Otros","descripcion":"leche por favor", "cantidad": "10","nombre": "Soy sus"},
    {"id": 6,"comuna": "San Fernando", "tipo": "Otros","descripcion":"carne de aveztrus", "cantidad": "10","nombre": "ravia de dinosaurio"}
]

const idTable = document.getElementById("pedidosTab");

function main(){
    let filas = '<tr style="background-color: #015958;"><th>Comuna</th><th>Tipo</th><th>Descripcion</th><th>Cantidad</th><th>nombre solicitante</th></tr>';
    for (i = 0; i < ejemplo.length; i++){
        if (i % 2 == 0) filas += "<tr onclick='selectTab("+ejemplo[i].id+")' style='background-color: #8FC1B5;'><th>"+ejemplo[i].comuna+"</th><th>"+ejemplo[i].tipo+"</th><th>"+ejemplo[i].descripcion+"</th><th>"+ejemplo[i].cantidad+"</th><th>"+ejemplo[i].nombre+"</th></tr>";
        else filas += "<tr onclick='selectTab("+ejemplo[i].id+")' style='background-color: #589A8D;'><th>"+ejemplo[i].comuna+"</th><th>"+ejemplo[i].tipo+"</th><th>"+ejemplo[i].descripcion+"</th><th>"+ejemplo[i].cantidad+"</th><th>"+ejemplo[i].nombre+"</th></tr>";
    }
    idTable.innerHTML = filas;
}

main();

function selectTab(i){
    window.location.href = '../html/informacion-pedidos.html';
}