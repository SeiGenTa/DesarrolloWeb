function initMap() {
    var map = L.map('map').setView([-40.4500000,-70.6666667], 4); // Coordenadas del centro del mapa (Nueva York, por ejemplo)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);


    
    $.ajax({
      url: "/get_donation_order_map",
      method: "GET",
      success: function(response) {
        console.log(response)
        var markers = L.markerClusterGroup({
          maxClusterRadius: 25, // Ajusta el valor según tus necesidades
      });
        response["donations"].forEach(element => {
          

          var marker = L.marker(
            [
              element[0]["lat"],
              element[0]["lng"]
            ],
            {icon: L.icon({
              iconUrl:'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',  // URL de la imagen del marcador
              iconSize: [25, 41],  // Tamaño del icono del marcador
              iconAnchor: [12, 41],  // Punto de anclaje del icono del marcador
              popupAnchor: [0, -41]  // Punto de anclaje del mensaje emergente del marcador
            })}
          );
          
          marker.on('click', function() {
            marker.unbindPopup();
            var text = "<h3>Donaciones</h3>";
            element["1"].forEach(donation => {
              text += "<h3> id: " + donation["id"] + " </h3>";
              text += "<p> calle: " + donation["calle"] + " </p>";
              text += "<p> cantidad: " + donation["cantidad"] + " </p>";
              text += "<p> tipo: " + donation["tipo"] + " </p>";
              text += "<p> fecha de disponibilidad: " + donation["fecha-disponible"] + " </p>";
            });
            marker.bindPopup(text).openPopup();
          });

          markers.addLayer(marker)
        });

        response["pedidos"].forEach(element =>{
          var marker = L.marker(
            [
              element[0]["lat"],
              element[0]["lng"]
            ],
            {icon: L.icon({
              iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',  // URL de la imagen del marcador
              iconSize: [25, 41],  // Tamaño del icono del marcador
              iconAnchor: [12, 41],  // Punto de anclaje del icono del marcador
              popupAnchor: [0, -41]  // Punto de anclaje del mensaje emergente del marcador
            })}
          );

          marker.on('click', function() {
            marker.unbindPopup();
            var text = "<h3>Pedidos</h3>";
            element["1"].forEach(donation => {
              text += "<h3> id: " + donation["id"] + " </h3>";
              text += "<p> Cantidad: " + donation["cantidad"] + " </p>";
              text += "<p> Email: " + donation["email"] + " </p>";
              text += "<p> tipo: " + donation["tipo"] + " </p>";
            });
            marker.bindPopup(text).openPopup();
          });
          markers.addLayer(marker);
          
        });
        map.addLayer(markers);
      },
      error: function(xhr, status, error) {
        // Ocurrió un error durante la solicitud
        console.log("Error: " + error);
      }
    });
    

}
document.addEventListener('DOMContentLoaded', initMap);

// Realizando una solicitud GET a Flask
