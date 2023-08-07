var tblColaboradores;
var tblParadas;
var tblRequisiones;

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        '<p style="margin-bottom: 0;">' +
        '<b>Colaborador:</b> ' + repo.nombre + '<br>' +
        '<b>Cargo:</b> ' + repo.cargo + '<br>' +
        '<b>Código:</b> <span class="badge badge-success">' + repo.codigo + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

function formatRepoMateriales(repo) {
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
        '<b>Cantidad disponible en inventario:</b> <span class="badge badge-info">'+repo.cantidad_inventario.toFixed(2)+'</span>'+ '<br>' +
        '<b>Cantidad producto no conforme:</b> <span class="badge badge-danger">'+repo.pnc.toFixed(2)+'</span>'+
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');
    if (repo.cantidad_inventario > 0) {
        return option;
    }
}

var control = {
    items: {
        turno:'',
        hora_inicio:'',
        hora_final:'',
        cantidad_producida:0,
        ciclo_turno:0,
        cavidades_operacion:0,
        observaciones:'',
        material_molido: 0,
        colaborador: [],
        motivo: [],
        requisicion: [],
    },
    tiempos_paradas: function () {
        var tiempos = [];
        $.each(this.items.motivo, function (key, value) {
            let timerelated = value.tiempo_paradas.split(':');
            let tiempo = new Date(timerelated);
            let timestamp = tiempo.getTime()
            tiempos.push(timestamp);
        });
        const reducer = (accumulator, curr) => accumulator + curr;

        return tiempos.reduce(reducer);
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.colaborador, function (key, value) {
            ids.push(value.id);
        });
        return ids;
    },
    get_ids_motivos: function () {
        var ids_motivos = [];
        $.each(this.items.motivo, function (key, value) {
            ids_motivos.push(value.id);
        });
        return ids_motivos;
    },
    calculo_disponible: function () {
        $.each(this.items.requisicion, function (pos, dict) {
            dict.pos = pos;
            dict.cantidad_ingresada = dict.cantidad_disponible - parseFloat(dict.cantidad_solicitada);
            cantidad_ingresada = dict.cantidad_ingresada;
        });
        this.items.requisicion.cantidad_ingresada = cantidad_ingresada
    },
    get_ids_materiales: function () {
        var ids_materiales = [];
        $.each(this.items.requisicion, function (key, value){
            ids_materiales.push(value.id);
        });
        return ids_materiales;
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
    },
    colaborador: function () {
        tblColaboradores = $('#tblColaboradores').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.colaborador,
            columns: [
                { "data": "id" },
                { "data": "id" },
                { "data": "nombre" },
                { "data": "cargo" },
                { "data": "codigo" },
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
                    targets: [1, 2, 3],
                    class: 'text-center',
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

            },
            initComplete: function (settings, json) {

            }
        });
    },
    motivo: function () {
        tblParadas = $('#tblParadas').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.motivo,
            columns: [
                { "data": "id" },
                { "data": "id" },
                { "data": "motivo" },
                { "data": "horas" },
                { "data": "minutos" },
                { "data": "observacion" },
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
                        return '<input type="number" name="horas" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.horas + '">';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="minutos" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.minutos + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="observacion" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.observacion + '">';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

            },
            initComplete: function (settings, json) {

            }
        });
    }
};

