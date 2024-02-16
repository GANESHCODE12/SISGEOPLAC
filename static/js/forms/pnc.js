var tblPnc;

var pnc = {
  items: {
    pnc_post: [],
  },
  get_ids: function () {
    var ids = [];
    $.each(this.items.pnc_post, function (key, value) {
      ids.push(value.id);
    });
    return ids;
  },
  pnc_post: function () {
    tblPnc = $('#tblPnc').DataTable({
      responsive: true,
      autoWidth: false,
      destroy: true,
      data: this.items.pnc_post,
      columns: [
        { "data": "id" },
        { "data": "text" },
        { "data": "estado_pnc" },
        { "data": "cantidad_pnc" },
        { "data": "tecnico" },
        { "data": "operario_1" },
        { "data": "operario_2" },
        { "data": "operario_3" },
        { "data": "observaciones" },
        { "data": "id_pnc" },
      ],
      columnDefs: [
        {
          targets: [0],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
            return '<a rel="remove" type="button" class="btn btn-danger btn-xs" style="color: white"><i class="fas fa-trash-alt"></i></a>';
          }
        },
        {
          targets: [-6],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<input type="text" name="tecnico" class="form-control form-control-sm input-sm" value="' + row.operario_1 + '">';
          } 
        },
        {
          targets: [-5],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<input type="text" name="operario_1" class="form-control form-control-sm input-sm" value="' + row.operario_1 + '">'
            } 
        },
        {
          targets: [-4],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<input type="text" name="operario_2" class="form-control form-control-sm input-sm" value="' + row.operario_2 + '">'
            } 
        },
        {
          targets: [-3],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<input type="text" name="operario_3" class="form-control form-control-sm input-sm" value="' + row.operario_3 + '">'
            } 
        },
        {
          targets: [2],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
            if(row.estado_pnc === "Pendiente"){
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido">Retenido</option>\
                  <option value="Pendiente" selected>Pendiente</option>\
                  <option value="Liberado">Liberado</option>\
                  <option value="Destruido">Destruido</option>\
                  <option value="Conciliado">Conciliado</option>\
                  </select>\
              '
            } else if (row.estado_pnc === "Liberado") {
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido">Retenido</option>\
                  <option value="Pendiente">Pendiente</option>\
                  <option value="Liberado" selected>Liberado</option>\
                  <option value="Destruido">Destruido</option>\
                  <option value="Conciliado">Conciliado</option>\
                  </select>\
              '
            } else if (row.estado_pnc === "Destruido") {
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido">Retenido</option>\
                  <option value="Pendiente">Pendiente</option>\
                  <option value="Liberado">Liberado</option>\
                  <option value="Destruido" selected>Destruido</option>\
                  <option value="Conciliado">Conciliado</option>\
                  </select>\
              '
            } else if (row.estado_pnc === "Conciliado") {
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido">Retenido</option>\
                  <option value="Pendiente">Pendiente</option>\
                  <option value="Liberado">Liberado</option>\
                  <option value="Destruido">Destruido</option>\
                  <option value="Conciliado" selected>Conciliado</option>\
                  </select>\
              '
            } else if (row.estado_pnc === "Retenido") {
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido" selected>Retenido</option>\
                  <option value="Pendiente">Pendiente</option>\
                  <option value="Liberado">Liberado</option>\
                  <option value="Destruido">Destruido</option>\
                  <option value="Conciliado">Conciliado</option>\
                  </select>\
              '
            } else {
              return '\
                  <select name="estado_pnc" id="estado_pnc" class="form-control form-control-sm input-sm">\
                  <option value="--------">--------</option>\
                  <option value="Retenido">Retenido</option>\
                  <option value="Pendiente">Pendiente</option>\
                  <option value="Liberado">Liberado</option>\
                  <option value="Destruido">Destruido</option>\
                  <option value="Conciliado">Conciliado</option>\
                  </select>\
              '
            }
          }
        },
        {
          targets: [3],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<input type="number" name="cantidad_pnc" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad_pnc + '">';
          }
        },
        {
          targets: [-2],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '<textarea name="observaciones" class="form-control form-control-sm input-sm" autocomplete="off" rows="2" cols="5">' + row.observaciones + '</textarea>';
          }
        },
        {
          targets: [-1],
          visible: false,
        },
      ],
      rowCallback(row, data, displayNum, displayIndex, dataIndex) {

      },
      initComplete: function (settings, json) {

      }
    });
  },
};

$(function () {
  // buscador de colaboradores
  $('select[name="id_motivo"]').select2({
    theme: "bootstrap4",
    language: 'es',
    allowClear: true,
    ajax: {
      delay: 250,
      type: 'POST',
      url: window.location.pathname,
      data: function (params) {
        var queryParameters = {
          term: params.term,
          action: 'search_motivo',
          ids: JSON.stringify(pnc.get_ids())
        }

        return queryParameters;
      },
      processResults: function (data) {
        return {
          results: data
        };
      },
    },
    placeholder: 'Ingrese el nombre de un motivo!',
    minimumInputLength: 1,
  }).on('select2:select', function (e) {
    var data = e.params.data;
    pnc.items.pnc_post.push(data);
    pnc.pnc_post();
    $(this).val('').trigger('change.select2');
  });

  //Evento: eliminar motivos
  $('#tblPnc tbody').on('click', 'a[rel="remove"]', function () {
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    alert_action('Notificación', '¿Est@ seguro de eliminar el motivo de Pnc?', function () {
      pnc.items.pnc_post.splice(tr.row, 1);
      pnc.pnc_post();
    });
  }).on('change', 'select[name="estado_pnc"]', function () {
    var estado_pnc = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].estado_pnc = estado_pnc;
  }).on('change', 'input[name="cantidad_pnc"]', function () {
    var cantidad_pnc = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].cantidad_pnc = cantidad_pnc;
  }).on('change', 'textarea[name="observaciones"]', function () {
    var observaciones = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].observaciones = observaciones;
  }).on('change', 'input[name="tecnico"]', function () {
    var tecnico = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].tecnico = tecnico;
  }).on('change', 'input[name="operario_1"]', function () {
    var operario_1 = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].operario_1 = operario_1;
  }).on('change', 'input[name="operario_2"]', function () {
    var operario_2 = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].operario_2 = operario_2;
  }).on('change', 'input[name="operario_3"]', function () {
    var operario_3 = $(this).val();
    var tr = tblPnc.cell($(this).closest('td, li')).index();
    pnc.items.pnc_post[tr.row].operario_3 = operario_3;
  });

  //Guardado de datos
  $('#formPnc').on('submit', function (e) {
    e.preventDefault();

    var parameters = new FormData();
    parameters.append('action', $('input[name="action"]').val());
    parameters.append('pnc', JSON.stringify(pnc.items));
    submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear los productos no conformes', function () {
      location.href = '/Producto_no_conforme/Productos_no_conformes/';
    });
  });

  // Inicializar tablas
  pnc.pnc_post();

});
