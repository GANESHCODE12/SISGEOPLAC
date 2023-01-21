var tblPnc;

$(function () {
    tblPnc = $('#data').DataTable({
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
            {"data": "producto"},
            {"data": "color"},
            {"data": "tipo_pnc"},
            {"data": "fecha_creacion"},
            {"data": "numero_op"},
            {"data": "id_inspeccion"},
            {"data": "estado_pnc"},
            {"data": "cantidad_pnc"},
            {"data": "colaboradores"},
            {"data": "opciones"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Producto_no_conforme/Detalle_PNC/' + row.id + '"><button title="Detalle PNC" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    return buttons;
                }
            },
            {
                targets: [3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.colaboradores, function (key, value) {
                        html += '<span class="badge badge-success">'+value.nombre+'</span> ';
                    });
                    return html;
                },
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
