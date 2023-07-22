var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');
var tblActualizarProgramacion;

function generate_report() {
    var busqueda = {
        'action': 'searchdata',
        'start_date': date_now,
        'end_date': date_now,
    };

    if (date_range !== null) {
        busqueda['start_date'] = date_range.startDate.format('YYYY-MM-DD');
        busqueda['end_date'] = date_range.endDate.format('YYYY-MM-DD');
    }

    var programacion = {
        items: {
            programacion_colaborador: [],
        },
        programacion_colaborador: function () {
            tblActualizarProgramacion = $('#tblActualizarProgramacion').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                pageLength: 50,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: busqueda,
                    dataSrc: ""
                },
                data: this.items.programacion_colaborador,
                columns: [
                    { "data": "id" },
                    { "data": "nombre" },
                    { "data": "turno" },
                    { "data": "fecha_programacion" },
                    { "data": "maquina" },
                    { "data": "cumplimiento" },
                    { "data": "motivo_incumplimiento" },
                    { "data": "turno_reprogramacion" },
                    { "data": "colaborador" },
                ],
                columnDefs: [
                    {
                        targets: [2],
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
                        targets: [-2],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<select class="form-control form-control-sm" name="turno_reprogramacion">' +
                            '<option value="">---</option>' +
                            '<option value="Turno 1" ' + (row.turno_reprogramacion === 'Turno 1' ? 'selected' : '') + '>Turno 1</option>' +
                            '<option value="Turno 2" ' + (row.turno_reprogramacion === 'Turno 2' ? 'selected' : '') + '>Turno 2</option>' +
                            '<option value="Turno 3" ' + (row.turno_reprogramacion === 'Turno 3' ? 'selected' : '') + '>Turno 3</option>' +
                            '<option value="Turno 4" ' + (row.turno_reprogramacion === 'Turno 4' ? 'selected' : '') + '>Turno 4</option>' +
                            '<option value="Turno 5" ' + (row.turno_reprogramacion === 'Turno 5' ? 'selected' : '') + '>Turno 5</option>' +
                            '<option value="Turno 6" ' + (row.turno_reprogramacion === 'Turno 6' ? 'selected' : '') + '>Turno 6</option>' +
                            '<option value="Vacaciones" ' + (row.turno_reprogramacion === 'Vacaciones' ? 'selected' : '') + '>Vacaciones</option>' +
                            '<option value="Incapacidad" ' + (row.turno_reprogramacion === 'Incapacidad' ? 'selected' : '') + '>Incapacidad</option>' +
                            '<option value="Licencia no remunerada" ' + (row.turno_reprogramacion === 'Licencia no remunerada' ? 'selected' : '') + '>Licencia no remunerada</option>' +
                            '<option value="Otros" ' + (row.turno_reprogramacion === 'Otros' ? 'selected' : '') + '>Otros</option>' +
                            '</select>';
                        }
                    },
                    {
                        targets: [3],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<input type="date" name="fecha_programacion" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.fecha_programacion + '">';
                        }
                    },
                    {
                        targets: [-3],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<select class="form-control form-control-sm" name="motivo_incumplimiento">' +
                            '<option value="" ' + (row.motivo_incumplimiento === '' ? 'selected' : '') + '>---</option>' +
                            '<option value="Calamidad domestica" ' + (row.motivo_incumplimiento === 'Calamidad domestica' ? 'selected' : '') + '>Calamidad domestica</option>' +
                            '<option value="Incapacidad EPS" ' + (row.motivo_incumplimiento === 'Incapacidad EPS' ? 'selected' : '') + '>Incapacidad EPS</option>' +
                            '<option value="Cambio de turno" ' + (row.motivo_incumplimiento === 'Cambio de turno' ? 'selected' : '') + '>Cambio de turno</option>' +
                            '<option value="Día de la familia" ' + (row.motivo_incumplimiento === 'Día de la familia' ? 'selected' : '') + '>Día de la familia</option>' +
                            '<option value="Permiso remunerado" ' + (row.motivo_incumplimiento === 'Permiso remunerado' ? 'selected' : '') + '>Permiso remunerado</option>' +
                            '<option value="Permiso no remunerado" ' + (row.motivo_incumplimiento === 'Permiso no remunerado' ? 'selected' : '') + '>Permiso no remunerado</option>' +
                            '<option value="Renuncia" ' + (row.motivo_incumplimiento === 'Renuncia' ? 'selected' : '') + '>Renuncia</option>' +
                            '<option value="Daño máquina" ' + (row.motivo_incumplimiento === 'Daño máquina' ? 'selected' : '') + '>Daño máquina</option>' +
                            '<option value="Falta de material" ' + (row.motivo_incumplimiento === 'Falta de material' ? 'selected' : '') + '>Falta de material</option>' +
                            '<option value="Incapacidad ARL" ' + (row.motivo_incumplimiento === 'Incapacidad ARL' ? 'selected' : '') + '>Incapacidad ARL</option>' +
                            '<option value="No justificado" ' + (row.motivo_incumplimiento === 'No justificado' ? 'selected' : '') + '>No justificado</option>' +
                            '<option value="Vacaciones" ' + (row.motivo_incumplimiento === 'Vacaciones' ? 'selected' : '') + '>Vacaciones</option>' +
                            '</select>';
                        }
                    },
                    {
                        targets: [5],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<input type="checkbox" name="cumplimiento" class="form-control form-control-sm input-sm" ' + (row.cumplimiento === true ? 'checked' : '') + '>';
                        }
                    },
                    {
                        targets: [-5],
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
                    {
                        targets: [-1],
                        visible: false,
                    },
                ],
                rowCallback(row, data, displayNum, displayIndex, dataIndex) {
    
                },
                initComplete: function (settings, json) {
                    programacion.items.programacion_colaborador = json;
                }
            });
        },
    };
    
    $(function () {
        $('#tblActualizarProgramacion tbody').on('change', 'select[name="turno"]', function () {
            var turno = $(this).find('option:selected').text();
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].turno = turno; 
        }).on('change', 'input[name="fecha_programacion"]', function () {
            var fecha_programacion = $(this).val();
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].fecha_programacion = fecha_programacion; 
        }).on('change', 'select[name="maquina"]', function () {
            var maquina = $(this).find('option:selected').text();
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].maquina = maquina; 
        }).on('change', 'input[name="cumplimiento"]', function () {
            var cumplimiento = $(this).is(':checked') ? 1 : 0;
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].cumplimiento = cumplimiento; 
        }).on('change', 'select[name="motivo_incumplimiento"]', function () {
            var motivo_incumplimiento = $(this).find('option:selected').text();
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].motivo_incumplimiento = motivo_incumplimiento; 
        }).on('change', 'select[name="turno_reprogramacion"]', function () {
            var turno_reprogramacion = $(this).find('option:selected').text();
            var tr = tblActualizarProgramacion.cell($(this).closest('td, li')).index();
            programacion.items.programacion_colaborador[tr.row].turno_reprogramacion = turno_reprogramacion; 
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
        programacion.programacion_colaborador()
    });
}

generate_report()

$(function () {
    $('input[name="date_range"]').daterangepicker({
        locale: {
            format: 'YYYY-MM-DD',
            applyLabel: '<i class="fas fa-chart-pie"></i> Aplicar',
            cancelLabel: '<i class="fas fa-times"></i> Cancelar',
        }
    }).on('apply.daterangepicker', function (ev, picker) {
        date_range = picker;
        generate_report();
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_now);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range = picker;
        generate_report();
    });
});
