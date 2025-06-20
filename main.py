import os
from modulo_historial.calcular_ganacia import historial
from modulo_pedido.menu import mostrar_menu

def main():
    
    print("=" * 45)
    print("   *** Bienvenido a TheBurgerClub Granada ***   ")
    print("=" * 45)

    print("1.Registrar pedido")
    print("2.Ver historial de ganacias")
    
    while True:
        opcion = input("Opcion: ")
        if opcion == "":
            print("Campo vacio!")
            continue
        else:
            opcionEntero = int(opcion)
            if opcionEntero == 1:
                os.system('cls')
                mostrar_menu()
                break
            elif opcionEntero == 2:
                os.system('cls')  
                historial()
                break
            else:
                print("Opcion no valido")
                continue

if __name__ == "__main__":
    main()