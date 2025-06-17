# Capturar: nombre, apellido, dirección, color casa, método de pago
# Validar datos ingresados (que sean texto, no vacíos, etc.)
# Este programador solo se enfoca en la parte personal del cliente y sus datos de contacto.

def capturar_datos_cliente():
    print("")
    print("---Datos del cliente---")
    print("")

    while True: 
        nombre = input("Ingrese su nombre: ")
        if nombre.strip() == "":
            print("Este espacio no puede estar vacío")
        else: 
            break

    while True:
        apellido = input("Ingrese su apellido: ")
        if apellido.strip() == "":
            print("Este espacio no puede estar vacío")
        else: 
            break

    while True:
        direccion = input("Ingrese la dirección de su casa: ")
        if direccion.strip() == "":
            print("Este espacio no puede estar vacío")
        else: 
            break

    while True:
        color_casa = input("Ingrese el color de su casa: ")
        if color_casa.strip() == "":
            print("Este espacio no puede estar vacío")
        else: 
            break

    while True:
        metodo_de_pago = input("Escoja su método de pago (Efectivo o Tarjeta): ")
        if metodo_de_pago == ["Efectivo", "Tarjeta"]:
            print("Método inválido. Escriba 'Efectivo' o 'Tarjeta'.")
        else:
            print(f"Método seleccionado: {metodo_de_pago}")
            break
    

capturar_datos_cliente()
