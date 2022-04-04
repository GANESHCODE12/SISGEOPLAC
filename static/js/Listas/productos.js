var tblProductos;

$(function () {
    tblProductos = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        order: [0, 'desc'],
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
            {"data": "Nombre_producto"},
            {"data": "cliente_especifico"},
            {"data": "numero_ficha"},
            {"data": "proceso"},
            {"data": "version"},
            {"data": "fecha_vigencia"},
            {"data": "estado_ficha"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="actualizar_producto/' + row.id + '" class="btn btn-info btn-xs btn-flat"><i class="fas fa-image"></i></a> ';
                    buttons += '<a href="ficha_' + row.id + '" type="button" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    buttons += '<a href="/produccion/nueva_orden/' + row.id + '" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-paste"></i></a> ';
                    buttons += '<a href="actualizar_ficha/' + row.id + '" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-highlighter"></i></a>';
                    return buttons;
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
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