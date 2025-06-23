from modulo_utils.mensajes import MENSAJES

def cancelar_pedido():
    while True:
        condicion = input("¿Desea cancelar la orden? (S/N): ").strip().lower()
        if condicion == "s":
            return True
        elif condicion == "n":
            return False
        else:
            print(MENSAJES['respuesta_no_valida'])
