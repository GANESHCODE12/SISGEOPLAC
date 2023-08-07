var tblProduccion;

$(function () {
    tblProduccion = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        order: [0, 'desc'],
        pageLength: 25,
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
            { "data": "numero_op" },
            { "data": "Nombre_producto" },
            { "data": "estado_op" },
            { "data": "maquina" },
            { "data": "lote" },
            { "data": "cliente" },
            { "data": "cantidad_requerida" },
            { "data": "saldo_a" },
            { "data": "saldo" },
            { "data": "saldo_cliente" },
            { "data": "color" },
            { "data": "fecha_entrega" },
            { "data": "numero_op" },
            { "data": "aprobacion_orden" }
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (row.aprobacion_orden === false) {
                        var buttons = '<a href="actualizar/orden-' + row.numero_op + '"><button title="Actualizar orden" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                        buttons += '<a href="#"><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-eye"></i></button></a> ';
                        buttons += '<a href="#"><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-gamepad"></i></button></a> ';
                        buttons += '<a href="#"><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-vials"></i></button></a> ';
                        buttons += '<a><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-list-alt"></i></button></a> ';
                        buttons += '<a><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-tools"></i></button></a> ';
                        // buttons += '<a href="#"><button title="Requiere aprobación" class="btn btn-danger btn-xs btn-flat" disabled><i class="fas fa-people-carry"></i></button></a> ';
                    } else {
                        var buttons = '<a href="actualizar/orden-' + row.numero_op + '"><button title="Actualizar orden" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button></a> ';
                        buttons += '<a href="detalle_orden/' + row.numero_op + '/"><button title="Detalle orden" class="btn btn-primary btn-xs btn-flat"><i class="fas fa-eye"></i></button></a> ';
                        buttons += '<a href="/Control_produccion/Crear_nuevo_control/' + row.numero_op + '/"><button title="Nuevo Control de Producción" class="btn btn-info btn-xs btn-flat"><i class="fas fa-gamepad"></i></button></a> ';
                        buttons += '<a href="/Control_calidad/Crear_inspeccion/' + row.numero_op + '"><button title="Crear Inspección" class="btn btn-success btn-xs btn-flat"><i class="fas fa-vials"></i></button></a> ';
                        buttons += '<a rel="details_controls"><button title="Controles de producción" class="btn btn-dark btn-xs btn-flat"><i class="fas fa-list-alt"></i></button></a> ';
                        buttons += '<a rel="details_MPI"><button title="Detalle Materia Prima E Insumos" class="btn btn-secondary btn-xs btn-flat"><i class="fas fa-tools"></i></button></a> ';
                        // buttons += '<a href="/Inventario/Requisicion_MP_insumos/' + row.numero_op + '"><button title="Requisición material" class="btn btn-success btn-xs btn-flat"><i class="fas fa-people-carry"></i></button></a> ';
                    }
                    return buttons;
                }
            },
            {
                targets: [6, 7, 8, 9],
                render: function (data, type, row) {
                    return data.toString().replace(
                        /\B(?=(\d{3})+(?!\d))/g, "."
                    );
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                render: function (data, type, row) {
                    return moment(data).format('DD/MM/YYYY')
                },

                "type": 'date'
            },
            {
                targets: [-1],
                visible: false,
            }
        ],
        initComplete: function (settings, json) {

        }
    });
    $('#data tbody').on('click', 'a[rel=details_controls]', function () {
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        var data = tblProduccion.row(tr.row).data();

        $('#tblDetControls').DataTable({
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
                    'action': 'search_details_controls',
                    'numero_op': data.numero_op
                },
                dataSrc: ""
            },
            columns: [
                { "data": "id" },
                { "data": "producto" },
                { "data": "orden" },
                { "data": "fecha" },
                { "data": "cantidad_producida" },
                { "data": "turno" },
                { "data": "maquina" },
                { "data": "colaboradores" }
            ],
            columnDefs: [
                {
                    targets: [0, 1, 2, 3, 4, 5, 6, 7],
                    class: 'text-center',
                },
                {
                    targets: [4],
                    render: function (data, type, row) {
                        return data.toString().replace(
                            /\B(?=(\d{3})+(?!\d))/g, "."
                        );
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var html = '';
                        $.each(row.colaboradores, function (key, value) {
                            html += '<span class="badge badge-primary">' + value.nombre + '</span> ';
                        });
                        return html;
                    },
                }
            ],
            initComplete: function (settings, json) {

            }
        });

        $('#myModalDetControls').modal('show');
    });

    $('#data tbody').on('click', 'a[rel=details_MPI]', function () {
        var tr = tblProduccion.cell($(this).closest('td, li')).index();
        var data = tblProduccion.row(tr.row).data();
        let numero_op_id = data.numero_op

        $('#tblDetMPI').DataTable({
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
                    'action': 'search_details_MPI',
                    'numero_op': data.numero_op
                },
                dataSrc: ""
            },
            columns: [
                { "data": "id" },
                { "data": "producto" },
                { "data": "categoria" },
                { "data": "referencia" },
                { "data": "proveedor" },
                { "data": "ingresado" },
                { "data": "fecha" },
                { "data": "lote" },
                { "data": "cantidad_solicitada" },
                { "data": "medida" },
            ],
            columnDefs: [
                {
                    targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    class: 'text-center',
                },
                {
                    targets: [-2],
                    render: function (data, type, row) {
                        return data.toString().replace(
                            /\B(?=(\d{3})+(?!\d))/g, "."
                        );
                    }
                }
            ],
            initComplete: function (settings, json) {

            }
        });

        $('#myModalDetMPI').modal('show');
        let tituloModal = document.getElementById('orderModalLabel');
        tituloModal.innerHTML = 'Materia Prima E Insumos Utilizados En La Orden' + ' ' + numero_op_id
    });
});
