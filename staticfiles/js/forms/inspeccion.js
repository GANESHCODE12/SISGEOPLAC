var tblPruebasEnsayos;
var tblInspeccionDimensiones;
var tblInspeccionAtributos;
var tblColaboradores;

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

var inspeccion = {
    items: {
        numero_op:'',
        turno: '',
        observaciones:'',
        colaborador: [],
        pruebasensayos: [],
        inspecciondimensiones: [],
        inspeccionatributos: [],
    },

    calculo_promedio_pruebas: function() {
        $.each(this.items.pruebasensayos, function (pos, dict) {
            dict.cavidades_pruebas = [];
            if (dict.cavidad_1 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_1))
            } 
            if (dict.cavidad_2 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_2))
            } 
            if (dict.cavidad_3 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_3))
            } 
            if (dict.cavidad_4 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_4))
            } 
            if (dict.cavidad_5 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_5))
            } 
            if (dict.cavidad_6 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_6))
            } 
            if (dict.cavidad_7 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_7))
            } 
            if (dict.cavidad_8 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_8))
            } 
            if (dict.cavidad_9 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_9))
            } 
            if (dict.cavidad_10 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_10))
            } 
            if (dict.cavidad_11 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_11))
            } 
            if (dict.cavidad_12 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_12))
            } 
            if (dict.cavidad_13 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_13))
            } 
            if (dict.cavidad_14 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_14))
            } 
            if (dict.cavidad_15 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_15))
            } 
            if (dict.cavidad_16 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_16))
            } 
            if (dict.cavidad_17 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_17))
            } 
            if (dict.cavidad_18 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_18))
            } 
            if (dict.cavidad_19 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_19))
            } 
            if (dict.cavidad_20 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_20))
            } 
            if (dict.cavidad_21 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_21))
            } 
            if (dict.cavidad_22 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_22))
            } 
            if (dict.cavidad_23 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_23))
            } 
            if (dict.cavidad_24 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_24))
            } 
            if (dict.cavidad_25 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_25))
            } 
            if (dict.cavidad_26 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_26))
            } 
            if (dict.cavidad_27 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_27))
            } 
            if (dict.cavidad_28 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_28))
            } 
            if (dict.cavidad_29 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_29))
            } 
            if (dict.cavidad_30 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_30))
            } 
            if (dict.cavidad_31 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_31))
            } 
            if (dict.cavidad_32 >= 0) {
                dict.cavidades_pruebas.push(parseFloat(dict.cavidad_32))
            }

            var i = 0, sumn = 0, arrayLen = dict.cavidades_pruebas.length;
            while (i < arrayLen) {
                sumn = sumn + dict.cavidades_pruebas[i++];
            }

            var promedio = sumn / arrayLen

            dict.valor_p = promedio.toFixed(2)

            if (
                dict.valor + dict.tolerancia_p >= dict.valor_p & 
                dict.valor - dict.tolerancia_p <= dict.valor_p
            ) {
                dict.resultado_p = "Conforme"
            } else {
                dict.resultado_p = "No conforme"
            }

        });
    },

    calculo_promedio_dimensiones: function() {
        $.each(this.items.inspecciondimensiones, function (pos, dict) {
            dict.cavidades_dimensiones = [];
            if (dict.cavidad_1 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_1))
            } 
            if (dict.cavidad_2 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_2))
            } 
            if (dict.cavidad_3 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_3))
            } 
            if (dict.cavidad_4 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_4))
            } 
            if (dict.cavidad_5 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_5))
            } 
            if (dict.cavidad_6 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_6))
            } 
            if (dict.cavidad_7 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_7))
            } 
            if (dict.cavidad_8 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_8))
            } 
            if (dict.cavidad_9 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_9))
            } 
            if (dict.cavidad_10 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_10))
            } 
            if (dict.cavidad_11 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_11))
            } 
            if (dict.cavidad_12 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_12))
            } 
            if (dict.cavidad_13 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_13))
            } 
            if (dict.cavidad_14 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_14))
            } 
            if (dict.cavidad_15 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_15))
            } 
            if (dict.cavidad_16 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_16))
            } 
            if (dict.cavidad_17 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_17))
            } 
            if (dict.cavidad_18 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_18))
            } 
            if (dict.cavidad_19 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_19))
            } 
            if (dict.cavidad_20 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_20))
            } 
            if (dict.cavidad_21 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_21))
            } 
            if (dict.cavidad_22 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_22))
            } 
            if (dict.cavidad_23 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_23))
            } 
            if (dict.cavidad_24 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_24))
            } 
            if (dict.cavidad_25 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_25))
            } 
            if (dict.cavidad_26 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_26))
            } 
            if (dict.cavidad_27 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_27))
            } 
            if (dict.cavidad_28 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_28))
            } 
            if (dict.cavidad_29 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_29))
            } 
            if (dict.cavidad_30 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_30))
            } 
            if (dict.cavidad_31 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_31))
            } 
            if (dict.cavidad_32 >= 0) {
                dict.cavidades_dimensiones.push(parseFloat(dict.cavidad_32))
            }

            var i = 0, sumn = 0, arrayLen = dict.cavidades_dimensiones.length;
            while (i < arrayLen) {
                sumn = sumn + dict.cavidades_dimensiones[i++];
            }

            var promedio = sumn / arrayLen

            dict.promedio = promedio.toFixed(2)

            if (
                dict.valor_nominal + dict.tolerancia_d >= dict.promedio & 
                dict.valor_nominal - dict.tolerancia_d <= dict.promedio
            ) {
                dict.resultado_id = "Conforme"
            } else {
                dict.resultado_id = "No conforme"
            }

        });
    },

    get_ids: function () {
        var ids = [];
        $.each(this.items.colaborador, function (key, value) {
            ids.push(value.id);
        });
        return ids;
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
    pruebasyoensayos: function () {
        tblPruebasEnsayos = $('#tblPruebasEnsayos').DataTable({
            destroy: true,
            ordering: false,
            scrollX: true,
            info: false,
            paging: false,
            searching: false,
            data: this.items.pruebasensayos,
            columns: [
                { "data": "text" },
                { "data": "valor" },
                { "data": "tolerancia_p" },
                { "data": "cavidad_1" },
                { "data": "cavidad_2" },
                { "data": "cavidad_3" },
                { "data": "cavidad_4" },
                { "data": "cavidad_5" },
                { "data": "cavidad_6" },
                { "data": "cavidad_7" },
                { "data": "cavidad_8" },
                { "data": "cavidad_9" },
                { "data": "cavidad_10" },
                { "data": "cavidad_11" },
                { "data": "cavidad_12" },
                { "data": "cavidad_13" },
                { "data": "cavidad_14" },
                { "data": "cavidad_15" },
                { "data": "cavidad_16" },
                { "data": "cavidad_17" },
                { "data": "cavidad_18" },
                { "data": "cavidad_19" },
                { "data": "cavidad_20" },
                { "data": "cavidad_21" },
                { "data": "cavidad_22" },
                { "data": "cavidad_23" },
                { "data": "cavidad_24" },
                { "data": "cavidad_25" },
                { "data": "cavidad_26" },
                { "data": "cavidad_27" },
                { "data": "cavidad_28" },
                { "data": "cavidad_29" },
                { "data": "cavidad_30" },
                { "data": "cavidad_31" },
                { "data": "cavidad_32" },
                { "data": "valor_p" },
                { "data": "resultado_p" },
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_1" class="form-control form-control-sm input-sm" value="' + row.cavidad_1 + '">';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_2" class="form-control form-control-sm input-sm" value="' + row.cavidad_2 + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_3" class="form-control form-control-sm input-sm" value="' + row.cavidad_3 + '">';
                    }
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_4" class="form-control form-control-sm input-sm" value="' + row.cavidad_4 + '">';
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_5" class="form-control form-control-sm input-sm" value="' + row.cavidad_5 + '">';
                    }
                },
                {
                    targets: [8],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_6" class="form-control form-control-sm input-sm" value="' + row.cavidad_6 + '">';
                    }
                },
                {
                    targets: [9],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_7" class="form-control form-control-sm input-sm" value="' + row.cavidad_7 + '">';
                    }
                },
                {
                    targets: [10],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_8" class="form-control form-control-sm input-sm" value="' + row.cavidad_8 + '">';
                    }
                },
                {
                    targets: [11],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_9" class="form-control form-control-sm input-sm" value="' + row.cavidad_9 + '">';
                    }
                },
                {
                    targets: [12],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_10" class="form-control form-control-sm input-sm" value="' + row.cavidad_10 + '">';
                    }
                },
                {
                    targets: [13],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_11" class="form-control form-control-sm input-sm" value="' + row.cavidad_11 + '">';
                    }
                },
                {
                    targets: [14],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_12" class="form-control form-control-sm input-sm" value="' + row.cavidad_12 + '">';
                    }
                },
                {
                    targets: [15],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_13" class="form-control form-control-sm input-sm" value="' + row.cavidad_13 + '">';
                    }
                },
                {
                    targets: [16],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_14" class="form-control form-control-sm input-sm" value="' + row.cavidad_14 + '">';
                    }
                },
                {
                    targets: [17],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_15" class="form-control form-control-sm input-sm" value="' + row.cavidad_15 + '">';
                    }
                },
                {
                    targets: [18],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_16" class="form-control form-control-sm input-sm" value="' + row.cavidad_16 + '">';
                    }
                },
                {
                    targets: [19],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_17" class="form-control form-control-sm input-sm" value="' + row.cavidad_17 + '">';
                    }
                },
                {
                    targets: [20],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_18" class="form-control form-control-sm input-sm" value="' + row.cavidad_18 + '">';
                    }
                },
                {
                    targets: [21],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_19" class="form-control form-control-sm input-sm" value="' + row.cavidad_19 + '">';
                    }
                },
                {
                    targets: [22],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_20" class="form-control form-control-sm input-sm" value="' + row.cavidad_20 + '">';
                    }
                },
                {
                    targets: [23],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_21" class="form-control form-control-sm input-sm" value="' + row.cavidad_21 + '">';
                    }
                },
                {
                    targets: [24],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_22" class="form-control form-control-sm input-sm" value="' + row.cavidad_22 + '">';
                    }
                },
                {
                    targets: [25],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_23" class="form-control form-control-sm input-sm" value="' + row.cavidad_23 + '">';
                    }
                },
                {
                    targets: [26],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_24" class="form-control form-control-sm input-sm" value="' + row.cavidad_24 + '">';
                    }
                },
                {
                    targets: [27],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_25" class="form-control form-control-sm input-sm" value="' + row.cavidad_25 + '">';
                    }
                },
                {
                    targets: [28],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_26" class="form-control form-control-sm input-sm" value="' + row.cavidad_26 + '">';
                    }
                },
                {
                    targets: [29],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_27" class="form-control form-control-sm input-sm" value="' + row.cavidad_27 + '">';
                    }
                },
                {
                    targets: [30],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_28" class="form-control form-control-sm input-sm" value="' + row.cavidad_28 + '">';
                    }
                },
                {
                    targets: [31],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_29" class="form-control form-control-sm input-sm" value="' + row.cavidad_29 + '">';
                    }
                },
                {
                    targets: [32],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_30" class="form-control form-control-sm input-sm" value="' + row.cavidad_30 + '">';
                    }
                },
                {
                    targets: [33],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_31" class="form-control form-control-sm input-sm" value="' + row.cavidad_31 + '">';
                    }
                },
                {
                    targets: [34],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_32" class="form-control form-control-sm input-sm" value="' + row.cavidad_32 + '">';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 0.00;
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cavidad_1"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_2"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_3"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_4"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_5"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_6"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_7"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_8"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_9"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_10"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_11"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_12"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_13"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_14"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_15"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_16"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_17"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_18"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_19"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_20"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_21"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_22"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_23"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_24"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_25"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_26"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_27"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_28"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_29"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_30"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_31"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_32"]').TouchSpin({
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
            destroy: true,
            ordering: false,
            scrollX: true,
            info: false,
            paging: false,
            searching: false,
            data: this.items.inspecciondimensiones,
            columns: [
                { "data": "text" },
                { "data": "valor_nominal" },
                { "data": "tolerancia_d" },
                { "data": "cavidad_1" },
                { "data": "cavidad_2" },
                { "data": "cavidad_3" },
                { "data": "cavidad_4" },
                { "data": "cavidad_5" },
                { "data": "cavidad_6" },
                { "data": "cavidad_7" },
                { "data": "cavidad_8" },
                { "data": "cavidad_9" },
                { "data": "cavidad_10" },
                { "data": "cavidad_11" },
                { "data": "cavidad_12" },
                { "data": "cavidad_13" },
                { "data": "cavidad_14" },
                { "data": "cavidad_15" },
                { "data": "cavidad_16" },
                { "data": "cavidad_17" },
                { "data": "cavidad_18" },
                { "data": "cavidad_19" },
                { "data": "cavidad_20" },
                { "data": "cavidad_21" },
                { "data": "cavidad_22" },
                { "data": "cavidad_23" },
                { "data": "cavidad_24" },
                { "data": "cavidad_25" },
                { "data": "cavidad_26" },
                { "data": "cavidad_27" },
                { "data": "cavidad_28" },
                { "data": "cavidad_29" },
                { "data": "cavidad_30" },
                { "data": "cavidad_31" },
                { "data": "cavidad_32" },
                { "data": "promedio" },
                { "data": "resultado_id" },
            ],
            columnDefs: [
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 0.00;
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_1" class="form-control form-control-sm input-sm" value="' + row.cavidad_1 + '">';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_2" class="form-control form-control-sm input-sm" value="' + row.cavidad_2 + '">';
                    }
                },
                {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_3" class="form-control form-control-sm input-sm" value="' + row.cavidad_3 + '">';
                    }
                },
                {
                    targets: [6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_4" class="form-control form-control-sm input-sm" value="' + row.cavidad_4 + '">';
                    }
                },
                {
                    targets: [7],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_5" class="form-control form-control-sm input-sm" value="' + row.cavidad_5 + '">';
                    }
                },
                {
                    targets: [8],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_6" class="form-control form-control-sm input-sm" value="' + row.cavidad_6 + '">';
                    }
                },
                {
                    targets: [9],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_7" class="form-control form-control-sm input-sm" value="' + row.cavidad_7 + '">';
                    }
                },
                {
                    targets: [10],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_8" class="form-control form-control-sm input-sm" value="' + row.cavidad_8 + '">';
                    }
                },
                {
                    targets: [11],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_9" class="form-control form-control-sm input-sm" value="' + row.cavidad_9 + '">';
                    }
                },
                {
                    targets: [12],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_10" class="form-control form-control-sm input-sm" value="' + row.cavidad_10 + '">';
                    }
                },
                {
                    targets: [13],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_11" class="form-control form-control-sm input-sm" value="' + row.cavidad_11 + '">';
                    }
                },
                {
                    targets: [14],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_12" class="form-control form-control-sm input-sm" value="' + row.cavidad_12 + '">';
                    }
                },
                {
                    targets: [15],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_13" class="form-control form-control-sm input-sm" value="' + row.cavidad_13 + '">';
                    }
                },
                {
                    targets: [16],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_14" class="form-control form-control-sm input-sm" value="' + row.cavidad_14 + '">';
                    }
                },
                {
                    targets: [17],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_15" class="form-control form-control-sm input-sm" value="' + row.cavidad_15 + '">';
                    }
                },
                {
                    targets: [18],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_16" class="form-control form-control-sm input-sm" value="' + row.cavidad_16 + '">';
                    }
                },
                {
                    targets: [19],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_17" class="form-control form-control-sm input-sm" value="' + row.cavidad_17 + '">';
                    }
                },
                {
                    targets: [20],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_18" class="form-control form-control-sm input-sm" value="' + row.cavidad_18 + '">';
                    }
                },
                {
                    targets: [21],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_19" class="form-control form-control-sm input-sm" value="' + row.cavidad_19 + '">';
                    }
                },
                {
                    targets: [22],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_20" class="form-control form-control-sm input-sm" value="' + row.cavidad_20 + '">';
                    }
                },
                {
                    targets: [23],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_21" class="form-control form-control-sm input-sm" value="' + row.cavidad_21 + '">';
                    }
                },
                {
                    targets: [24],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_22" class="form-control form-control-sm input-sm" value="' + row.cavidad_22 + '">';
                    }
                },
                {
                    targets: [25],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_23" class="form-control form-control-sm input-sm" value="' + row.cavidad_23 + '">';
                    }
                },
                {
                    targets: [26],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_24" class="form-control form-control-sm input-sm" value="' + row.cavidad_24 + '">';
                    }
                },
                {
                    targets: [27],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_25" class="form-control form-control-sm input-sm" value="' + row.cavidad_25 + '">';
                    }
                },
                {
                    targets: [28],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_26" class="form-control form-control-sm input-sm" value="' + row.cavidad_26 + '">';
                    }
                },
                {
                    targets: [29],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_27" class="form-control form-control-sm input-sm" value="' + row.cavidad_27 + '">';
                    }
                },
                {
                    targets: [30],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_28" class="form-control form-control-sm input-sm" value="' + row.cavidad_28 + '">';
                    }
                },
                {
                    targets: [31],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_29" class="form-control form-control-sm input-sm" value="' + row.cavidad_29 + '">';
                    }
                },
                {
                    targets: [32],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_30" class="form-control form-control-sm input-sm" value="' + row.cavidad_30 + '">';
                    }
                },
                {
                    targets: [33],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_31" class="form-control form-control-sm input-sm" value="' + row.cavidad_31 + '">';
                    }
                },
                {
                    targets: [34],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cavidad_32" class="form-control form-control-sm input-sm" value="' + row.cavidad_32 + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '';
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cavidad_1"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_2"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_3"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_4"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_5"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_6"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_7"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_8"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_9"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_10"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_11"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_12"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_13"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_14"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_15"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_16"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_17"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_18"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_19"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_20"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_21"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_22"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_23"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_24"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_25"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_26"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_27"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_28"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_29"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_30"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_31"]').TouchSpin({
                    min: 0,
                    max: 1000000000,
                    decimals: 2,
                    step: 0.01
                })
                $(row).find('input[name="cavidad_32"]').TouchSpin({
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
                    ids: JSON.stringify(inspeccion.get_ids())
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
        inspeccion.items.colaborador.push(data);
        inspeccion.colaborador();
        $(this).val('').trigger('change.select2');
    });
    //Evento: eliminar colaboradores
    $('#tblColaboradores tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblColaboradores.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar al colaborador de la inspección de calidad?', function () {
            inspeccion.items.colaborador.splice(tr.row, 1);
            inspeccion.colaborador();
        });
    });
    //Eventos: resultado y valor de pruebas
    $('#tblPruebasEnsayos tbody').on('change', 'input[name="cavidad_1"]', function () {
        var cavidad_1 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_1 = cavidad_1
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_2"]', function () {
        var cavidad_2 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_2 = cavidad_2
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_3"]', function () {
        var cavidad_3 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_3 = cavidad_3
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_4"]', function () {
        var cavidad_4 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_4 = cavidad_4
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_5"]', function () {
        var cavidad_5 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_5 = cavidad_5
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_6"]', function () {
        var cavidad_6 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_6 = cavidad_6
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_7"]', function () {
        var cavidad_7 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_7 = cavidad_7
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_8"]', function () {
        var cavidad_8 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_8 = cavidad_8
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_9"]', function () {
        var cavidad_9 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_9 = cavidad_9
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_10"]', function () {
        var cavidad_10 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_10 = cavidad_10
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_11"]', function () {
        var cavidad_11 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_11 = cavidad_11
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_12"]', function () {
        var cavidad_12 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_12 = cavidad_12
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_13"]', function () {
        var cavidad_13 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_13 = cavidad_13
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_14"]', function () {
        var cavidad_14 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_14 = cavidad_14
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_15"]', function () {
        var cavidad_15 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_15 = cavidad_15
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_16"]', function () {
        var cavidad_16 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_16 = cavidad_16
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_17"]', function () {
        var cavidad_17 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_17 = cavidad_17
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_18"]', function () {
        var cavidad_18 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_18 = cavidad_18
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_19"]', function () {
        var cavidad_19 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_19 = cavidad_19
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_20"]', function () {
        var cavidad_20 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_20 = cavidad_20
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_21"]', function () {
        var cavidad_21 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_21 = cavidad_21
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_22"]', function () {
        var cavidad_22 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_22 = cavidad_22
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_23"]', function () {
        var cavidad_23 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_23 = cavidad_23
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_24"]', function () {
        var cavidad_24 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_24 = cavidad_24
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_25"]', function () {
        var cavidad_25 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_25 = cavidad_25
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_26"]', function () {
        var cavidad_26 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_26 = cavidad_26
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_27"]', function () {
        var cavidad_27 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_27 = cavidad_27
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_28"]', function () {
        var cavidad_28 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_28 = cavidad_28
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_29"]', function () {
        var cavidad_29 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_29 = cavidad_29
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_30"]', function () {
        var cavidad_30 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_30 = cavidad_30
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_31"]', function () {
        var cavidad_31 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_31 = cavidad_31
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    }).on('change', 'input[name="cavidad_32"]', function () {
        var cavidad_32 = ($(this).val());
        var tr = tblPruebasEnsayos.cell($(this).closest('td, li')).index();
        inspeccion.items.pruebasensayos[tr.row].cavidad_32 = cavidad_32
        inspeccion.calculo_promedio_pruebas()
        $('td:eq(35)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].valor_p)
        $('td:eq(36)', tblPruebasEnsayos.row(tr.row).node()).html(inspeccion.items.pruebasensayos[tr.row].resultado_p)
    });

    //Evento: resultado y promedio de dimensiones
    $('#tblInspeccionDimensiones tbody').on('change', 'input[name="cavidad_1"]', function () {
        var cavidad_1 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_1 = cavidad_1
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_2"]', function () {
        var cavidad_2 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_2 = cavidad_2
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_3"]', function () {
        var cavidad_3 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_3 = cavidad_3
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_4"]', function () {
        var cavidad_4 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_4 = cavidad_4
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_5"]', function () {
        var cavidad_5 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_5 = cavidad_5
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_6"]', function () {
        var cavidad_6 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_6 = cavidad_6
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_7"]', function () {
        var cavidad_7 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_7 = cavidad_7
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_8"]', function () {
        var cavidad_8 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_8 = cavidad_8
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_9"]', function () {
        var cavidad_9 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_9 = cavidad_9
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_10"]', function () {
        var cavidad_10 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_10 = cavidad_10
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_11"]', function () {
        var cavidad_11 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_11 = cavidad_11
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_12"]', function () {
        var cavidad_12 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_12 = cavidad_12
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_13"]', function () {
        var cavidad_13 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_13 = cavidad_13
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_14"]', function () {
        var cavidad_14 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_14 = cavidad_14
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_15"]', function () {
        var cavidad_15 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_15 = cavidad_15
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_16"]', function () {
        var cavidad_16 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_16 = cavidad_16
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_17"]', function () {
        var cavidad_17 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_17 = cavidad_17
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_18"]', function () {
        var cavidad_18 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_18 = cavidad_18
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_19"]', function () {
        var cavidad_19 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_19 = cavidad_19
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_20"]', function () {
        var cavidad_20 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_20 = cavidad_20
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_21"]', function () {
        var cavidad_21 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_21 = cavidad_21
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_22"]', function () {
        var cavidad_22 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_22 = cavidad_22
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_23"]', function () {
        var cavidad_23 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_23 = cavidad_23
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_24"]', function () {
        var cavidad_24 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_24 = cavidad_24
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_25"]', function () {
        var cavidad_25 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_25 = cavidad_25
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_26"]', function () {
        var cavidad_26 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_26 = cavidad_26
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_27"]', function () {
        var cavidad_27 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_27 = cavidad_27
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_28"]', function () {
        var cavidad_28 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_28 = cavidad_28
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_29"]', function () {
        var cavidad_29 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_29 = cavidad_29
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_30"]', function () {
        var cavidad_30 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_30 = cavidad_30
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_31"]', function () {
        var cavidad_31 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_31 = cavidad_31
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    }).on('change', 'input[name="cavidad_32"]', function () {
        var cavidad_32 = ($(this).val());
        var tr = tblInspeccionDimensiones.cell($(this).closest('td, li')).index();
        inspeccion.items.inspecciondimensiones[tr.row].cavidad_32 = cavidad_32
        inspeccion.calculo_promedio_dimensiones()
        $('td:eq(35)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].promedio)
        $('td:eq(36)', tblInspeccionDimensiones.row(tr.row).node()).html(inspeccion.items.inspecciondimensiones[tr.row].resultado_id)
    });

    //Evento: resultado de atributos
    $('#tblInspeccionAtributos tbody').on('change', 'input[name="resultado_ia"]', function () {
        var resultado_ia = ($(this).val());
        var tr = tblInspeccionAtributos.cell($(this).closest('td, li')).index();
        inspeccion.items.inspeccionatributos[tr.row].resultado_ia = resultado_ia
    });


    //Guardado de datos
    $('form').on('submit', function(e){
        e.preventDefault();

        inspeccion.items.numero_op = $('input[name="numero_op_id"]').val();
        inspeccion.items.turno = $('select[name="turno"]').val();
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
    inspeccion.colaborador();
});
