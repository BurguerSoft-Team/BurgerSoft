# Importaciones necesarias para el módulo de facturación
from modulo_guardar.guardar_datos import gestionar_operaciones
from modulo_pedido.menu import mostrar_menu
from modulo_pedido.reinicio import reiniciar_pedido
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla

def generar_factura(cliente, pedidos, delivery=50):
    """
    Genera y muestra una factura completa para el pedido del cliente.
    
    Args:
        cliente: Lista con los datos del cliente
        pedidos: Lista con los productos del pedido
        delivery: Costo del delivery (por defecto 50 córdobas)
    """
    # Configuración del formato de la factura
    caracter = 45
    
    # Muestra el encabezado de la factura
    print("\n" + "="*caracter)
    print("         🧾 BURGERSOFT - FACTURA")
    print("="*caracter)

    # Extrae los datos del cliente
    nombre = cliente[0]['Nombre']
    apellido = cliente[1]["Apellido"]
    direccion = cliente[2]["Dirección"]
    pago = cliente[4]["Método de pago (Efectivo/Tarjeta)"]

    # Muestra la información del cliente
    print(f"Nombre del cliente: {nombre} {apellido}")
    print(f"Dirección: {direccion}")
    print(f"Método de pago: {pago}")
    print("-" * caracter)

    # Calcula y muestra los productos del pedido
    total_pedido = 0
    print("Productos seleccionados: ")
    print("-" * caracter)
    for pedido in pedidos:
        print(f"{pedido['cantidad']:^5}{pedido['producto']:<30}{pedido['precio_unitario']:>8.2f}")
        total_pedido += pedido['precio_unitario']
    print("-" * caracter)

    # Muestra el resumen final con delivery
    print(f"Costo de delivery:        ${delivery:.2f}")
    total_pagar = total_pedido + delivery
    print(f"TOTAL A PAGAR:            ${total_pagar:.2f}")
    print("-" * caracter)
    print("⏱ Tiempo estimado de entrega: 20–25 minutos")
    print("="*caracter + "\n")
    
    # Guarda la operación en el archivo de ventas
    gestionar_operaciones(cliente=nombre,pedido=pedidos)

    # Pregunta si desea realizar otro pedido
    if reiniciar_pedido():
        limpiar_pantalla()
        mostrar_menu(limpiar=True)
    else:
        limpiar_pantalla()
        
