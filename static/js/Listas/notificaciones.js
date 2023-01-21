var tblNotificaciones;

$(function () {
    tblNotificaciones = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        pageLength: 50,
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
                "className": 'details-notify',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "id"},
            {"data": "actor"},
            {"data": "destinatario"},
            {"data": "timestamp"},
            {"data": "motivo"},
            {"data": "verbo"},
            {"data": "read"},
            {"data": "produccion"},
        ],
        columnDefs: [
            {
                targets: [4],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [0, 1, 2, 3, 4, 6],
                searchable: false,
            },
        ],
        initComplete: function (settings, json) {

        }
    })
});