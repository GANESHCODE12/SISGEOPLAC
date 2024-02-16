var tblInventarioLote;

$(function () {
    tblInventarioLote = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        pageLength: 25,
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
            { "data": "numero_op" },
            { "data": "lote" },
            { "data": "nombre" },
            { "data": "color" },
            { "data": "codigo" },
            { "data": "cantidad" },
            { "data": "cajas" },
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3, 4, 5, 6],
                class: 'text-center',
                orderable: false,
            },
            {
                targets: [-1, -2],
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            }
        ],
        initComplete: function (settings, json) {

        },
    });
});