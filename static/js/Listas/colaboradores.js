var tblColaboradores;

$(function () {
    tblColaboradores = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "full_name" },
            { "data": "numero_documento" },
            { "data": "telefono_contacto" },
            { "data": "proceso" },
            { "data": "nombre_emergencia" },
            { "data": "parentezco" },
            { "data": "telefono_emergencia" },
            { "data": "id" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-2],
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Gestión_humana/Proceso_disciplinario/' + row.id + '"><span class="badge badge-primary" style="width: auto">' + 'Proceso disciplinario' + '</span></a><br>';
                    buttons += '<a href="/Gestión_humana/examenes-medicos/' + row.id + '"><span class="badge badge-primary">' + 'Examenes medicos' + '</span></a><br>';
                    buttons += '<a href="/Gestión_humana/capacitacion/' + row.id + '"><span class="badge badge-primary">' + 'Capacitación' + '</span></a><br>';
                    buttons += '<a href="/Gestión_humana/entrega-dotacion/' + row.id + '"><span class="badge badge-primary">' + 'Dotación' + '</span></a><br>';
                    buttons += '<a href="/Gestión_humana/Otro_si/' + row.id + '/"><span class="badge badge-primary">' + 'Otro si' + '</span></a><br>';
                    return buttons;
                }
            },
            {
                targets: [-1],
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Gestión_humana/Actualizar_colaborador/' + row.id + '"><button title="Otro Si" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-user"></i></button></a> ';
                    buttons += '<a rel="details_otro_si"><button title="Otro Si" class="btn btn-info btn-xs btn-flat"><i class="fas fa-folder"></i></button></a> ';
                    buttons += '<a rel="examenes_medicos"><button title="Exámenes médicos" class="btn btn-info btn-xs btn-flat"><i class="fas fa-stethoscope"></i></button></a> ';
                    buttons += '<a rel="capacitacion"><button title="Capacitación" class="btn btn-info btn-xs btn-flat"><i class="fas fa-handshake"></i></button></a> ';
                    buttons += '<a rel="dotacion"><button title="Dotación" class="btn btn-info btn-xs btn-flat"><i class="fas fa-hard-hat"></i></button></a> ';
                    buttons += '<a rel="details_Procesos"><button title="Procesos Disciplinarios" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-gavel"></i></button></a>';
                    return buttons;
                }
            },
            {
                targets: [0],
                render: function (data, type, row) {
                    var buttons = '<a href="/Gestión_humana/Colaborador/' + row.id + '">' + row.full_name + '</a><br>';
                    return buttons;
                }
            },
            {
                targets: [0, 1, 2, 3, 4, 5, 6],
                class: 'text-center',
            },
        ],
        initComplete: function (settings, json) {

        }
    });
    $('#data tbody')
        .on('click', 'a[rel=details_otro_si]', function () {
            var tr = tblColaboradores.cell($(this).closest('td, li')).index();
            var data = tblColaboradores.row(tr.row).data();

            $('#tblDetOtroSi').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 25,
                deferRender: true,
                order: [0, 'desc'],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_otro_si',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "tema" },
                    { "data": "otro_si" },
                    { "data": "id" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3],
                        class: 'text-center',
                    },
                    {
                        targets: [-2],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.otro_si + '" download="' + row.otro_si + '"><button class="btn btn-primary">Descargar Otro Si</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [-1],
                        render: function (data, type, row) {
                            var buttons = '<a href="/Gestión_humana/Actualizar_otro_si/' + row.id + '"><button title="Actualizar Otro Si" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                            return buttons;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetOtroSi').modal('show');
        });

    $('#data tbody')
        .on('click', 'a[rel=details_Procesos]', function () {
            var tr = tblColaboradores.cell($(this).closest('td, li')).index();
            var data = tblColaboradores.row(tr.row).data();

            $('#tblDetProcesos').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 25,
                deferRender: true,
                order: [0, 'desc'],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_procesos',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "informe_falta" },
                    { "data": "carta_citacion" },
                    { "data": "acta" },
                    { "data": "decision" },
                    { "data": "id" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3, 4, 5],
                        class: 'text-center',
                    },
                    {
                        targets: [2],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.carta_citacion + '" download="' + row.carta_citacion + '"><button class="btn btn-primary">Descargar Carta Citación</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [3],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.acta + '" download="' + row.acta + '"><button class="btn btn-primary">Descargar Acta</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [-1],
                        render: function (data, type, row) {
                            var buttons = '<a href="/Gestión_humana/Actualizar_proceso_disciplinario/' + row.id + '"><button title="Actualizar Proceso" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                            return buttons;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetProcesos').modal('show');
        });
    $('#data tbody')
        .on('click', 'a[rel=examenes_medicos]', function () {
            var tr = tblColaboradores.cell($(this).closest('td, li')).index();
            var data = tblColaboradores.row(tr.row).data();

            $('#tblDetExamenes').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 25,
                deferRender: true,
                order: [0, 'desc'],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_examen',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "fecha_examen" },
                    { "data": "motivo" },
                    { "data": "resultados" },
                    { "data": "id" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3, 4],
                        class: 'text-center',
                    },
                    {
                        targets: [-2],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.resultados + '" download="' + row.resultados + '"><button class="btn btn-primary">Descargar resultados</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [-1],
                        render: function (data, type, row) {
                            var buttons = '<a href="/Gestión_humana/actualizar-examen-medico/' + row.id + '"><button title="Actualizar Otro Si" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                            return buttons;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetExamenes').modal('show');
        });
        $('#data tbody')
        .on('click', 'a[rel=capacitacion]', function () {
            var tr = tblColaboradores.cell($(this).closest('td, li')).index();
            var data = tblColaboradores.row(tr.row).data();

            $('#tblDetCapacitacion').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 25,
                deferRender: true,
                order: [0, 'desc'],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_capacitacion',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "tema" },
                    { "data": "fecha_capacitacion" },
                    { "data": "certificado" },
                    { "data": "id" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3, 4],
                        class: 'text-center',
                    },
                    {
                        targets: [-2],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.certificado + '" download="' + row.certificado + '"><button class="btn btn-primary">Descargar resultados</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [-1],
                        render: function (data, type, row) {
                            var buttons = '<a href="/Gestión_humana/actualizar-capacitacion/' + row.id + '"><button title="Actualizar Otro Si" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                            return buttons;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetCapacitacion').modal('show');
        });
        $('#data tbody')
        .on('click', 'a[rel=dotacion]', function () {
            var tr = tblColaboradores.cell($(this).closest('td, li')).index();
            var data = tblColaboradores.row(tr.row).data();

            $('#tblDetDotacion').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 25,
                deferRender: true,
                order: [0, 'desc'],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_dotacion',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "id" },
                    { "data": "fecha_entrega" },
                    { "data": "documento" },
                    { "data": "id" },
                ],
                columnDefs: [
                    {
                        targets: [0, 1, 2, 3],
                        class: 'text-center',
                    },
                    {
                        targets: [-2],
                        render: function (data, type, row) {
                            var buttons = '<a href="' + row.documento + '" download="' + row.documento + '"><button class="btn btn-primary">Descargar resultados</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [-1],
                        render: function (data, type, row) {
                            var buttons = '<a href="/Gestión_humana/actualizar-entrega-dotacion/' + row.id + '"><button title="Actualizar Otro Si" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                            return buttons;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModalDetDotacion').modal('show');
        });
});