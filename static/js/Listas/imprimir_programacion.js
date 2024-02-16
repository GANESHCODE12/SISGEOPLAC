var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');
var tblImprimirProgramacion;

function generate_report() {
    var busqueda = {
        'action': 'searchdata',
        'start_date': date_now,
        'end_date': date_now,
    };

    if (date_range !== null) {
        busqueda['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        busqueda['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }

    var programacion = {
        items: {
            programacion_colaborador: [],
        },
        programacion_colaborador: function () {
            tblImprimirProgramacion = $('#tblImprimirProgramacion').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 200,
                paging: false,
                searching: false,
                dom: 'Bfrtip',
                buttons: [
                    {
                        extend: 'excelHtml5',
                        text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                        titleAttr: 'Excel',
                        className: 'btn btn-success btn-flat btn-xs'
                    },
                    {
                        extend: 'pdfHtml5',
                        text: 'Descargar Pdf <i class="fas fa-file-pdf"></i>',
                        titleAttr: 'PDF',
                        className: 'btn btn-danger btn-flat btn-xs',
                        download: 'open',
                        orientation: 'landscape',
                        pageSize: 'LEGAL',
                    }
                ],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: busqueda,
                    dataSrc: ""
                },
                data: this.items.programacion_colaborador,
                columns: [
                    { "data": "nombre" },
                    { "data": "fecha_programacion" },
                    { "data": "turno" },
                    { "data": "maquina" },
                ],
                columnDefs: [

                ],
                rowCallback(row, data, displayNum, displayIndex, dataIndex) {
    
                },
                initComplete: function (settings, json) {
                    
                }
            });
        },
    };
    programacion.programacion_colaborador();
}

generate_report()

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
});
