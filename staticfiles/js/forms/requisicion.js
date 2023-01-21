var tblRequisiones;

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.text + '<br>' +
        '<b>Lote:</b> ' + repo.lote + '<br>' +
        '<b>Referencia:</b> <span class="badge badge-warning">'+repo.referencia+'</span>'+ '<br>' +
        '<b>Cantidad necesaria para la orden:</b> <span class="badge badge-success">'+repo.cantidad_disponible.toFixed(2)+'</span>'+ '<br>' +
        '<b>Cantidad disponible en inventario:</b> <span class="badge badge-info">'+repo.cantidad_inventario.toFixed(2)+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');
    return option;
}

var solicitudes = {
    items: {
        requisicion: [],
    },
    calculo_disponible: function () {
        $.each(this.items.requisicion, function (pos, dict) {
            dict.pos = pos;
            dict.cantidad_ingresada = dict.cantidad_disponible - parseFloat(dict.cantidad_solicitada);
            cantidad_ingresada = dict.cantidad_ingresada;
        });
        this.items.requisicion.cantidad_ingresada = cantidad_ingresada
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.requisicion, function (key, value){
            ids.push(value.id);
        });
        return ids;
    },
    requisicion: function () {
        tblRequisiones = $('#tblRequisiones').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.requisicion,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "referencia" },
                { "data": "tipo" },
                { "data": "lote" },
                { "data": "cantidad_disponible" },
                { "data": "cantidad_solicitada" },
                { "data": "observaciones_solicitud" },
                { "data": "cantidad_disponible" },

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
                    targets: [1, 2, 3, 4, 5],
                    class: 'text-center',
                    orderable: false,
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad_solicitada" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad_solicitada + '">';
                    }
                },
                {
                    targets: [5],
                    render: function (data, type, row) {
                        return data.toString().replace(
                            /\B(?=(\d{3})+(?!\d))/g, "."
                        );
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input name="observaciones_solicitud" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.observaciones_solicitud + '">';
                    }
                },
                {
                    targets: [-1],
                    visible: false,
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                    $(row).find('input[name="cantidad_solicitada"]').TouchSpin({
                        min: 0,
                        max: data.cantidad_disponible,
                        decimals: 2,
                        boostat: 1,
                        maxboostedstep: 30,
                        step: 0.01
                    });
            },
            initComplete: function (settings, json) {

            }
        });
    }
};

$(function () {

    // buscador de elementos
    $('select[name="id_requision"]').select2({
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
                    action: 'search_MP_Ingreso',
                    ids: JSON.stringify(solicitudes.get_ids())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre, la referencia o el lote de un elemento!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        solicitudes.items.requisicion.push(data);
        solicitudes.requisicion();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar elementos
    $('#tblRequisiones tbody').on('change', 'input[name="cantidad_solicitada"]', function () {
        var cantidad_solicitada = parseFloat($(this).val());
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        solicitudes.items.requisicion[tr.row].cantidad_solicitada = cantidad_solicitada
        solicitudes.calculo_disponible();
        $('td:eq(5)', tblRequisiones.row(tr.row).node()).html(solicitudes.items.requisicion[tr.row].cantidad_ingresada.toFixed(2))
    })
    .on('change', 'input[name="observaciones_solicitud"]', function () {
        var observaciones_solicitud = $(this).val();
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        solicitudes.items.requisicion[tr.row].observaciones_solicitud = observaciones_solicitud
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            solicitudes.items.requisicion.splice(tr.row, 1);
            solicitudes.requisicion();
        });
    });

    //Guardado de datos
    $('#formRequisiones').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('solicitudes', JSON.stringify(solicitudes.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/produccion/listado_ordenes';
        });
    });

    // Inicializar tablas
    solicitudes.requisicion();

});
