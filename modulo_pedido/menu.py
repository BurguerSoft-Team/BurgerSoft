import os


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
    print("              *** MENU ***   ")
    print("=" * 42)

    while True:
        n = 1
        for plato, precio in menu.items():
            print(f"{n}. {plato} - {precio} córdobas")
            n += 1
        print("\n")

        try:
            seleccion = int(input("¿Qué deseas ordenar? (Elige el número del platillo): "))
            if 1 <= seleccion <= len(menu):
                plato_elegido = list(menu.keys())[seleccion - 1]
                cantidad, precio = calcular_cantidad_precio(precio=menu[plato_elegido], plato=plato_elegido)
                pedido.append({"producto": plato_elegido, "cantidad": cantidad, "precio_unitario": precio})
                print(f"Has agregado {cantidad} {plato_elegido} por {precio} córdobas a tu pedido.")
            else:
                os.system("cls")
                print("=" * 62)
                print("Error: opción no válida. Por favor, elige un número del menú.".center(42))
                print("=" * 62 + "\n")
                continue
        except ValueError:
            print("Entrada inválida. Debes ingresar un número correspondiente al platillo.")
            continue

        while True:
            otra_orden = input("¿Deseas ordenar otro plato? (sí/no): ").strip().lower()
            if otra_orden == "si":
                os.system("cls")
                break
            elif otra_orden == "no":
                from modulo_cliente.datos_cliente import capturar_datos_cliente
                os.system("cls")
                capturar_datos_cliente()
                return
            else:
                print("Respuesta no válida. Por favor, escribe 'sí' o 'no'.")
                continue

def calcular_cantidad_precio(precio, plato):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de '{plato}': "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.\n")
                continue
            if cantidad == 0:
                print("Cantidad 0 no permitida. Se agregará 1 por defecto.\n")
                cantidad = 1
            precio_total = precio * cantidad
            return cantidad, precio_total
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero válido.\n")
            continue

def obtener_pedido():
    return pedido



