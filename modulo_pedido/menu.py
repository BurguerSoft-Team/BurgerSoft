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
    print("=" * 45)
    print("   *** MENU ***   ")
    print("=" * 45)

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
                precio = menu[plato_elegido]
                pedido.append((plato_elegido, precio))
                print(f"Has agregado '{plato_elegido}' por {precio} córdobas a tu pedido.")
            else:
                print("Opción no válida. Intenta de nuevo.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        while True:
            otra_orden = input("¿Deseas ordenar otro plato? (sí/no): ").strip().lower()
            if otra_orden == "si":
                break  
            elif otra_orden == "no":
                mostrar_pedido()
                return
            else:
                print("Escriba si o no")
                continue


def mostrar_pedido():
    print("\nTu pedido final es:")
    i = 1
    for plato, precio in pedido:
        print(f"{i}. {plato} por {precio} córdobas")
        i += 1


