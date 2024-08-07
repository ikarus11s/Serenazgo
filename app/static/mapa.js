let map;
let marker;

function initMap() {
    const puebloLibre = { lat: -12.0789, lng: -77.0842 };
    map = new google.maps.Map(document.getElementById("mapContainer"), {
        zoom: 14,
        center: puebloLibre,
    });

    marker = new google.maps.Marker({
        position: puebloLibre,
        map: map,
        draggable: true
    });

    google.maps.event.addListener(marker, 'dragend', function(event) {
        document.getElementById("latitud").value = event.latLng.lat();
        document.getElementById("longitud").value = event.latLng.lng();
    });

    map.addListener("click", (event) => {
        marker.setPosition(event.latLng);
        document.getElementById("latitud").value = event.latLng.lat();
        document.getElementById("longitud").value = event.latLng.lng();
    });
}

function obtenerCoordenadasDelMapa() {
    return {
        lat: marker.getPosition().lat(),
        lng: marker.getPosition().lng()
    };
}