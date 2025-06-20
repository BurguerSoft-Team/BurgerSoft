def capturar_datos_cliente():
    datos_a_pedir = ["Nombre", "Apellido", "Dirección", "Color de casa", "Método de pago"]
    datos_cliente = []

    for encabezado in datos_a_pedir:
        while True:
            dato = input(f"{encabezado}: ").strip()
            if dato == "":
                print("Este espacio no puede estar vacío")
            elif encabezado == "Método de pago" and dato not in ["Efectivo", "Tarjeta"]:
                print("Método inválido. Escriba 'Efectivo' o 'Tarjeta'.")
            else:
                datos_cliente.append(dato)
                break

    return datos_cliente

capturar_datos_cliente()
