# Importaciones de módulos necesarios para el funcionamiento del programa
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_numero
from modulo_historial.calcular_ganacia import historial
from modulo_pedido.menu import mostrar_menu

def main():
    """
    Función principal del programa BurgerSoft.
    Maneja el menú principal y la navegación entre las diferentes opciones.
    """
    while True:
        # Limpia la pantalla y muestra el encabezado del programa
        limpiar_pantalla()
        print("=" * 45)
        print(f"   {MENSAJES['bienvenida']}   ")
        print("=" * 45)
        
        # Muestra las opciones del menú principal
        for linea in MENSAJES['menu_principal']:
            print(linea)
        
        # Captura la opción seleccionada por el usuario
        opcion = input_numero(MENSAJES['ingrese_opcion'])
        
        # Maneja las diferentes opciones del menú
        if opcion == 1:
            # Opción 1: Registrar un nuevo pedido
            limpiar_pantalla()
            mostrar_menu(limpiar=False)
        elif opcion == 2:
            # Opción 2: Ver historial de ganancias
            limpiar_pantalla()
            historial()
        elif opcion == 3:
            # Opción 3: Salir del programa
            print(MENSAJES['gracias'])
            break
        else:
            # Opción inválida
            print(MENSAJES['opcion_no_valida'])

# Punto de entrada del programa
if __name__ == "__main__":
    main()