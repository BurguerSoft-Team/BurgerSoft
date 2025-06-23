import os
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_numero, input_si_no
from modulo_pedido.cancelar import cancelar_pedido


menu = {
    "Hamburguesa Bacon Cheese": 180,
    "Hamburguesa Carnuda": 220,
    "Sandwich de pollo": 170,
    "Alitas de 18": 500,
    "Alitas de 6": 220,
    "Chilli Fries": 200,
    "Quesadillas de Res": 230,
    "Cheese Burger": 160,
    "Aros de cebolla": 130,
    "Mozarella sticks": 180,
}


pedido = []
def mostrar_menu():
    print("=" * 42)
    print(f"              {MENSAJES['menu_titulo']}   ")
    print("=" * 42)

    while True:
        n = 1
        for plato, precio in menu.items():
            print(f"{n}. {plato} - {precio} córdobas")
            n += 1
        print("\n")

        seleccion = input_numero("¿Qué deseas ordenar? (Elige el número del platillo): ")
        if 1 <= seleccion <= len(menu):
            plato_elegido = list(menu.keys())[seleccion - 1]
            cantidad, precio = calcular_cantidad_precio(precio=menu[plato_elegido], plato=plato_elegido)
            pedido.append({"producto": plato_elegido, "cantidad": cantidad, "precio_unitario": precio})
            print(MENSAJES['agregado_pedido'].format(cantidad=cantidad, plato=plato_elegido, precio=precio))
        else:
            limpiar_pantalla()
            print("=" * 62)
            print(MENSAJES['error_menu'].center(42))
            print("=" * 62 + "\n")
            continue

        if input_si_no(MENSAJES['ordenar_otro']):
            limpiar_pantalla()
            continue
        else:
            if pedido:
                print("\n" + "=" * 50)
                print(MENSAJES['resumen_pedido'])
                print("=" * 50)
                total_pedido = 0
                for item in pedido:
                    print(f"- {item['producto']} x{item['cantidad']} = ${item['precio_unitario']:.2f}")
                    total_pedido += item['precio_unitario']
                print("-" * 50)
                print(f"TOTAL: ${total_pedido:.2f}")
                print("=" * 50)
                
                
                if cancelar_pedido():
                    print(MENSAJES['pedido_cancelado'])
                    pedido.clear()
                    return
            
            from modulo_cliente.datos_cliente import capturar_datos_cliente
            limpiar_pantalla()
            capturar_datos_cliente()
            pedido.clear()
            return

def calcular_cantidad_precio(precio, plato):
    while True:
        try:
            cantidad = input_numero(MENSAJES['ingrese_cantidad'].format(plato=plato))
            if cantidad < 0:
                print(MENSAJES['cantidad_negativa'])
                continue
            if cantidad == 0:
                print(MENSAJES['cantidad_cero'])
                cantidad = 1
            precio_total = precio * cantidad
            return cantidad, precio_total
        except ValueError:
            print(MENSAJES['entrada_invalida'])
            continue

def obtener_pedido():
    return pedido



