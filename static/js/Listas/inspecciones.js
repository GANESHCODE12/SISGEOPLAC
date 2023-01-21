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
            {"data": "opciones"},
            {"data": "pnc"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_calidad/Detalle_inspeccion/' + row.id + '"><button title="Detalle Inspección" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    buttons += '<a href="/Control_calidad/crear-certificado-calidad/' + row.id + '"><button title="Crear certificado de calidad" class="btn btn-success btn-xs btn-flat"><i class="fas fa-folder-open"></i></button></a> ';
                    buttons += '<a href="/Producto_no_conforme/Nuevo_producto_no_conforme/' + row.id + '"><button title="Crear PNC" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-times-circle"></i></button></a> ';
                    if(row.pnc > 0){
                        buttons += '<a href="/Producto_no_conforme/actualizar_pnc/' + row.id + '/"><button title="Actualizar PNC" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i> <i class="fas fa-times-circle"></i></button></a> ';
                        buttons += '<a rel="details_pnc"><button title="Trazabilidad PNC" class="btn btn-info btn-xs btn-flat"><i class="fas fa-paste"></i></button></a> ';
                    }
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
                targets: [0, 2, 3, -3],
                class: 'text-center',
            },
            {
                targets: [-1],
                visible: false,
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#data tbody')
        .on('click', 'a[rel=details_pnc]', function () {
            var tr = tblInspecciones.cell($(this).closest('td, li')).index();
            var data = tblInspecciones.row(tr.row).data();

            $('#tblDetPnc').DataTable({
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
                        'action': 'search_details_pnc',
                        'id_inspeccion': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "id"},
                    {"data": "fecha_creacion"},
                    {"data": "numero_op"},
                    {"data": "id_inspeccion"},
                    {"data": "estado_pnc"},
                    {"data": "cantidad_pnc"},
                    {"data": "tipo_pnc"},
                    {"data": "observaciones"},
                ],
                columnDefs: [
                    {
                        targets: [1],
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

            $('#myModalDetPnc').modal('show');
        });
});