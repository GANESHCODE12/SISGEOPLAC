var tblUsuarios;

$(function () {
    tblUsuarios = $('#data').DataTable({
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
            {"data": "full_name"},
            {"data": "username"},
            {"data": "date_joined"},
            {"data": "groups"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/users/actualizar_usuario/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/users/eliminar_usuario/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash"></i></a> ';
                    return buttons;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.groups, function (key, value) {
                        html += '<span class="badge badge-success">'+value.name+'</span> ';
                    });
                    return html;
                },
            },
            {
                targets: [-3],
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
