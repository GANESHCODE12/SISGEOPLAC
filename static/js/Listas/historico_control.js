var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');
var tblHistoricoControl;

function generate_report() {
    var parameters = {
        'action': 'search_report',
        'start_date': date_now,
        'end_date': date_now,
    };

    if (date_range !== null) {
        parameters['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        parameters['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }

    tblHistoricoControl = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "id"},
            {"data": "numero_op"},
            {"data": "cantidad_producida"},
            {"data": "saldo_orden"},
            {"data": "hora_inicio"},
            {"data": "turno"},
            {"data": "producto"},
            {"data": "maquina"},
            {"data": "colaboradores"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                render: function (data, type, row) {
                    var buttons = '<a href="/Control_produccion/Detalle_control/' + row.id + '/"><button title="Detalle" class="btn btn-info btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                    return buttons;
                }
            },
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                searchable: false,
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [0, 1, 3, 4, 6, 7, 8],
                searchable: false,
                orderable: false,
            },
            {
                targets: [4],
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            },
            {
                targets: [3],
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.colaboradores, function (key, value) {
                        html += '<span class="badge badge-primary">'+value.nombre+'</span> ';
                    });
                    return html;
                },
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {
    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'YYYY-MM-DD',
            applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
            cancelLabel: '<i class="fas fa-times"></i> Cancelar',
        }
    }).on('apply.daterangepicker', function (ev, picker) {
        date_range = picker;
        generate_report();
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range = picker;
        generate_report();
    });

    generate_report();
});
