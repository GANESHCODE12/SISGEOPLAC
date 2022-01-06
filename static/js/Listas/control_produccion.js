var tblControl;

$(function () {
    tblControl = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
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
            {"data": "numero_op"},
            {"data": "supervisor"},
            {"data": "tecnico"},
            {"data": "operario"},
            {"data": "turno"},
            {"data": "producto"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_produccion/Detalle_control/' + row.id + '/" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
