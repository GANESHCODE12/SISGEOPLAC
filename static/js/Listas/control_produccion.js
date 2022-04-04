var tblControl;

$(function () {
    tblControl = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        order: [1, 'desc'],
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
            {"data": "id"},
            {"data": "numero_op"},
            {"data": "cantidad_producida"},
            {"data": "saldo_orden"},
            {"data": "fecha_creacion"},
            {"data": "turno"},
            {"data": "producto"},
            {"data": "supervisor"},
            {"data": "tecnico"},
            {"data": "operario"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_produccion/Detalle_control/' + row.id + '/" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    buttons += '<a href="/Control_produccion/Crear_nuevo_control/' + row.numero_op + '/" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-plus"></i></a>';
                    return buttons;
                }
            },
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                searchable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [0, 1, 3, 4, 6, 7, 8],
                searchable: false,
                orderable: false,
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
                targets: [3],
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
