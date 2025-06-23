import os
from modulo_factura.calculo_factura import generar_factura
from modulo_pedido.menu import obtener_pedido




datos_cliente = []
def capturar_datos_cliente():

    print("=" * 30)
    print("   *** DATOS DEL CLIENTE ***   ")
    print("=" * 30)
    datos_a_pedir = ["Nombre", "Apellido", "Dirección", "Color de casa", "Método de pago (Efectivo/Tarjeta)"]
    

    for encabezado in datos_a_pedir:
        while True:
            dato = input(f"{encabezado}: ").strip()
            if dato == "":
                print("Este espacio no puede estar vacío")
            elif encabezado == "Método de pago" and dato not in ["Efectivo", "Tarjeta"]:
                print("Método inválido. Escriba 'Efectivo' o 'Tarjeta'.")
            else:
                datos_cliente.append({encabezado:dato})
                break
    os.system("cls")
    generar_factura(cliente=datos_cliente,pedidos=obtener_pedido())








