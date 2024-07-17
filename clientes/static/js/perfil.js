document.addEventListener('DOMContentLoaded', function () {
    const tipoClienteSelect = document.querySelector('select[name="id_tipo_cliente"]');
    const naturalFields = document.getElementById('natural-fields');
    const empresaFields = document.getElementById('empresa-fields');

    tipoClienteSelect.addEventListener('change', function () {
        const selectedValue = tipoClienteSelect.value;
        toggleFormFields(selectedValue);
    });

    function toggleFormFields(tipo) {
        if (tipo === '1') {  // Valor correspondiente a "Natural"
            naturalFields.style.display = 'block';
            empresaFields.style.display = 'none';
        } else if (tipo === '2') {  // Valor correspondiente a "Empresa"
            naturalFields.style.display = 'none';
            empresaFields.style.display = 'block';
        }
    }

    // Inicializar con el estado basado en el valor actual de id_tipo_cliente
    toggleFormFields(tipoClienteSelect.value);
});
