var tblPruebasEnsayos;
var tblInspeccionDimensiones;
var tblInspeccionAtributos;

var inspeccion = {
    items: {
        numero_op:'',
        tecnico: '',
        operario: '',
        turno: '',
        fecha_despacho: '',
        cantidad_solicitada:0,
        empaque_y_embalaje:'',
        observaciones:'',
        pruebasensayos: [],
        inspecciondimensiones: [],
        inspeccionatributos: [],
    },
    pruebasyoensayos: function () {
        tblPruebasEnsayos = $('#tblPruebasEnsayos').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.pruebasensayos,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "valor" },
                { "data": "tolerancia_p" },
                { "data": "metodo_p" },
                { "data": "valor_p" },
                { "data": "resultado_p" },
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
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="metodo_p" class="form-control form-control-sm input-sm" value="' + row.metodo_p + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="resultado_p" class="form-control form-control-sm input-sm" value="' + row.resultado_p + '">';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="valor_p" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.valor_p + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="valor_p"]').TouchSpin({
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
    inspecciondimensiones: function () {
        tblInspeccionDimensiones = $('#tblInspeccionDimensiones').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.inspecciondimensiones,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "valor_nominal" },
                { "data": "tolerancia_d" },
                { "data": "promedio" },
                { "data": "resultado_id" },
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
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="promedio" class="form-control form-control-sm input-sm" value="' + row.promedio + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="resultado_id" class="form-control form-control-sm input-sm" value="' + row.resultado_id + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="promedio"]').TouchSpin({
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
    inspeccionatributos: function () {
        tblInspeccionAtributos = $('#tblInspeccionAtributos').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.inspeccionatributos,
            columns: [
                { "data": "id" },
                { "data": "text" },
                { "data": "especificacion" },
                { "data": "observacion" },
                { "data": "resultado_ia" },
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
                        return '<input type="text" name="resultado_ia" class="form-control form-control-sm input-sm" value="' + row.resultado_ia + '">';
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    }
};


//Formato busqueda pruebas
function formatRepoPruebas(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Prueba:</b> ' + repo.text + '<br>' +
        '<b>Producto:</b> ' + repo.Nombre_producto + '<br>' +
        '<b>Versión producto:</b> <span class="badge badge-warning">'+repo.version+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

//Formato busqueda dimensiones
function formatRepoDimensiones(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Prueba:</b> ' + repo.text + '<br>' +
        '<b>Producto:</b> ' + repo.Nombre_producto + '<br>' +
        '<b>Versión producto:</b> <span class="badge badge-warning">'+repo.version+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

//Formato busqueda atributos
function formatRepoAtibuto(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">'+
        '<div class="row">' +
        '<div class="text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Prueba:</b> ' + repo.text + '<br>' +
        '<b>Producto:</b> ' + repo.Nombre_producto + '<br>' +
        '<b>Versión producto:</b> <span class="badge badge-warning">'+repo.version+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

$(function () {

    // buscador de pruebas
    $('select[name="pruebas_y_o_ensayos"]').select2({
        theme: "bootstrap4",
        language: 'es',
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
        templateResult: formatRepoPruebas,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        data.metodo_p = '';
        data.valor_p = 0.00;
        data.resultado_p = '';

        inspeccion.items.pruebasensayos.push(data);
        inspeccion.pruebasyoensayos();

        $(this).val('').trigger('change.select2');
    });

    // buscador de atributos
    $('select[name="inspeccion_atributos"]').select2({
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
        templateResult: formatRepoAtibuto,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        data.resultado_ia = '';

        inspeccion.items.inspeccionatributos.push(data);
        inspeccion.inspeccionatributos();

        $(this).val('').trigger('change.select2');
    });

      // buscador de dimensiones
      $('select[name="inspeccion_dimensional"]').select2({
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
        templateResult: formatRepoDimensiones,
    }).on('select2:select', function (e) {
        var data = e.params.data;

        data.promedio = 0.00;
        data.resultado_id = '';

        inspeccion.items.inspecciondimensiones.push(data);
        inspeccion.inspecciondimensiones();

        $(this).val('').trigger('change.select2');
    });


    //Eventos: resultado, valor y eliminar de pruebas
    $('#tblPruebasEnsayos tbody').on('change', 'input[name="valor_p"]', function () {
        console.clear();
        var valor_p = parseFloat($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].valor_p = valor_p;
    })
    .on('change', 'input[name="metodo_p"]', function () {
        console.clear();
        var metodo_p = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].metodo_p = metodo_p; 
    })
    .on('change', 'input[name="resultado_p"]', function () {
        console.clear();
        var resultado_p = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].resultado_p = resultado_p; 
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta prueba y/o ensayo de la ficha técnica?', function () {
            inspeccion.items.pruebasensayos.splice(tr.row, 1);
            inspeccion.pruebasyoensayos();
        });
    });

    //Evento: resultado, promedio y eliminar de dimensiones
    $('#tblInspeccionDimensiones tbody').on('change', 'input[name="promedio"]', function () {
        console.clear();
        var promedio = parseFloat($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].promedio = promedio
    })
    .on('change', 'input[name="resultado_id"]', function () {
        console.clear();
        var resultado_id = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].resultado_id = resultado_id; 
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            inspeccion.items.inspecciondimensiones.splice(tr.row, 1);
            inspeccion.inspecciondimensiones();
        });
    });

    //Evento: resultado y eliminar item de atributos
    $('#tblInspeccionAtributos tbody').on('change', 'input[name="resultado_ia"]', function () {
        console.clear();
        var resultado_ia = ($(this).val());
        var tr = tblInspeccionAtributos.cell($(this).closest('td, li')).index();
        inspeccion.items.inspeccionatributos[tr.row].resultado_ia = resultado_ia
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblInspeccionAtributos.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            inspeccion.items.inspeccionatributos.splice(tr.row, 1);
            inspeccion.inspeccionatributos();
        });
    });

    //Guardado de datos
    $('form').on('submit', function(e){
        e.preventDefault();

        inspeccion.items.numero_op = $('input[name="numero_op_id"]').val();
        inspeccion.items.tecnico = $('input[name="tecnico"]').val();
        inspeccion.items.operario = $('input[name="operario"]').val();
        inspeccion.items.turno = $('select[name="turno"]').val();
        inspeccion.items.fecha_despacho = $('input[name="fecha_despacho"]').val();
        inspeccion.items.cantidad_solicitada = $('input[name="cantidad_solicitada"]').val();
        inspeccion.items.empaque_y_embalaje = $('textarea[name="empaque_y_embalaje"]').val();
        inspeccion.items.observaciones = $('textarea[name="observaciones"]').val();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('inspeccion', JSON.stringify(inspeccion.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Control_calidad/Inspecciones_calidad/';
        });
    });

});
