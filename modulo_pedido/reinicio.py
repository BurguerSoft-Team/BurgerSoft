def reiniciar_pedido():
    """
    Pregunta al usuario si desea realizar otra orden después de completar una.
    
    Returns:
        bool: True si el usuario desea hacer otra orden, False en caso contrario
    """
    while True:
        # Captura la respuesta del usuario
        condicion = input("¿Desea realizar otra orden? (S/N): ").strip().lower()
        if condicion == "s":
            return True
        elif condicion == "n":
            return False
        else:
            # Muestra mensaje de error si la respuesta no es válida
            print("Por favor, ingrese 'S' para sí o 'N' para no.")



