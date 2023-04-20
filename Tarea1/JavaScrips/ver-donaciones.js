var ejemplo = [
    {"comuna": "Pichilemu", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Simon Jara", "fotos": ["photo_0.jpg"]},
    {"comuna": "Santiago", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Andres garradas", "fotos": ["photo_0.jpg"]},
    {"comuna": "San Fernando", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Aguerras cerda", "fotos": ["photo_0.jpg"]},
    {"comuna": "Rancagua", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Ricardo malon", "fotos": ["photo_0.jpg"]},
    {"comuna": "Buin", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Gran tiburon", "fotos": ["photo_0.jpg"]},
    {"comuna": "Talca", "tipo": "verduras", "cantidad": "10", "fecha":"2023-04-05", "nombre": "Manuel antonio", "fotos": ["photo_0.jpg"]}
]

const idTable = document.getElementById("OrdenPedidos");

function main(){
    let filas = '<tr style="background-color: #015958;"><th>Comuna</th><th>Tipo</th><th>Cantidad</th><th>fecha</th><th>nombre</th><th>foto</th></tr>';
    for (i = 0; i < ejemplo.length; i++){
        if (i % 2 == 0) filas += "<tr onclick='selectTab("+ejemplo[i].id+")' style='background-color: #8FC1B5;'><th>"+ejemplo[i].comuna+"</th><th>"+ejemplo[i].tipo+"</th><th>"+ejemplo[i].cantidad+"</th><th>"+ejemplo[i].fecha+"</th><th>"+ejemplo[i].nombre+"</th><th><img class='photo' src = '../photos/"+(ejemplo[i].fotos)[0]+"'></tr>";
        else filas += "<tr onclick='selectTab("+ejemplo[i].id+")' style='background-color: #589A8D;'><th>"+ejemplo[i].comuna+"</th><th>"+ejemplo[i].tipo+"</th><th>"+ejemplo[i].cantidad+"</th><th>"+ejemplo[i].fecha+"</th><th>"+ejemplo[i].nombre+"</th><th><img class='photo' src = '../photos/"+(ejemplo[i].fotos)[0]+"'></tr>";
    }
    idTable.innerHTML = filas;
}

main();

function selectTab(){
    window.location.href = '../html/informacion-donaciones.html';
}