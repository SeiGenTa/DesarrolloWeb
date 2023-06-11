let map = L.map("map").setView([-33.457925, -70.664511], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

fetch("http://localhost:8007/get-map-data")
  .then((response) => response.json())
  .then((parsedData) => {
    for (let conf of parsedData) {
      let lat = conf["conf_lat"];
      let lng = conf["conf_long"];

      const onMarkerClick = (e) => {
        L.popup()
          .setLatLng([lat, lng])
          .setContent(
            `<h1>${conf["conf_title"]}:</h1><i>${conf["conf_text"]}</i><br>-${conf["username"]}`
          )
          .openOn(map);
      };

      let marker = L.marker([lat, lng]).addTo(map);
      marker.on("click", onMarkerClick);
    }
  });
