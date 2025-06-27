from modulo_guardar.guardar_datos import gestionar_operaciones
from modulo_pedido.menu import mostrar_menu
from modulo_pedido.reinicio import reiniciar_pedido
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla



def generar_factura(cliente, pedidos, delivery=50):
    caracter = 45
    print("\n" + "="*caracter)
    print("         🧾 BURGERSOFT - FACTURA")
    print("="*caracter)

    nombre = cliente[0]['Nombre']
    apellido = cliente[1]["Apellido"]
    direccion = cliente[2]["Dirección"]
    pago = cliente[4]["Método de pago (Efectivo/Tarjeta)"]

    print(f"Nombre del cliente: {nombre} {apellido}")
    print(f"Dirección: {direccion}")
    print(f"Método de pago: {pago}")
    print("-" * caracter)

    total_pedido = 0
    print("Productos seleccionados: ")
    print("-" * caracter)
    for pedido in pedidos:
        print(f"{pedido['cantidad']:^5}{pedido['producto']:<30}{pedido['precio_unitario']:>8.2f}")
        total_pedido += pedido['precio_unitario']
    print("-" * caracter)

    print(f"Costo de delivery:        ${delivery:.2f}")
    total_pagar = total_pedido + delivery
    print(f"TOTAL A PAGAR:            ${total_pagar:.2f}")
    print("-" * caracter)
    print("⏱ Tiempo estimado de entrega: 20–25 minutos")
    print("="*caracter + "\n")
    gestionar_operaciones(cliente=nombre,pedido=pedidos)

    if reiniciar_pedido():
        limpiar_pantalla()
        mostrar_menu(limpiar=True)
    else:
        limpiar_pantalla()
        print(MENSAJES['gracias'])