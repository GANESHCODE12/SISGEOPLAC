var tblStock;

$(function () {
    tblStock = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        rowGroup: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: "",
        },
        columns: [
            {"data": "Nombre_producto"},
            {"data": "cliente"},
            {"data": "color"},
            {"data": "cantidad_requerida"},
            // {"data": ""},
            // {"data": ""},
            // {"data": ""},
            // {"data": ""},
        ],
        rowsGroup: [0, 1, 2],
        columnDefs: [
    
        ],
        initComplete: function (settings, json) {

        }
    });
});
