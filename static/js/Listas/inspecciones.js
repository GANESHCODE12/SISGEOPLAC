var tblInspecciones;

$(function () {
    tblInspecciones = $('#data').DataTable({
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
            {"data": "id"},
            {"data": "fecha_creacion"},
            {"data": "turno"},
            {"data": "maquina"},
            {"data": "numero_op"},
            {"data": "lote"},
            {"data": "inspector"},
            {"data": "producto"},
            {"data": "cliente"},
            {"data": "saldo"},
            {"data": "opciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_calidad/Actualizar_certificado/' + row.id + '" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/Control_calidad/Detalle_inspeccion/' + row.id + '" type="button" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    buttons += '<a href="/Control_calidad/Certificado_calidad/' + row.id + '" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                    buttons += '<a href="/Producto_no_conforme/Nuevo_producto_no_conforme/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-times-circle"></i></a>';
                    return buttons;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [0, 2, 3, -2],
                class: 'text-center',
            },
            {
                targets: [0, 1, 2, 4, 5, 6, 7, 8],
                searchable: false,
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});

table.destroy();