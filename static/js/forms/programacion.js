var tblProgramacion;

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

var programacion = {
    items: {
        programacion_colaborador: [],
    },
    get_ids: function () {
        var ids = [];
        $.each(this.items.programacion_colaborador, function (key, value) {
            ids.push(value.id);
        });
        return ids;
    },
    programacion_colaborador: function () {
        tblProgramacion = $('#tblProgramacion').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.programacion_colaborador,
            columns: [
                { "data": "id" },
                { "data": "id" },
                { "data": "nombre" },
                { "data": "turno" },
                { "data": "fecha_programacion" },
                { "data": "maquina" },
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
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<select class="form-control form-control-sm" name="turno">' +
                        '<option value="---">---</option>' +
                        '<option value="Turno 1" ' + (row.turno === 'Turno 1' ? 'selected' : '') + '>Turno 1</option>' +
                        '<option value="Turno 2" ' + (row.turno === 'Turno 2' ? 'selected' : '') + '>Turno 2</option>' +
                        '<option value="Turno 3" ' + (row.turno === 'Turno 3' ? 'selected' : '') + '>Turno 3</option>' +
                        '<option value="Turno 4" ' + (row.turno === 'Turno 4' ? 'selected' : '') + '>Turno 4</option>' +
                        '<option value="Turno 5" ' + (row.turno === 'Turno 5' ? 'selected' : '') + '>Turno 5</option>' +
                        '<option value="Turno 6" ' + (row.turno === 'Turno 6' ? 'selected' : '') + '>Turno 6</option>' +
                        '<option value="Vacaciones" ' + (row.turno === 'Vacaciones' ? 'selected' : '') + '>Vacaciones</option>' +
                        '<option value="Incapacidad" ' + (row.turno === 'Incapacidad' ? 'selected' : '') + '>Incapacidad</option>' +
                        '<option value="Licencia no remunerada" ' + (row.turno === 'Licencia no remunerada' ? 'selected' : '') + '>Licencia no remunerada</option>' +
                        '<option value="Otros" ' + (row.turno === 'Otros' ? 'selected' : '') + '>Otros</option>' +
                        '</select>';
                    }
                },
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="date" name="fecha_programacion" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.fecha_programacion + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<select class="form-control form-control-sm" name="maquina">' +
                        '<option value="---">---</option>' +
                        '<option value="Sin asignar" ' + (row.maquina === 'Sin asignar' ? 'selected' : '') + '>Sin asignar</option>' +
                        '<option value="Inyectora 1" ' + (row.maquina === 'Inyectora 1' ? 'selected' : '') + '>Inyectora 1</option>' +
                        '<option value="Inyectora 2" ' + (row.maquina === 'Inyectora 2' ? 'selected' : '') + '>Inyectora 2</option>' +
                        '<option value="Inyectora 3" ' + (row.maquina === 'Inyectora 3' ? 'selected' : '') + '>Inyectora 3</option>' +
                        '<option value="Inyectora 4" ' + (row.maquina === 'Inyectora 4' ? 'selected' : '') + '>Inyectora 4</option>' +
                        '<option value="Inyectora 5" ' + (row.maquina === 'Inyectora 5' ? 'selected' : '') + '>Inyectora 5</option>' +
                        '<option value="Inyectora 6" ' + (row.maquina === 'Inyectora 6' ? 'selected' : '') + '>Inyectora 6</option>' +
                        '<option value="Inyectora 7" ' + (row.maquina === 'Inyectora 7' ? 'selected' : '') + '>Inyectora 7</option>' +
                        '<option value="Sopladora 1" ' + (row.maquina === 'Sopladora 1' ? 'selected' : '') + '>Sopladora 1</option>' +
                        '<option value="Sopladora 2" ' + (row.maquina === 'Sopladora 2' ? 'selected' : '') + '>Sopladora 2</option>' +
                        '<option value="Sopladora 3" ' + (row.maquina === 'Sopladora 3' ? 'selected' : '') + '>Sopladora 3</option>' +
                        '<option value="Maquila" ' + (row.maquina === 'Maquila' ? 'selected' : '') + '>Maquila</option>' +
                        '<option value="Ensamble" ' + (row.maquina === 'Ensamble' ? 'selected' : '') + '>Ensamble</option>' +
                        '</select>';
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
                    ids: JSON.stringify(programacion.get_ids())
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
        programacion.items.programacion_colaborador.push(data);
        programacion.programacion_colaborador();
        $(this).val('').trigger('change.select2');
    });

    //Evento: eliminar colaboradores
    $('#tblProgramacion tbody').on('click', 'a[rel="remove"]', function () {
        var tr = tblProgramacion.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Est@ seguro de eliminar al colaborador del control de producción?', function () {
            programacion.items.programacion_colaborador.splice(tr.row, 1);
            programacion.programacion_colaborador();
        });
    }).on('change', 'select[name="turno"]', function () {
        var turno = $(this).find('option:selected').text();
        var tr = tblProgramacion.cell($(this).closest('td, li')).index();
        programacion.items.programacion_colaborador[tr.row].turno = turno; 
    }).on('change', 'input[name="fecha_programacion"]', function () {
        var fecha_programacion = $(this).val();
        var tr = tblProgramacion.cell($(this).closest('td, li')).index();
        programacion.items.programacion_colaborador[tr.row].fecha_programacion = fecha_programacion; 
    }).on('change', 'select[name="maquina"]', function () {
        var maquina = $(this).find('option:selected').text();
        var tr = tblProgramacion.cell($(this).closest('td, li')).index();
        programacion.items.programacion_colaborador[tr.row].maquina = maquina; 
    });

    //Guardado de datos
    $('#formProgramacion').on('submit', function(e){
        e.preventDefault();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('programacion', JSON.stringify(programacion.items));
        submit_with_ajax(window.location.pathname, parameters, 'Notificación', 'Esta segur@ que desea crear el siguiente registro', function(){
            location.href = '/Gestión_humana/programacion-historico';
        });
    });

    // Inicializar tablas
    programacion.programacion_colaborador();

});
