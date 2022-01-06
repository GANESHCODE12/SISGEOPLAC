var tblPruebas;
var tblDimensiones;
var tblNormas;
var tblAtributos;

var ficha = {
    items: {
        producto: [],
        normas: [],
        pruebas: [],
        dimensiones: [],
        atributos: [],
    },
    normas: function () {
        tblNormas = $('#tblNormas').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.normas,
            columns: [
                { "data": "id" },
                { "data": "codigo" },
                { "data": "titulo" },
                //se agrega con la misma estructura y con el valor que se dio en el autocomplete
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
            ],
            initComplete: function (settings, json) {

            }
        });
    },
    pruebas: function () {
        tblPruebas = $('#tblPruebas').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.pruebas,
            columns: [
                { "data": "id" },
                { "data": "variables" },
                { "data": "valor" },
                { "data": "tolerancia_p" },
                //se agrega con la misma estructura y con el valor que se dio en el autocomplete
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
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="valor" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.valor + '">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="tolerancia_p" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.tolerancia_p + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="valor"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                });
                $(row).find('input[name="tolerancia_p"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                });

            },
            initComplete: function (settings, json) {

            }
        });
    },
    dimensiones: function () {
        tblDimensiones = $('#tblDimensiones').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.dimensiones,
            columns: [
                { "data": "id" },
                { "data": "caracteristicas_control" },
                { "data": "valor_nominal" },
                { "data": "tolerancia_d" },
                //se agrega con la misma estructura y con el valor que se dio en el autocomplete
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
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="valor_nominal" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.valor_nominal + '">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="tolerancia_d" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.tolerancia_d + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="valor_nominal"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                });
                $(row).find('input[name="tolerancia_d"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                });

            },
            initComplete: function (settings, json) {

            }
        });
    },
    atributos: function () {
        tblAtributos = $('#tblAtributos').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.atributos,
            columns: [
                { "data": "id" },
                { "data": "caracteristicas" },
                { "data": "especificacion" },
                { "data": "observacion" },
                //se agrega con la misma estructura y con el valor que se dio en el autocomplete
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
            ],
            initComplete: function (settings, json) {

            }
        });
    }
};

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.Nombre_producto + '<br>' +
        '<b>Cliente:</b> ' + repo.cliente_especifico + '<br>' +
        '<b>Versión:</b> <span class="badge badge-warning">'+repo.version+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

$(function () {

    // buscador de normas
    $('select[name="id_normas"]').select2({
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
                    action: 'search_normas'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre de una norma!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        ficha.items.normas.push(data);
        ficha.normas();
        $(this).val('').trigger('change.select2');
    });

    // buscador de pruebas
    $('select[name="id_pruebas"]').select2({
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
                    action: 'search_pruebas'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre de una prueba y/o ensayo!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        data.valor = 0.00;
        data.tolerancia_p = 0.00;

        ficha.items.pruebas.push(data);
        ficha.pruebas();

        $(this).val('').trigger('change.select2');
    });

    // buscador de atributos
    $('select[name="id_atributos"]').select2({
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
                    action: 'search_atributos'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un atributo!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        ficha.items.atributos.push(data);
        ficha.atributos();

        $(this).val('').trigger('change.select2');
    });

      // buscador de dimensiones
      $('select[name="id_dimensiones"]').select2({
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
                    action: 'search_dimensiones'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una dimensión!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        data.valor_nominal = 0.00;
        data.tolerancia_d = 0.00;

        ficha.items.dimensiones.push(data);
        ficha.dimensiones();

        $(this).val('').trigger('change.select2');
    });

    // buscador de productos
    $('select[name="id_producto"]').select2({
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
                    action: 'search_producto'
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un producto!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        ficha.items.producto.push(data)

    });

    //Eventos: valor, tolerancia y eliminar de pruebas
    $('#tblPruebas tbody').on('change', 'input[name="valor"]', function () {
        console.clear();
        var valor = parseFloat($(this).val());
        var tr = tblPruebas.cell($(this).closest('td, li')).index();
        ficha.items.pruebas[tr.row].valor = valor;
    })
    .on('change', 'input[name="tolerancia_p"]', function () {
        console.clear();
        var tolerancia_p = parseFloat($(this).val());
        var tr = tblPruebas.cell($(this).closest('td, li')).index();
        ficha.items.pruebas[tr.row].tolerancia_p = tolerancia_p; 
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblPruebas.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta prueba y/o ensayo de la ficha técnica?', function () {
            ficha.items.pruebas.splice(tr.row, 1);
            ficha.pruebas();
        });
    });

    //Evento: valor, tolerancia y eliminar de dimensiones
    $('#tblDimensiones tbody').on('change', 'input[name="valor_nominal"]', function () {
        console.clear();
        var valor_nominal = parseFloat($(this).val());
        var tr = tblDimensiones.cell($(this).closest('td, li')).index();
        console.log(tr)
        var data = tblDimensiones.row(tr.row).node();
        ficha.items.dimensiones[tr.row].valor_nominal = valor_nominal
    })
    .on('change', 'input[name="tolerancia_d"]', function () {
        console.clear();
        var tolerancia_d = parseFloat($(this).val());
        var tr = tblDimensiones.cell($(this).closest('td, li')).index();
        var data = tblDimensiones.row(tr.row).node();
        ficha.items.dimensiones[tr.row].tolerancia_d = tolerancia_d; 
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblDimensiones.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            ficha.items.dimensiones.splice(tr.row, 1);
            ficha.dimensiones();
        });
    });

    //Eliminar item de normas
    $('#tblNormas tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblNormas.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta norma de la ficha técnica?', function () {
            ficha.items.normas.splice(tr.row, 1);
            ficha.normas();
        });
    });

    //Eliminar item de atributos
    $('#tblAtributos tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblAtributos.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar este atributo de la ficha técnica?', function () {
            ficha.items.atributos.splice(tr.row, 1);
            ficha.atributos();
        });
    });

    //Guardado de datos
    $('form').on('submit', function(e){
        e.preventDefault();

        ficha.items.id_producto = $('select[name="id_producto"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('ficha', JSON.stringify(ficha.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = 'listado_productos';
        });
    });

});
