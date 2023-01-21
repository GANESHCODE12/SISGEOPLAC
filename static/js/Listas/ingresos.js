var tblIngresos;

$(function () {
    tblIngresos = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        order: [0, 'desc'],
        pageLength: 25,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "material"},
            {"data": "categoria"},
            {"data": "fecha_ingreso"},
            {"data": "cantidad_ingresada"},
            {"data": "opciones"},
            {"data": "existe"},
            {"data": "inspeccion"},
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_calidad/crear-inspeccion-mp/' + row.id + '"><button title="Realizar inspección" class="btn btn-success btn-xs btn-flat"><i class="fas fa-plus"></i></button></a> ';
                    if (row.existe === 1) {
                        buttons += '<a href="/Control_calidad/detalle-inspeccion-mp/' + row.inspeccion + '"><button title="Detalle inspección mp" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    }
                    return buttons;
                }
            },
            {
                targets: [-1, -2],
                visible: false
            },
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [3],
                class: 'text-center',
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});