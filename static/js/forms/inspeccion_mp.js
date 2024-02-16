var tblAnalisis;
var tblDimensional;

var inspeccion = {
    items: {
        arte_cliente:'',
        unidades_muestra: '',
        proveedor:'',
        arte_ingreso: '',
        unidades_empaque: '',
        certificado: '',
        especificaciones: '',
        observaciones: '',
        revisado_por: '',
        aprobado: '',
        tolerado: '',
        estado: '',
        lote_ingreso: '',
        analisis: [],
        dimensional: [],
    },

    analisis: function () {
        tblAnalisis = $('#tblAnalisis').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            pageLength: 25,
            data: this.items.analisis,
            columns: [
                { "data": "especificacion" },
                { "data": "cumple" },
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '\
                        <select name="cumple" id="cumple" class="form-control form-control-sm input-sm">\
                        <option value="-------">-------</option>\
                        <option value="No aplica">No aplica</option>\
                        <option value="Cumple">Cumple</option>\
                        <option value="No cumple">No cumple</option>\
                        </select>\
                        '
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

            },
            initComplete: function (settings, json) {

            }
        });
    },

    dimensional: function () {
        tblDimensional = $('#tblDimensional').DataTable({
            destroy: true,
            ordering: false,
            scrollX: true,
            info: false,
            paging: false,
            searching: false,
            data: this.items.dimensional,
            columns: [
                { "data": "especificacion" },
                { "data": "muestra_1" },
                { "data": "muestra_2" },
                { "data": "muestra_3" },
                { "data": "muestra_4" },
                { "data": "muestra_5" },
                { "data": "muestra_6" },
                { "data": "muestra_7" },
                { "data": "muestra_8" },
                { "data": "muestra_9" },
                { "data": "muestra_10" },
                { "data": "muestra_11" },
                { "data": "muestra_12" },
                { "data": "muestra_13" },
                { "data": "cumple" },
            ],
            columnDefs: [
                {
                    targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_1" class="form-control form-control-sm input-sm" value="' + row.muestra_1 + '">';
                    }
                },
                {
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_2" class="form-control form-control-sm input-sm" value="' + row.muestra_2 + '">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_3" class="form-control form-control-sm input-sm" value="' + row.muestra_3 + '">';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_4" class="form-control form-control-sm input-sm" value="' + row.muestra_4 + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_5" class="form-control form-control-sm input-sm" value="' + row.muestra_5 + '">';
                    }
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_6" class="form-control form-control-sm input-sm" value="' + row.muestra_6 + '">';
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_7" class="form-control form-control-sm input-sm" value="' + row.muestra_7 + '">';
                    }
                },
                {
                    targets: [8],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_8" class="form-control form-control-sm input-sm" value="' + row.muestra_8 + '">';
                    }
                },
                {
                    targets: [9],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_9" class="form-control form-control-sm input-sm" value="' + row.muestra_9 + '">';
                    }
                },
                {
                    targets: [10],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_10" class="form-control form-control-sm input-sm" value="' + row.muestra_10 + '">';
                    }
                },
                {
                    targets: [11],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_11" class="form-control form-control-sm input-sm" value="' + row.muestra_11 + '">';
                    }
                },
                {
                    targets: [12],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_12" class="form-control form-control-sm input-sm" value="' + row.muestra_12 + '">';
                    }
                },
                {
                    targets: [13],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="muestra_13" class="form-control form-control-sm input-sm" value="' + row.muestra_12 + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '\
                        <select name="cumple" id="cumple" class="form-control form-control-sm input-sm">\
                        <option value="-------">-------</option>\
                        <option value="No aplica">No aplica</option>\
                        <option value="Cumple">Cumple</option>\
                        <option value="No cumple">No cumple</option>\
                        </select>\
                        '
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="muestra_1"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_2"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_3"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_4"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_5"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_6"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_7"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_8"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_9"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_10"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_11"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_12"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="muestra_13"]').TouchSpin({
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
};

$(function () {

    //Eventos: muestras, especificación y cumple de dimensiones
    $('#tblAnalisis tbody').on('change', 'select[name="cumple"]', function () {
        var cumple = ($(this).val());
        var tr = tblAnalisis.cell($(this).closest('td, li')).index();
        inspeccion.items.analisis[tr.row].cumple = cumple
    });

    $('#id_certificado').on('change', function () {
        var certificado = ($(this).val());
        console.log(certificado)
    })

    //Eventos: muestras, especificación y cumple de dimensiones
    $('#tblDimensional tbody').on('change', 'input[name="muestra_1"]', function () {
        var muestra_1 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_1 = muestra_1
    }).on('change', 'input[name="muestra_2"]', function () {
        var muestra_2 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_2 = muestra_2
    }).on('change', 'input[name="muestra_3"]', function () {
        var muestra_3 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_3 = muestra_3
    }).on('change', 'input[name="muestra_4"]', function () {
        var muestra_4 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_4 = muestra_4
    }).on('change', 'input[name="muestra_5"]', function () {
        var muestra_5 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_5 = muestra_5
    }).on('change', 'input[name="muestra_6"]', function () {
        var muestra_6 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_6 = muestra_6
    }).on('change', 'input[name="muestra_7"]', function () {
        var muestra_7 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_7 = muestra_7
    }).on('change', 'input[name="muestra_8"]', function () {
        var muestra_8 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_8 = muestra_8
    }).on('change', 'input[name="muestra_9"]', function () {
        var muestra_9 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_9 = muestra_9
    }).on('change', 'input[name="muestra_10"]', function () {
        var muestra_10 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_10 = muestra_10
    }).on('change', 'input[name="muestra_11"]', function () {
        var muestra_11 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_11 = muestra_11
    }).on('change', 'input[name="muestra_12"]', function () {
        var muestra_12 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_12 = muestra_12
    }).on('change', 'input[name="muestra_13"]', function () {
        var muestra_13 = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].muestra_13 = muestra_13
    }).on('change', 'select[name="cumple"]', function () {
        var cumple = ($(this).val());
        var tr = tblDimensional.cell($(this).closest('td, li')).index();
        inspeccion.items.dimensional[tr.row].cumple = cumple
    });

    //Guardado de datos
    $('form').on('submit', function(e){
        e.preventDefault();

        inspeccion.items.arte_cliente = $('input[name="arte_cliente"]').val();
        inspeccion.items.unidades_muestra = $('input[name="unidades_muestra"]').val();
        inspeccion.items.proveedor = $('input[name="proveedor"]').val();
        inspeccion.items.arte_ingreso = $('input[name="arte_ingreso"]').val();
        inspeccion.items.unidades_empaque = $('input[name="unidades_empaque"]').val();
        inspeccion.items.certificado = $('select[name="certificado"]').val();
        inspeccion.items.especificaciones = $('select[name="especificaciones"]').val();
        inspeccion.items.revisado_por = $('input[name="revisado_por"]').val();
        inspeccion.items.aprobado = $('select[name="aprobado"]').val();
        inspeccion.items.tolerado = $('select[name="tolerado"]').val();
        inspeccion.items.estado = $('select[name="estado"]').val();
        inspeccion.items.lote_ingreso = $('select[name="lote_ingreso"]').val();
        inspeccion.items.observaciones = $('textarea[name="observaciones"]').val();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('inspeccion', JSON.stringify(inspeccion.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Control_calidad/Inspecciones_calidad/';
        });
    });

    inspeccion.dimensional();
    inspeccion.analisis();
});
