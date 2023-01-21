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
            {"data": "id"},
            {"data": "full_name"},
            {"data": "numero_documento"},
            {"data": "telefono_contacto"},
            {"data": "proceso"},
            {"data": "nombre_emergencia"},
            {"data": "parentezco"},
            {"data": "telefono_emergencia"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/Gestión_humana/Actualizar_colaborador/' + row.id + '"><button title="Editar Información Colaborador" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                    buttons += '<a href="/Gestión_humana/Otro_si/' + row.id + '/"><button title="Agregar Otro Si" class="btn btn-success btn-xs btn-flat"><i class="fas fa-folder-open"></i></button></a> ';
                    buttons += '<a href="/Gestión_humana/Proceso_disciplinario/' + row.id + '"><button title="Agregar Proceso Disciplinario" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-gavel"></i></button></a> ';
                    buttons += '<a href="/Gestión_humana/Colaborador/' + row.id + '"><button title="Colaborador" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-user"></i></button></a> ';
                    buttons += '<a rel="details_otro_si"><button title="Otro Si" class="btn btn-secondary btn-xs btn-flat"><i class="fas fa-folder"></i></button></a> ';
                    buttons += '<a rel="details_Procesos"><button title="Procesos Disciplinarios" class="btn btn-secondary btn-xs btn-flat"><i class="fas fa-gavel"></i></button></a>';
                    return buttons;
                }
            },
            {
                targets: [0, 1, 2, 3, 4, 5, 6, 7, 8],
                class: 'text-center',
            },
            {
                targets: [3, 4, 5, 6, 7],
                class: 'text-center',
                orderable: false,
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
                            var buttons = '<a href="'+ row.otro_si + '" download="'+ row.otro_si + '"><button class="btn btn-primary">Descargar Otro Si</button></a>';
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
                            var buttons = '<a href="'+ row.carta_citacion + '" download="'+ row.carta_citacion + '"><button class="btn btn-primary">Descargar Carta Citación</button></a>';
                            return buttons;
                        }
                    },
                    {
                        targets: [3],
                        render: function (data, type, row) {
                            var buttons = '<a href="'+ row.acta + '" download="'+ row.acta + '"><button class="btn btn-primary">Descargar Acta</button></a>';
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
});