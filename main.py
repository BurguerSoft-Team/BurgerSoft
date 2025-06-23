from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_numero
from modulo_historial.calcular_ganacia import historial
from modulo_pedido.menu import mostrar_menu

def main():
    while True:
        limpiar_pantalla()
        print("=" * 45)
        print(f"   {MENSAJES['bienvenida']}   ")
        print("=" * 45)
        for linea in MENSAJES['menu_principal']:
            print(linea)
        
        opcion = input_numero(MENSAJES['ingrese_opcion'])
        
        if opcion == 1:
            limpiar_pantalla()
            mostrar_menu()
        elif opcion == 2:
            limpiar_pantalla()
            historial()
        elif opcion == 3:
            print(MENSAJES['gracias'])
            break
        else:
            print(MENSAJES['opcion_no_valida'])

if __name__ == "__main__":
    main()