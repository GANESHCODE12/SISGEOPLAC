var tblTecnicosOperarios;

$(function () {
    tblTecnicosOperarios = $('#data').DataTable({
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
            {"data": "nombre"},
            {"data": "cargo"},
            {"data": "codigo"},
        ],
        columnDefs: [
            {
                targets: [0, 1, 2, 3],
                class: 'text-center',
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});