var tblDocumentos;

$(function () {
    tblDocumentos = $('#data').DataTable({
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
            {"data": "codigo"},
            {"data": "titulo"},
            {"data": "tipo_documento"},
            {"data": "proceso"},
            {"data": "versión"},
            {"data": "fecha"},
            {"data": "estado_documento"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Documentación/actualizar_documento/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/Documentación/detalle_documento/' + row.id + '/" type="button" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
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