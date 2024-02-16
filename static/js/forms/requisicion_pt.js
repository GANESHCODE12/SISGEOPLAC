var tblRequisionesPT;

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
        '<b>Color:</b> ' + repo.color + '<br>' +
        '<b>Cantidad:</b> <span class="badge badge-success">'+repo.cantidad_disponible+'</span>'+ '<br>' +
        '<b>Cantidad PNC:</b> <span class="badge badge-danger">'+repo.pnc+'</span>'+ '<br>' +
        '<b>Código:</b> <span class="badge badge-warning">'+repo.codigo_producto+'</span>'+ '<br>' +
        '<b>Orden:</b> <span class="badge badge-info">'+repo.orden+'</span>'+ '<br>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');
    if (repo.cantidad_disponible > 0) {
        return option;
    }
}

var solicitudes_pt = {
    items: {
        requisicion_pt: [],
    },
    calculo_disponible: function () {
        $.each(this.items.requisicion_pt, function (pos, dict) {
            dict.pos = pos;
            dict.cantidad_ingresada = dict.cantidad_disponible - parseFloat(dict.cantidad_solicitada);
            cantidad_ingresada = dict.cantidad_ingresada;
        });
        this.items.requisicion_pt.cantidad_ingresada = cantidad_ingresada
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.requisicion_pt, function (key, value){
            ids.push(value.id);
        });
        return ids;
    },
    requisicion_pt: function () {
        tblRequisionesPT = $('#tblRequisionesPT').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.requisicion_pt,
            columns: [
                { "data": "id" },
                { "data": "orden" },
                { "data": "text" },
                { "data": "codigo_producto" },
                { "data": "color" },
                { "data": "cantidad_disponible" },
                { "data": "cantidad_solicitada" },
                { "data": "observaciones_PT" },
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
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input name="observaciones_PT" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.observaciones_PT + '">';
                    }
                },
                {
                    targets: [-1],
                    visible: false
                },
                {
                    targets: [5],
                    render: function (data, type, row) {
                        return data.toString().replace(
                            /\B(?=(\d{3})+(?!\d))/g, "."
                        );
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cantidad_solicitada"]').TouchSpin({
                    min: 0,
                    max: data.cantidad_disponible,
                    decimals: 2,
                    boostat: 10,
                    maxboostedstep: 30,
                    step: 1.00
                });
            },
            initComplete: function (settings, json) {

            }
        });
    }
};

$(function () {

    // buscador de elementos
    $('select[name="id_requision_pt"]').select2({
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
                    action: 'search_PT',
                    ids: JSON.stringify(solicitudes_pt.get_ids())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre, el color o el código de un producto!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        solicitudes_pt.items.requisicion_pt.push(data);
        solicitudes_pt.requisicion_pt();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar elementos
    $('#tblRequisionesPT tbody').on('change', 'input[name="cantidad_solicitada"]', function () {
        console.clear();
        var cantidad_solicitada = parseFloat($(this).val());
        var tr = tblRequisionesPT.cell($(this).closest('td, li')).index();
        var data = tblRequisionesPT.row(tr.row).node();
        solicitudes_pt.items.requisicion_pt[tr.row].cantidad_solicitada = cantidad_solicitada
        solicitudes_pt.calculo_disponible();
        $('td:eq(5)', tblRequisionesPT.row(tr.row).node()).html(solicitudes_pt.items.requisicion_pt[tr.row].cantidad_ingresada.toFixed(2))
    })
    .on('change', 'input[name="observaciones_PT"]', function () {
        console.clear();
        var observaciones_PT = $(this).val();
        var tr = tblRequisionesPT.cell($(this).closest('td, li')).index();
        var data = tblRequisionesPT.row(tr.row).node();
        console.log(data)
        solicitudes_pt.items.requisicion_pt[tr.row].observaciones_PT = observaciones_PT
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblRequisionesPT.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            solicitudes_pt.items.requisicion_pt.splice(tr.row, 1);
            solicitudes_pt.requisicion_pt();
        });
    });

    //Guardado de datos
    $('#formRequisionesPT').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('solicitudes_pt', JSON.stringify(solicitudes_pt.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Inventario/Inventario_PT';
        });
    });

    // Inicializar tablas
    solicitudes_pt.requisicion_pt();

});
