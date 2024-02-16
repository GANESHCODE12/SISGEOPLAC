var tblProgramacion;

$(function () {
    tblProgramacion = $('#data').DataTable({
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
            { "data": "id" },
            { "data": "nombre" },
            { "data": "fecha_programacion" },
            { "data": "turno" },
            { "data": "maquina" },
            { "data": "cumplimiento" },
            { "data": "motivo_incumplimiento" },
            { "data": "turno_reprogramacion" },
        ],
        columnDefs: [
            {
                targets: [1, 2, 4, 3, 4, 5, 6, 7],
                class: 'col-2',
            },
            {
                targets: [5],
                class: 'text-center',
                render: function (data, type, row) {
                    return row.cumplimiento === true ? 'Si' : 'No'
                } 
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});