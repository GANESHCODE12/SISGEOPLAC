var tblPruebas;
var tblDimensiones;
var tblNormas;
var tblAtributos;
var tblColores;

var ficha = {
    items: {
        Nombre_producto: '',
        numero_ficha: '',
        proceso: '',
        version: '',
        fecha_vigencia: '',
        tipo_producto: '',
        cliente_especifico: '',
        estado_ficha: '',
        cavidades: '',
        peso: '',
        material: '',
        ciclo: '',
        descripción_especificaciones: '',
        olor: '',
        pigmento: '',
        tipo: '',
        unidad_empaque: '',
        forma_empaque: '',
        caja: '',
        bolsa: '',
        plano: '',
        fecha_plano: '',
        vida_util: '',
        elaborado: '',
        revisado: '',
        aprobado: '',
        notas: '',
        normas: [],
        pruebas: [],
        dimensiones: [],
        atributos: [],
        colores: [],
    },
    get_ids_normas: function () {
        var ids_normas = [];
        $.each(this.items.normas, function (key, value){
            ids_normas.push(value.id);
        });
        return ids_normas;
    },
    get_ids_pruebas: function () {
        var ids_pruebas = [];
        $.each(this.items.pruebas, function (key, value){
            ids_pruebas.push(value.id);
        });
        return ids_pruebas;
    },
    get_ids_dimensiones: function () {
        var ids_dimensiones = [];
        $.each(this.items.dimensiones, function (key, value){
            ids_dimensiones.push(value.id);
        });
        return ids_dimensiones;
    },
    get_ids_atributos: function () {
        var ids_atributos = [];
        $.each(this.items.atributos, function (key, value){
            ids_atributos.push(value.id);
        });
        return ids_atributos;
    },
    get_ids_colores: function () {
        var ids_colores = [];
        $.each(this.items.colores, function (key, value){
            ids_colores.push(value.id);
        });
        return ids_colores;
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
    },
    colores: function () {
        tblColores = $('#tblColores').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.colores,
            columns: [
                { "data": "id" },
                { "data": "color" },
                { "data": "codigo_producto" }
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
                        return '<input type="text" name="codigo_producto" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.codigo_producto + '">';
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    }
};

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
                    action: 'search_normas',
                    ids_normas: JSON.stringify(ficha.get_ids_normas())
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
                    action: 'search_pruebas',
                    ids_pruebas: JSON.stringify(ficha.get_ids_pruebas())
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
                    action: 'search_atributos',
                    ids_atributos: JSON.stringify(ficha.get_ids_atributos())
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
                    action: 'search_dimensiones',
                    ids_dimensiones: JSON.stringify(ficha.get_ids_dimensiones())
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

    // buscador de color
    $('select[name="id_colores"]').select2({
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
                    action: 'search_colores',
                    ids_colores: JSON.stringify(ficha.get_ids_colores())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un color!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        ficha.items.colores.push(data);
        ficha.colores();
        $(this).val('').trigger('change.select2');
    });

    //Eventos: valor, tolerancia y eliminar de pruebas
    $('#tblPruebas tbody').on('change', 'input[name="valor"]', function () {
        var valor = parseFloat($(this).val());
        var tr = tblPruebas.cell($(this).closest('td, li')).index();
        ficha.items.pruebas[tr.row].valor = valor;
    })
    .on('change', 'input[name="tolerancia_p"]', function () {
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
        var valor_nominal = parseFloat($(this).val());
        var tr = tblDimensiones.cell($(this).closest('td, li')).index();
        console.log(tr)
        var data = tblDimensiones.row(tr.row).node();
        ficha.items.dimensiones[tr.row].valor_nominal = valor_nominal
    })
    .on('change', 'input[name="tolerancia_d"]', function () {
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
    
    //Eliminar colores
    $('#tblColores tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblColores.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar este color de la ficha técnica?', function () {
            ficha.items.colores.splice(tr.row, 1);
            ficha.colores();
        });
    })
    .on('change', 'input[name="codigo_producto"]', function () {
        var codigo_producto = $(this).val();
        var tr = tblColores.cell($(this).closest('td, li')).index();
        ficha.items.colores[tr.row].codigo_producto = codigo_producto; 
    });

    //Guardado de datos
    $('form').on('submit', function(e){
        e.preventDefault();

        ficha.items.Nombre_producto = $('input[name="Nombre_producto"]').val();
        ficha.items.numero_ficha = $('input[name="numero_ficha"]').val();
        ficha.items.proceso = $('input[name="proceso"]').val();
        ficha.items.version = $('input[name="version"]').val();
        ficha.items.fecha_vigencia = $('input[name="fecha_vigencia"]').val();
        ficha.items.tipo_producto = $('input[name="tipo_producto"]').val();
        ficha.items.cliente_especifico = $('input[name="cliente_especifico"]').val();
        ficha.items.estado_ficha = $('select[name="estado_ficha"]').val();
        ficha.items.cavidades = $('input[name="cavidades"]').val();
        ficha.items.peso = $('input[name="peso"]').val();
        ficha.items.material = $('input[name="material"]').val();
        ficha.items.ciclo = $('input[name="ciclo"]').val();
        ficha.items.descripción_especificaciones = $('input[name="descripción_especificaciones"]').val();
        ficha.items.olor = $('input[name="olor"]').val();
        ficha.items.pigmento = $('input[name="pigmento"]').val();
        ficha.items.tipo = $('input[name="tipo"]').val();
        ficha.items.unidad_empaque = $('input[name="unidad_empaque"]').val();
        ficha.items.forma_empaque = $('input[name="forma_empaque"]').val();
        ficha.items.caja = $('input[name="caja"]').val();
        ficha.items.bolsa = $('input[name="bolsa"]').val();
        ficha.items.plano = $('input[name="plano"]').val();
        ficha.items.fecha_plano = $('input[name="fecha_plano"]').val();
        ficha.items.vida_util = $('textarea[name="vida_util"]').val();
        ficha.items.elaborado = $('input[name="elaborado"]').val();
        ficha.items.revisado = $('input[name="revisado"]').val();
        ficha.items.aprobado = $('input[name="aprobado"]').val();
        ficha.items.notas = $('textarea[name="notas"]').val();

        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('ficha', JSON.stringify(ficha.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/productos/listado_productos';
        });
    });

    // Inicializar tablas
    ficha.dimensiones();
    ficha.normas();
    ficha.atributos();
    ficha.pruebas();
    ficha.colores();

});
