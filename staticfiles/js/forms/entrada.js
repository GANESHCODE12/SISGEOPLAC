var tblEntradas;

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.nombre + '<br>' +
        '<b>Proveedor:</b> ' + repo.proveedor + '<br>' +
        '<b>Categoria:</b> ' + repo.categoria + '<br>' +
        '<b>Referencia:</b> <span class="badge badge-warning">'+repo.referencia+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

var entradas = {
    items: {
        entrada: [],
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.entrada, function (key, value){
            ids.push(value.id);
        });
        return ids;
    },
    entrada: function () {
        tblEntradas = $('#tblEntradas').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.entrada,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "referencia" },
                { "data": "cantidad_ingresada" },
                { "data": "factura" },
                { "data": "remision" },
                { "data": "lote" },
                { "data": "observaciones_ingreso_materia_prima" },
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
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad_ingresada" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad_ingresada + '">';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="factura" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.factura + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="remision" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.remision + '">';
                    }
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="lote" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.remision + '">';
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="observaciones_ingreso_materia_prima" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.observaciones_ingreso_materia_prima + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cantidad_ingresada"]').TouchSpin({
                    min: 0,
                    max: 10000000,
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
    $('select[name="id_entrada"]').select2({
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
                    action: 'search_MP_Insumo',
                    ids: JSON.stringify(entradas.get_ids())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre o la referencia de un elemento!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        entradas.items.entrada.push(data);
        entradas.entrada();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar elementos
    $('#tblEntradas tbody').on('change', 'input[name="cantidad_ingresada"]', function () {
        console.clear();
        var cantidad_ingresada = parseFloat($(this).val());
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        console.log(tr)
        var data = tblEntradas.row(tr.row).node();
        entradas.items.entrada[tr.row].cantidad_ingresada = cantidad_ingresada
    })
    .on('change', 'input[name="factura"]', function () {
        console.clear();
        var factura = $(this).val();
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        var data = tblEntradas.row(tr.row).node();
        entradas.items.entrada[tr.row].factura = factura; 
    })
    .on('change', 'input[name="remision"]', function () {
        console.clear();
        var remision = $(this).val();
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        var data = tblEntradas.row(tr.row).node();
        entradas.items.entrada[tr.row].remision = remision; 
    })
    .on('change', 'input[name="lote"]', function () {
        var lote = $(this).val();
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        var data = tblEntradas.row(tr.row).node();
        entradas.items.entrada[tr.row].lote = lote; 
    })
    .on('change', 'input[name="observaciones_ingreso_materia_prima"]', function () {
        console.clear();
        var observaciones_ingreso_materia_prima = $(this).val();
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        var data = tblEntradas.row(tr.row).node();
        entradas.items.entrada[tr.row].observaciones_ingreso_materia_prima = observaciones_ingreso_materia_prima; 
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblEntradas.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            entradas.items.entrada.splice(tr.row, 1);
            entradas.entrada();
        });
    });

    $('.btnAddElement').on('click',  function () {
        $('#myModalElemento').modal('show');
    });

    $('#myModalElemento').on('hidden.bs.modal', function (e) {
        $('#formElement').trigger('reset');
    });

    $('#formElement').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', 'create_element');
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el elemento?', function(response){
            $('#myModalElemento').modal('hide');
        });
    });

    //Guardado de datos
    $('#formEntries').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('entradas', JSON.stringify(entradas.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Inventario/Lista_elementos_MP_insumos';
        });
    });

    // Inicializar tablas
    entradas.entrada();

});
