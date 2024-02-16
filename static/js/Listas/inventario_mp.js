var tblInventarioMp;

$(function () {
    tblInventarioMp = $('#data').DataTable({
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
            { "data": "id" },
            { "data": "nombre" },
            { "data": "referencia" },
            { "data": "categoria" },
            { "data": "proveedor" },
            { "data": "cantidad" },
            { "data": "pnc" },
            { "data": "cantidad_real" },
            { "data": "Unidad_Meidida" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a rel="details"><button title="Ingresos" class="btn btn-success btn-xs btn-flat"><i class="fas fa-dolly"></i></button></a> ';
                    buttons += '<a rel="details_outputs"><button title="Requisiciones" class="btn btn-info btn-xs btn-flat"><i class="fas fa-dolly-flatbed"></i></button></a>';
                    return buttons;
                }
            },
            {
                targets: [0, 2, 3, 4, 5, 6],
                class: 'text-center',
                orderable: false,
            },
            {
                targets: [5, -3],
                class: 'text-center',
                render: function (data, type, row) {
                    return parseFloat(data).toFixed(2);
                }
            }
        ],
        initComplete: function (settings, json) {

        },
    });

    $('#data tbody')
        .on('click', 'a[rel=details]', function () {
            var tr = tblInventarioMp.cell($(this).closest('td, li')).index();
            var data = tblInventarioMp.row(tr.row).data();

            $('#tblDet').DataTable({
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
                        'action': 'search_details_entries',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "nombre" },
                    { "data": "referencia" },
                    { "data": "ingreso" },
                    { "data": "cantidad_ingresada" },
                    { "data": "persona" },
                    { "data": "factura" },
                    { "data": "remision" },
                    { "data": "lote" },
                    { "data": "observaciones_ingreso_materia_prima" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3, 4, 5, 6, 7],
                        class: 'text-center',
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        });

    $('#data tbody')
        .on('click', 'a[rel=details_outputs]', function () {
            var tr = tblInventarioMp.cell($(this).closest('td, li')).index();
            var data = tblInventarioMp.row(tr.row).data();

            $('#tblDetOutputs').DataTable({
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
                        'action': 'search_details_outputs',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "nombre" },
                    { "data": "referencia" },
                    { "data": "solicitud" },
                    { "data": "solicitada" },
                    { "data": "persona" },
                    { "data": "numero_orden" },
                    { "data": "observaciones_solicitud" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3, 4, 5, 6, 7],
                        class: 'text-center',
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetOutputs').modal('show');
        });
});