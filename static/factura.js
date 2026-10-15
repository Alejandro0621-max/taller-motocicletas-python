
document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("detalleFactura");
    const botonAgregar = document.getElementById("agregarRepuesto");
    const catalogoRepuestos = document.getElementById("catalogoRepuestos");
    const subtotalGeneral = document.getElementById("subtotalFactura");
    const totalGeneral = document.getElementById("totalFactura");
    const mensaje = document.getElementById("mensajeDetalle");

    if (!tabla || !botonAgregar || !subtotalGeneral || !totalGeneral) {
        console.error("Factura: faltan elementos HTML necesarios.");
        return;
    }

    // Catálogo temporal de servicios para probar sin base de datos.
    const serviciosPrueba = [
        {
            codigo: "SRV-001",
            descripcion: "Cambio de aceite y revisión general",
            valor: 45000
        },
        {
            codigo: "SRV-002",
            descripcion: "Mantenimiento preventivo",
            valor: 80000
        }
    ];

    const moneda = valor =>
        new Intl.NumberFormat("es-CO", {
            style: "currency",
            currency: "COP",
            maximumFractionDigits: 0
        }).format(valor);

    function buscarConcepto(codigo, tipo) {
        const codigoBuscado = codigo.trim().toUpperCase();

        if (!codigoBuscado) return null;

        if (tipo === "Servicio") {
            return serviciosPrueba.find(servicio =>
                servicio.codigo.toUpperCase() === codigoBuscado
            ) || null;
        }

        if (tipo === "Repuesto" && catalogoRepuestos) {
            const opciones = Array.from(catalogoRepuestos.options);

            const opcion = opciones.find(item =>
                item.value &&
                (item.dataset.codigo || "").trim().toUpperCase()
                    === codigoBuscado
            );

            if (!opcion) return null;

            return {
                id: opcion.value,
                codigo: opcion.dataset.codigo,
                descripcion: opcion.dataset.nombre || opcion.textContent.trim(),
                valor: Number(opcion.dataset.valor) || 0,
                stock: Number(opcion.dataset.stock) || 0
            };
        }

        return null;
    }

    function actualizarNumeracion() {
        tabla.querySelectorAll("tr").forEach((fila, indice) => {
            fila.querySelector(".numero-linea").textContent = indice + 1;
        });
    }

    function calcularTotales() {
        let totalFactura = 0;

        tabla.querySelectorAll("tr").forEach(fila => {
            const cantidad = Number(fila.querySelector(".cantidad").value);
            const precio = Number(fila.querySelector(".valor-unitario").value);
            const descripcion = fila.querySelector(".descripcion-concepto").value;

            const subtotal = descripcion && cantidad > 0 && precio >= 0
                ? cantidad * precio
                : 0;

            fila.querySelector(".valor-total").value = moneda(subtotal);
            totalFactura += subtotal;
        });

        subtotalGeneral.textContent = moneda(totalFactura);
        totalGeneral.textContent = moneda(totalFactura);

        if (mensaje) {
            mensaje.hidden = tabla.rows.length > 0;
        }
    }

    function agregarFila() {
        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td class="numero-linea"></td>
            <td>
                <select name="tipo[]" class="tipo-concepto">
                    <option value="Repuesto">Repuesto</option>
                    <option value="Servicio">Servicio</option>
                </select>
            </td>
            <td>
                <input type="text" name="codigo[]"
                       class="codigo-concepto"
                       placeholder="Ej. REP-001">
            </td>
            <td>
                <input type="text" name="descripcion[]"
                       class="descripcion-concepto"
                       placeholder="Descripción automática" readonly>
            </td>
            <td>
                <input type="number" name="cantidad[]"
                       class="cantidad" value="1" min="1" step="1">
            </td>
            <td>
                <input type="number" name="valor_unitario[]"
                       class="valor-unitario" value="0" min="0" step="0.01">
            </td>
            <td>
                <input type="text" class="valor-total" value="$ 0" readonly>
            </td>
            <td>
                <button type="button" class="btn-quitar"
                        aria-label="Eliminar concepto">×</button>
            </td>
        `;

        tabla.appendChild(fila);

        const codigo = fila.querySelector(".codigo-concepto");
        const tipo = fila.querySelector(".tipo-concepto");
        const descripcion = fila.querySelector(".descripcion-concepto");
        const cantidad = fila.querySelector(".cantidad");
        const precio = fila.querySelector(".valor-unitario");

        function completarConcepto() {
            const concepto = buscarConcepto(codigo.value, tipo.value);

            if (concepto) {
                descripcion.value = concepto.descripcion;
                precio.value = concepto.valor;
            } else {
                descripcion.value = "";
                precio.value = "0";
            }

            calcularTotales();
        }

        codigo.addEventListener("change", completarConcepto);
        codigo.addEventListener("keydown", evento => {
            if (evento.key === "Enter") {
                evento.preventDefault();
                completarConcepto();
            }
        });

        tipo.addEventListener("change", completarConcepto);
        cantidad.addEventListener("input", calcularTotales);
        precio.addEventListener("input", calcularTotales);

        fila.querySelector(".btn-quitar").addEventListener("click", () => {
            fila.remove();
            actualizarNumeracion();
            calcularTotales();
        });

        actualizarNumeracion();
        calcularTotales();
        codigo.focus();
    }

    botonAgregar.addEventListener("click", agregarFila);

    // Crear la primera fila vacía.
    agregarFila();

    console.log("Factura: JavaScript cargado correctamente.");
});

