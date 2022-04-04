var tblProduccion;

$(function () {
    tblProduccion = $('#data').DataTable({
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
            {"data": "numero_op"},
            {"data": "Nombre_producto"},
            {"data": "lote"},
            {"data": "cliente"},
            {"data": "cantidad_requerida"},
            {"data": "estado_op"},
            {"data": "fecha_entrega"},
            {"data": "numero_op"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="actualizar_orden/' + row.numero_op + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="detalle_orden/' + row.numero_op + '/" type="button" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    buttons += '<a href="/Control_produccion/Crear_nuevo_control/' + row.numero_op + '/" type="button" class="btn btn-info btn-xs btn-flat"><i class="fas fa-gamepad"></i></a> ';
                    buttons += '<a href="/Control_calidad/Crear_inspeccion/' + row.numero_op + '" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-vials"></i></a> ';
                    return buttons;
                }
            },
            {
                targets: [4],
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
