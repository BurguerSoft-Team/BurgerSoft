# Importación de mensajes del sistema
from modulo_utils.mensajes import MENSAJES

def cancelar_pedido():
    """
    Permite al usuario cancelar su pedido actual.
    
    Returns:
        bool: True si el usuario confirma la cancelación, False en caso contrario
    """
    while True:
        # Pregunta al usuario si desea cancelar el pedido
        condicion = input("¿Desea cancelar la orden? (S/N): ").strip().lower()
        if condicion == "s":
            return True
        elif condicion == "n":
            return False
        else:
            # Muestra mensaje de error si la respuesta no es válida
            print(MENSAJES['respuesta_no_valida'])
