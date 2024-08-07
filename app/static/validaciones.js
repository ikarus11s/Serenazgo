function validarFormulario() {
    const dni = document.getElementById('dni').value;
    const celular = document.getElementById('celular').value;

    if (!validarDNI(dni)) {
        alert('El DNI debe tener 8 dígitos numéricos.');
        return false;
    }

    if (!validarCelular(celular)) {
        alert('El número de celular debe tener 9 dígitos numéricos.');
        return false;
    }

    return true;
}

function validarDNI(dni) {
    const regex = /^[0-9]{8}$/;
    return regex.test(dni);
}

function validarCelular(celular) {
    const regex = /^[0-9]{9}$/;
    return regex.test(celular);
}

document.getElementById('emergencyForm').addEventListener('submit', function(event) {
    if (!validarFormulario()) {
        event.preventDefault();
    }
});