document.addEventListener('DOMContentLoaded', function() {
    cargarDNIsSerenos();
    document.getElementById('dniSereno').addEventListener('change', cargarEstadoSereno);
    document.getElementById('numeroParte').addEventListener('change', cargarInfoIncidente);
    document.getElementById('serenoForm').addEventListener('submit', actualizarEstado);
});

function cargarDNIsSerenos() {
    // Aquí se haría una llamada al servidor para obtener la lista de DNIs
    const dnis = ['12345678', '87654321', '11223344']; // Ejemplo
    const select = document.getElementById('dniSereno');
    dnis.forEach(dni => {
        const option = document.createElement('option');
        option.value = dni;
        option.textContent = dni;
        select.appendChild(option);
    });
}

function cargarEstadoSereno() {
    const dni = document.getElementById('dniSereno').value;
    // Aquí se haría una llamada al servidor para obtener el estado del sereno
    const estado = 'Normal'; // Ejemplo
    document.getElementById('estadoSereno').textContent = `Estado actual: ${estado}`;
    cargarNumerosParte(dni);
}

function cargarNumerosParte(dni) {
    // Aquí se haría una llamada al servidor para obtener los números de parte asociados al sereno
    const numeros = ['PO-0000001', 'PO-0000002', 'PO-0000003']; // Ejemplo
    const select = document.getElementById('numeroParte');
    select.innerHTML = '';
    numeros.forEach(numero => {
        const option = document.createElement('option');
        option.value = numero;
        option.textContent = numero;
        select.appendChild(option);
    });
}

function cargarInfoIncidente() {
    const numeroParte = document.getElementById('numeroParte').value;
    // Aquí se haría una llamada al servidor para obtener la información del incidente
    const info = {
        tipo: 'Robo',
        ubicacion: 'Av. Principal 123',
        estado: 'En proceso'
    }; // Ejemplo
    const infoDiv = document.getElementById('incidenteInfo');
    infoDiv.innerHTML = `
        <p><strong>Tipo:</strong> ${info.tipo}</p>
        <p><strong>Ubicación:</strong> ${info.ubicacion}</p>
        <p><strong>Estado:</strong> ${info.estado}</p>
    `;
}

function actualizarEstado(event) {
    event.preventDefault();
    const dni = document.getElementById('dniSereno').value;
    const numeroParte = document.getElementById('numeroParte').value;
    const nuevoEstado = document.getElementById('nuevoEstado').value;
    // Aquí se haría una llamada al servidor para actualizar el estado
    console.log(`Actualizando estado para DNI ${dni}, Parte ${numeroParte} a ${nuevoEstado}`);
    // Después de la actualización exitosa, se podría mostrar un mensaje de confirmación
    alert('Estado actualizado con éxito');
}