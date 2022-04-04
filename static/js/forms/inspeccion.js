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
            ordering: false,
            info: false,
            paging: false,
            searching: false,
            data: this.items.pruebasensayos,
            columns: [
                { "data": "text" },
                { "data": "valor" },
                { "data": "tolerancia_p" },
                { "data": "metodo_p" },
                { "data": "valor_p" },
                { "data": "resultado_p" },
            ],
            columnDefs: [
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
                })
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
            ordering: false,
            info: false,
            paging: false,
            searching: false,
            data: this.items.inspecciondimensiones,
            columns: [
                { "data": "text" },
                { "data": "valor_nominal" },
                { "data": "tolerancia_d" },
                { "data": "promedio" },
                { "data": "resultado_id" },
            ],
            columnDefs: [
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="promedio" class="form-control form-control-sm input-sm" value="' + row.promedio + '">';
                    }
                },
                {
                    targets: [4],
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
                })
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
            ordering: false,
            info: false,
            paging: false,
            searching: false,
            data: this.items.inspeccionatributos,
            columns: [
                { "data": "text" },
                { "data": "especificacion" },
                { "data": "observacion" },
                { "data": "resultado_ia" },
            ],
            columnDefs: [
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

$(function () {

    //Eventos: resultado y valor de pruebas
    $('#tblPruebasEnsayos tbody').on('change', 'input[name="valor_p"]', function () {
        var valor_p = parseFloat($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].valor_p = valor_p;
    }).on('change', 'input[name="metodo_p"]', function () {
        var metodo_p = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].metodo_p = metodo_p; 
    }).on('change', 'input[name="resultado_p"]', function () {
        var resultado_p = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].resultado_p = resultado_p; 
    });

    //Evento: resultado, promedio y eliminar de dimensiones
    $('#tblInspeccionDimensiones tbody').on('change', 'input[name="promedio"]', function () {
        var promedio = parseFloat($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].promedio = promedio
    })
    .on('change', 'input[name="resultado_id"]', function () {
        var resultado_id = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].resultado_id = resultado_id; 
    });

    //Evento: resultado y eliminar item de atributos
    $('#tblInspeccionAtributos tbody').on('change', 'input[name="resultado_ia"]', function () {
        var resultado_ia = ($(this).val());
        var tr = tblInspeccionAtributos.cell($(this).closest('td, li')).index();
        inspeccion.items.inspeccionatributos[tr.row].resultado_ia = resultado_ia
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

    inspeccion.pruebasyoensayos();
    inspeccion.inspecciondimensiones();
    inspeccion.inspeccionatributos();
});
