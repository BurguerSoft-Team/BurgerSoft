# Diccionario que contiene todos los mensajes del sistema
# Organizados por categorías para facilitar su mantenimiento
MENSAJES = {
    # Mensajes del menú principal
    'bienvenida': "*** Bienvenido a TheBurgerClub Granada ***",
    'menu_principal': [
        "1. Registrar pedido",
        "2. Ver historial de ganancias",
        "3. Salir"
    ],
    
    # Mensajes de validación general
    'campo_vacio': "¡El campo no puede estar vacío!",
    'solo_numeros': "Solo se permiten números.",
    'opcion_no_valida': "Opción no válida.",
    'gracias': "¡Gracias por usar el programa!",
    'ingrese_opcion': "Opción: ",
    
    # Mensajes del menú de productos
    'menu_titulo': "*** MENU ***",
    'error_menu': "Error: opción no válida. Por favor, elige un número del menú.",
    'agregado_pedido': "Has agregado {cantidad} {plato} por {precio} córdobas a tu pedido.",
    'ordenar_otro': "¿Deseas ordenar otro plato? (sí/no): ",
    'respuesta_no_valida': "Respuesta no válida. Por favor, ingrese 'S' para sí o 'N' para no.",
    
    # Mensajes de validación de cantidad
    'cantidad_negativa': "La cantidad no puede ser negativa. Intenta de nuevo.",
    'cantidad_cero': "Cantidad 0 no permitida. Se agregará 1 por defecto.",
    'ingrese_cantidad': "Ingrese la cantidad de '{plato}': ",
    'entrada_invalida': "Entrada inválida. Debes ingresar un número entero válido.",
    
    # Mensajes de datos del cliente
    'datos_cliente': "*** DATOS DEL CLIENTE ***",
    'espacio_vacio': "Este espacio no puede estar vacío",
    'metodo_pago_invalido': "Método inválido. Escriba 'E' para Efectivo o 'T' para Tarjeta.",
    
    # Mensajes del historial de ganancias
    'historial_ganancias': "Historial de ganancias\n",
    'fecha_fin_menor': "La fecha de fin no puede ser menor que la fecha de inicio. Intenta de nuevo.\n",
    'base_datos_vacia': "La base de datos está vacía!",
    'no_ventas_periodo': "No se encontraron ventas en el periodo seleccionado.",
    'detalle_ventas': "--- Detalle de ventas en el periodo ---",
    'total_ganado': "TOTAL GANADO EN EL PERIODO: ${total:.2f}",
    
    # Mensajes de pedidos
    'pedido_cancelado': "Pedido cancelado. Volviendo al menú principal...",
    'resumen_pedido': "RESUMEN DE TU PEDIDO:",
    
    # Mensajes de validación adicionales
    "numero_no_permitido": "No se permiten números en estos datos. Intente nuevamente.",
    "cantidad_negativa": "La cantidad no puede ser negativa. Intenta de nuevo.",
} 