var tblProduccion;

var desarrollo = {
    items: {
        producto: '',
        ciclo: '',
        solicitado_por: '',
        fecha_limite_entrega: '',
        cantidad: 0,
        tipo_empaque: '',
        maquina: '',
        objetivo_muestra: '',
        molde_nuevo: '',
        es_funcional: '',
        diseño: '',
        variables: '',
        peso_solicitado: '',
        observaciones: '',
        color: '',
        muestras: '',
        autorizacion: '',
        produccion: [],
    },
    calculo_total:function () {
        $.each(this.items.produccion, function (pos, dict) {
            dict.motivos = [];
            if (dict.mp >= 0) {
                dict.motivos.push(parseFloat(dict.mp))
            }
            if (dict.pigmentos >= 0) {
                dict.motivos.push(parseFloat(dict.pigmentos))
            }
            if (dict.empaque >= 0) {
                dict.motivos.push(parseFloat(dict.empaque))
            }
            if (dict.maquila >= 0) {
                dict.motivos.push(parseFloat(dict.maquila))
            }
            if (dict.operario >= 0) {
                dict.motivos.push(parseFloat(dict.operario))
            }
            if (dict.tecnico >= 0) {
                dict.motivos.push(parseFloat(dict.tecnico))
            }
            if (dict.montaje >= 0) {
                dict.motivos.push(parseFloat(dict.montaje))
            }

            var i = 0, sumn = 0, arrayLen = dict.motivos.length;
            while (i < arrayLen) {
                sumn = sumn + dict.motivos[i++];
            }

            dict.suma_total = sumn

        });
    },
    produccion: function () {
        tblProduccion = $('#tblProduccion').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.produccion,
            columns: [
                { "data": "especificacion" },
                { "data": "mp" },
                { "data": "pigmentos" },
                { "data": "empaque" },
                { "data": "maquila" },
                { "data": "operario" },
                { "data": "tecnico" },
                { "data": "montaje" },
                { "data": "total" },
            ],
            columnDefs: [
                {
                    targets: [0, 1, 2, 3, 4, 5, 6, 7, 8],
                    class: 'text-center',
                },
                {
                    targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="mp" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.mp + '">';
                    }
                },
                {
                    targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="pigmentos" class="form-control form-control-sm input-sm" autocopigmentoslete="off" value="' + row.pigmentos + '">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="empaque" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.empaque + '">';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="maquila" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.maquila + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="operario" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.operario + '">';
                    }
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="tecnico" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.tecnico + '">';
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="number" name="montaje" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.montaje + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 0.00;
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

            },
            initComplete: function (settings, json) {

            }
        });
    },
};

$(function () {

    //Evento: eliminar motivos
    $('#tblProduccion tbody').on('change', 'input[name="mp"]', function () {
        var mp = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].mp = mp;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="pigmentos"]', function () {
        var pigmentos = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].pigmentos = pigmentos;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="empaque"]', function () {
        var empaque = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].empaque = empaque;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="maquila"]', function () {
        var maquila = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].maquila = maquila;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="operario"]', function () {
        var operario = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].operario = operario;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="tecnico"]', function () {
        var tecnico = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].tecnico = tecnico;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    }).on('change', 'input[name="montaje"]', function () {
        var montaje = $(this).val();
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        desarrollo.items.produccion[tr.row].montaje = montaje;
        desarrollo.calculo_total()
        $('td:eq(8)', tblProduccion.row(tr.row).node()).html(desarrollo.items.produccion[tr.row].suma_total)
    });

    //Guardado de datos
    $('#formControl').on('submit', function(e){
        e.preventDefault();

        desarrollo.items.producto = $('input[name="producto"]').val();
        desarrollo.items.fecha_limite_entrega = $('input[name="fecha_limite_entrega"]').val();
        desarrollo.items.cantidad = $('input[name="cantidad"]').val();
        desarrollo.items.ciclo = $('input[name="ciclo"]').val();
        desarrollo.items.tipo_empaque = $('input[name="tipo_empaque"]').val();
        desarrollo.items.solicitado_por = $('input[name="solicitado_por"]').val();
        desarrollo.items.color = $('input[name="color"]').val();
        desarrollo.items.peso_solicitado = $('input[name="peso_solicitado"]').val();
        desarrollo.items.molde_nuevo = $('select[name="molde_nuevo"]').val();
        desarrollo.items.es_funcional = $('select[name="es_funcional"]').val();
        desarrollo.items.diseño = $('select[name="diseño"]').val();
        desarrollo.items.variables = $('select[name="variables"]').val();
        desarrollo.items.maquina = $('select[name="maquina"]').val();
        desarrollo.items.autorizacion = $('select[name="autorizacion"]').val();
        desarrollo.items.objetivo_muestra = $('textarea[name="objetivo_muestra"]').val();
        desarrollo.items.observaciones = $('textarea[name="observaciones"]').val();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('desarrollo', JSON.stringify(desarrollo.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Control_produccion/Control_orden/';
        });
    });

    // Inicializar tablas
    desarrollo.produccion();

});