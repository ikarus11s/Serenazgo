document.addEventListener('DOMContentLoaded', function() {
    // Cargar opciones para los selectores
    cargarOpciones('tipo', getTiposEmergencia());
    document.getElementById('tipo').addEventListener('change', actualizarSubtipos);
    document.getElementById('subtipo').addEventListener('change', actualizarModalidades);

    // Manejar cambio en la selección de ubicación
    document.querySelectorAll('input[name="ubicacion"]').forEach(function(radio) {
        radio.addEventListener('change', manejarCambioUbicacion);
    });

    // Manejar envío del formulario
    document.getElementById('emergencyForm').addEventListener('submit', enviarAlerta);
});

function cargarOpciones(selectId, opciones) {
    const select = document.getElementById(selectId);
    select.innerHTML = '';
    opciones.forEach(function(opcion) {
        const option = document.createElement('option');
        option.value = opcion;
        option.textContent = opcion;
        select.appendChild(option);
    });
}

function actualizarSubtipos() {
    const tipo = document.getElementById('tipo').value;
    cargarOpciones('subtipo', getSubtiposEmergencia(tipo));
    actualizarModalidades();
}

function actualizarModalidades() {
    const subtipo = document.getElementById('subtipo').value;
    cargarOpciones('modalidad', getModalidades(subtipo));
}

function manejarCambioUbicacion(event) {
    const mapContainer = document.getElementById('mapContainer');
    if (event.target.value === 'paraOtra') {
        mapContainer.style.display = 'block';
        // Aquí se debería inicializar el mapa
        inicializarMapa();
    } else {
        mapContainer.style.display = 'none';
    }
}

function inicializarMapa() {
    // Implementar la inicialización del mapa aquí
    // Por ejemplo, usando la API de Google Maps
}

function enviarAlerta(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    
    // Añadir coordenadas
    if (data.ubicacion === 'paraMi') {
        // Obtener ubicación actual
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                data.latitud = position.coords.latitude;
                data.longitud = position.coords.longitude;
                enviarDatosAlServidor(data);
            }, function(error) {
                console.error('Error al obtener la ubicación:', error);
                alert('No se pudo obtener su ubicación. Por favor, intente de nuevo.');
            });
        } else {
            alert('Su navegador no soporta geolocalización.');
        }
    } else {
        // Obtener coordenadas del mapa
        const coordenadas = obtenerCoordenadasDelMapa();
        data.latitud = coordenadas.lat;
        data.longitud = coordenadas.lng;
        enviarDatosAlServidor(data);
    }
}

function enviarDatosAlServidor(data) {
    // Aquí se enviarían los datos al servidor (Google Apps Script)
    google.script.run
        .withSuccessHandler(function(result) {
            alert('Alerta enviada con éxito');
            document.getElementById('emergencyForm').reset();
        })
        .withFailureHandler(function(error) {
            console.error('Error al enviar la alerta:', error);
            alert('Hubo un error al enviar la alerta. Por favor, intente de nuevo.');
        })
        .registrarAlerta(data);
}

function getTiposEmergencia() {
    // Esta función debería obtener los tipos de emergencia del servidor
    return ['Robo', 'Accidente', 'Incendio', 'Violencia doméstica'];
}

function getSubtiposEmergencia(tipo) {
    // Esta función debería obtener los subtipos de emergencia del servidor basados en el tipo seleccionado
    const subtipos = {
        'Robo': ['Robo a mano armada', 'Robo de vehículo', 'Robo a vivienda'],
        'Accidente': ['Accidente de tránsito', 'Accidente laboral', 'Caída'],
        'Incendio': ['Incendio estructural', 'Incendio forestal', 'Incendio vehicular'],
        'Violencia doméstica': ['Violencia física', 'Violencia psicológica', 'Violencia económica']
    };
    return subtipos[tipo] || [];
}

function getModalidades(subtipo) {
    // Esta función debería obtener las modalidades del servidor basadas en el subtipo seleccionado
    const modalidades = {
        'Robo a mano armada': ['Con arma de fuego', 'Con arma blanca'],
        'Robo de vehículo': ['Auto', 'Moto', 'Bicicleta'],
        'Accidente de tránsito': ['Choque', 'Atropello', 'Volcadura'],
        'Incendio estructural': ['Vivienda', 'Comercio', 'Industria'],
        // ... más modalidades para otros subtipos
    };
    return modalidades[subtipo] || [];
}

function obtenerCoordenadasDelMapa() {
    // Esta función debería obtener las coordenadas seleccionadas en el mapa
    // Por ahora, retornamos coordenadas de ejemplo
    return { lat: -12.0789, lng: -77.0842 };
}