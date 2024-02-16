var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');
var tblReporteRendimiento;

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

  tblReporteRendimiento = $('#data').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
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
      data: parameters,
      dataSrc: ""
    },
    columns: [
      { "data": "control" },
      { "data": "numero_op" },
      { "data": "producto" },
      { "data": "maquina" },
      { "data": "colaborador" },
      { "data": "turno" },
      { "data": "cargo" },
      { "data": "cantidad_producida" },
      { "data": "cantidad_esperada" },
      { "data": "rendimiento" },
      { "data": "hora_inicio" },
    ],
    columnDefs: [
      {
        targets: [0, 1, -2, -3, -4, 5],
        class: 'text-center'
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