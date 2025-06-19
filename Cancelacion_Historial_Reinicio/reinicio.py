


def reiniciar_pedido():
    while True:
        condicion = input("¿Desea realizar otra orden? (S/N): ").strip().lower()
        if condicion == "s":
            return True
        elif condicion == "n":
            return False
        else:
            print("Por favor, ingrese 'S' para sí o 'N' para no.")



