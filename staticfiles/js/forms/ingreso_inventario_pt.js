var tblInventario;

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        '<p style="margin-bottom: 0;">' +
        '<b>Producto:</b> ' + repo.text + '<br>' +
        '<b>Código:</b> ' + repo.codigo_producto + '<br>' +
        '<b>Color:</b> ' + repo.color + '<br>' +
        '<b>Versión:</b> <span class="badge badge-warning">'+repo.version+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

var inventario = {
    items: {
        productos: [],
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.productos, function (key, value){
            ids.push(value.id);
        });
        return ids;
    },
    productos: function () {
        tblInventario = $('#tblInventario').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.productos,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "color" },
                { "data": "codigo_producto" },
                { "data": "version" },
                { "data": "cantidad" },
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
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cantidad"]').TouchSpin({
                    min: 0,
                    max: 100000000,
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
    $('select[name="id_inventario"]').select2({
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
                    action: 'search_Inventario',
                    ids: JSON.stringify(inventario.get_ids())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el Nombre del producto!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        inventario.items.productos.push(data);
        inventario.productos();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar elementos
    $('#tblInventario tbody').on('change', 'input[name="cantidad"]', function () {
        console.clear();
        var cantidad = $(this).val();
        var tr = tblInventario.cell($(this).closest('td, li')).index();
        console.log(tr)
        var data = tblInventario.row(tr.row).node();
        inventario.items.productos[tr.row].cantidad = cantidad
    });

    //Guardado de datos
    $('#formInventario').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('inventario', JSON.stringify(inventario.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Inventario/Lista_elementos_MP_insumos';
        });
    });

    // Inicializar tablas
    inventario.productos();

});
