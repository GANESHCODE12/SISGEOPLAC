var tblProductos;

function format(d) {
    console.log(d);
    var html = '<table class="table table-bordered">';
    html += '<thead class="thead-dark">';
    html += '<th scope="col">Color</th>';
    html += '<th scope="col">Acciones</th>';
    html += '</thead>';
    html += '<tbody>';
    $.each(d.color, function (key, value) {
        html+='<tr>'
        html+='<td>'+value.color.color+'</td>'
        html+='<td style="text-align: center;">'+'<a href="/produccion/nueva_orden/' + value.id + '"><button class="btn btn-success btn-xs btn-flat">Nueva Orden de Producción</button></a>'+'</td>'
        html+='</tr>';
    });
    html += '</tbody>';
    return html;
}

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
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
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
                    var buttons = '<a href="actualizar_ficha/' + row.id + '"><button title="Actualizar Producto" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-highlighter"></i></button></a> ';
                    buttons += '<a href="ficha_' + row.id + '"><button title="Ficha Técnica" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    buttons += '<a href="actualizar_diagrama/' + row.id + '"><button title="Actualizar Diagrama" class="btn btn-dark btn-xs btn-flat"><i class="fas fa-image"></i></button></a>';
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
    })
    .on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = tblProductos.row(tr);
        if (row.child.isShown()) {
            row.child.hide();
            tr.removeClass('shown');
        } else {
            row.child(format(row.data())).show();
            tr.addClass('shown');
        }
    });
});