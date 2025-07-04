# Importaciones necesarias para el módulo de pedidos
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_numero, input_si_no
from modulo_pedido.cancelar import cancelar_pedido

# Diccionario que contiene el menú de productos con sus precios
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

# Lista global para almacenar el pedido actual
pedido = []

def mostrar_menu(limpiar):
    """
    Función principal para mostrar el menú y procesar pedidos.
    
    Args:
        limpiar: Booleano que indica si limpiar el pedido anterior
    """
    # Limpia el pedido si se solicita
    if limpiar:
        pedido.clear()
        
    # Muestra el encabezado del menú
    print("=" * 42)
    print(f"              {MENSAJES['menu_titulo']}   ")
    print("=" * 42)

    while True:
        # Muestra todos los productos disponibles
        n = 1
        for plato, precio in menu.items():
            print(f"{n}. {plato} - {precio} córdobas")
            n += 1
        print("\n")

        # Captura la selección del usuario
        seleccion = input_numero("¿Qué deseas ordenar? (Elige el número del platillo): ")
        if 1 <= seleccion <= len(menu):
            # Procesa la selección válida
            plato_elegido = list(menu.keys())[seleccion - 1]
            cantidad, precio = calcular_cantidad_precio(precio=menu[plato_elegido], plato=plato_elegido)
            pedido.append({"producto": plato_elegido, "cantidad": cantidad, "precio_unitario": precio})
            print(MENSAJES['agregado_pedido'].format(cantidad=cantidad, plato=plato_elegido, precio=precio))
        else:
            # Maneja selección inválida
            limpiar_pantalla()
            print("=" * 62)
            print(MENSAJES['error_menu'].center(42))
            print("=" * 62 + "\n")
            continue

        # Pregunta si desea ordenar otro plato
        if input_si_no(MENSAJES['ordenar_otro']):
            limpiar_pantalla()
            continue
        else:
            # Muestra resumen y continúa con el proceso
            resumen(limpiar)
            break

def resumen(limpiar):
    """
    Muestra el resumen del pedido y permite modificaciones.
    
    Args:
        limpiar: Booleano que indica si limpiar el pedido
    """
    if pedido:
        # Muestra el resumen del pedido
        print("\n" + "=" * 50)
        print(MENSAJES['resumen_pedido'])
        print("=" * 50)
        total_pedido = 0
        m = 1
        for item in pedido:
            print(f"{m}- {item['producto']} x{item['cantidad']} = ${item['precio_unitario']:.2f}")
            m += 1
            total_pedido += item['precio_unitario']
        print("-" * 50)
        print(f"TOTAL: ${total_pedido:.2f}")
        print("=" * 50)

        # Permite cambios en el pedido
        cambio(limpiar)
        
        # Verifica si se cancela el pedido
        if cancelar_pedido():
            print(MENSAJES['pedido_cancelado'])
            pedido.clear()
            return
            
    # Continúa con la captura de datos del cliente
    from modulo_cliente.datos_cliente import capturar_datos_cliente
    limpiar_pantalla()
    capturar_datos_cliente(limpiar=limpiar)
    pedido.clear()
    return
        
def cambio(limpiar):
    """
    Permite al usuario modificar elementos de su pedido.
    
    Args:
        limpiar: Booleano que indica si limpiar el pedido
    """
    while True:
        condicion = input("Desea cambiar un plato de su orden? (si/no): ")
        if condicion.lower().strip() in ["s", "si"]:
            # Proceso de cambio de plato
            while True:
                cambio = input_numero("Ingrese el numero del plato que desea cambiar: ")
                if cambio in range(1,len(pedido) + 1):
                    limpiar_pantalla()
                    seleccionado = pedido[cambio-1]
                    
                    # Muestra el plato seleccionado y el menú completo
                    print(f"- {seleccionado['producto']} x{seleccionado['cantidad']} = ${seleccionado['precio_unitario']:.2f}")
                    print("")
                    n = 1
                    for plato, precio in menu.items():
                        print(f"{n}. {plato} - {precio} córdobas")
                        n += 1
                    print("\n")
                    
                    # Proceso de reemplazo
                    while True:
                        seleccion = int(input("Por cual lo desea reemplazar?: "))
                    
                        if 1 <= seleccion <= len(menu):
                            plato_elegido = list(menu.keys())[seleccion - 1]
                            while True:
                                cantidad_nueva = int(input("Cuantas unidades desea?: "))
                                print("")
                                if cantidad_nueva <= 0:
                                    print("Ingrese un mayor que 0")
                                    continue
                                else:
                                    # Actualiza el pedido con el nuevo plato
                                    precio = menu[plato_elegido]
                                    precio_nuevo = precio * cantidad_nueva

                                    if cantidad_nueva:
                                        cantidad = int(cantidad_nueva)
                                    if precio_nuevo:
                                        precio = int(precio_nuevo)
                                    if plato_elegido:
                                        pedido[cambio-1] = {"producto": plato_elegido, "cantidad": cantidad, "precio_unitario": precio}

                                    # Muestra el pedido actualizado
                                    print("PEDIDO ACTUALIZADO!")
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
                                    break
                        else:
                            print("Ingrese un numero dentro del rango\n")
                            continue
                        break
                    
                else:
                    print("Ingrese un numero dentro del rango\n")
                    continue
                break
        elif condicion.lower().strip() in ["n", "no"]:
            break
        else:
            print(MENSAJES['respuesta_no_valida'])
            print("")
            continue
        break

def calcular_cantidad_precio(precio, plato):
    """
    Calcula la cantidad y precio total de un producto.
    
    Args:
        precio: Precio unitario del producto
        plato: Nombre del producto
        
    Returns:
        tuple: (cantidad, precio_total)
    """
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
    """
    Retorna el pedido actual.
    
    Returns:
        list: Lista con los elementos del pedido
    """
    return pedido