$(function () {
    // buscador de colaboradores
    $('select[name="id_colaborador"]').select2({
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
                    action: 'search_colaborador',
                    ids_colaborador: JSON.stringify(control.get_ids())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre o el código de un colaborador!',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        control.items.colaborador.push(data);
        control.colaborador();
        $(this).val('').trigger('change.select2');
    });

    // buscador de motivos paradas
    $('select[name="id_paradas"]').select2({
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
                    ids_motivos: JSON.stringify(control.get_ids_motivos())
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese un motivo!',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        control.items.motivo.push(data);
        control.motivo();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar colaboradores
    $('#tblColaboradores tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblColaboradores.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar al colaborador del control de producción?', function () {
            control.items.colaborador.splice(tr.row, 1);
            control.colaborador();
        });
    });
    //Evento: eliminar motivos
    $('#tblParadas tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblParadas.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar el motivo de parada?', function () {
            control.items.motivo.splice(tr.row, 1);
            control.motivo();
        });
    }).on('change', 'input[name="minutos"]', function () {
        var minutos = $(this).val();
        var tr = tblParadas.cell($(this).closest('td, li')).index();
        control.items.motivo[tr.row].minutos = minutos; 
    }).on('change', 'input[name="horas"]', function () {
        var horas = $(this).val();
        var tr = tblParadas.cell($(this).closest('td, li')).index();
        control.items.motivo[tr.row].horas = horas; 
    }).on('change', 'input[name="observacion"]', function () {
        var observacion = $(this).val();
        var tr = tblParadas.cell($(this).closest('td, li')).index();
        control.items.motivo[tr.row].observacion = observacion; 
    });

    // buscador de elementos
    $('select[name="id_materiales"]').select2({
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
                    action: 'search_material',
                    ids_materiales: JSON.stringify(control.get_ids_materiales())
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
        templateResult: formatRepoMateriales,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        control.items.requisicion.push(data);
        control.requisicion();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar elementos
    $('#tblRequisiones tbody').on('change', 'input[name="cantidad_solicitada"]', function () {
        var cantidad_solicitada = parseFloat($(this).val());
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        control.items.requisicion[tr.row].cantidad_solicitada = cantidad_solicitada
        control.calculo_disponible();
        $('td:eq(5)', tblRequisiones.row(tr.row).node()).html(control.items.requisicion[tr.row].cantidad_ingresada.toFixed(2))
    })
    .on('change', 'input[name="observaciones_solicitud"]', function () {
        var observaciones_solicitud = $(this).val();
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        control.items.requisicion[tr.row].observaciones_solicitud = observaciones_solicitud
    })
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblRequisiones.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar esta dimensión de la ficha técnica?', function () {
            control.items.requisicion.splice(tr.row, 1);
            control.requisicion();
        });
    });
    

    //Modal crear motivo
    $('.btnAddElement').on('click',  function () {
        $('#myModalElemento').modal('show');
        console.log(control.tiempos_paradas())
    });
    $('#myModalElemento').on('hidden.bs.modal', function (e) {
        $('#formElement').trigger('reset');
    });
    $('#formElement').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData(this);
        parameters.append('action', 'create_element');
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el motivo?', function(response){
            $('#myModalElemento').modal('hide');
        });
    });

    //Guardado de datos
    $('#formControl').on('submit', function(e){
        e.preventDefault();

        control.items.turno = $('select[name="turno"]').val();
        control.items.hora_inicio = $('input[name="hora_inicio"]').val();
        control.items.hora_final = $('input[name="hora_final"]').val();
        control.items.cantidad_producida = $('input[name="cantidad_producida"]').val();
        control.items.ciclo_turno = $('input[name="ciclo_turno"]').val();
        control.items.cavidades_operacion = $('input[name="cavidades_operacion"]').val();
        control.items.material_molido = $('input[name="material_molido"]').val();
        control.items.observaciones = $('textarea[name="observaciones"]').val();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('control', JSON.stringify(control.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Control_produccion/Control_orden/';
        });
    });

    // Inicializar tablas
    control.colaborador();
    control.motivo();
    control.requisicion();

});

$(function () {
    $("#hora_inicio").datetimepicker({
        format: 'DD-MM-YYYY HH:mm Z',
        icons: {
            'time': "fa fa-clock",
            'date': "fa fa-calendar",
            'up': "fa fa-arrow-up",
            'down': "fa fa-arrow-down"
        }
    });
    $("#hora_final").datetimepicker({
        format: 'DD-MM-YYYY HH:mm Z',
        icons: {
            'time': "fa fa-clock",
            'date': "fa fa-calendar",
            'up': "fa fa-arrow-up",
            'down': "fa fa-arrow-down"
        }
    });
});