var tblCertificados;

$(function () {
    tblCertificados = $('#data').DataTable({
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
            {"data": "fecha_despacho"},
            {"data": "producto"},
            {"data": "color"},
            {"data": "cliente_despacho"},
            {"data": "numero_op"},
            {"data": "lote"},
            {"data": "cantidad_orden"},
            {"data": "cantidad_solicitada"},
            {"data": "saldo"},
            {"data": "opciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_calidad/Detalle_inspeccion/' + row.id + '"><button title="Detalle Inspección" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    buttons += '<a href="/Control_calidad/crear-certificado-calidad/' + row.id + '"><button title="Crear certificado de calidad" class="btn btn-success btn-xs btn-flat"><i class="fas fa-folder-open"></i></button></a> ';
                    buttons += '<a href="/Producto_no_conforme/Nuevo_producto_no_conforme/' + row.id + '"><button title="Crear PNC" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-times-circle"></i></button></a> ';
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
                targets: [7, 8, 9],
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

table.destroy();