var tblTecnicosOperarios;

$(function () {
    tblTecnicosOperarios = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        retrieve: true,
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
        initComplete: function (settings, json) {

        }
    });
});