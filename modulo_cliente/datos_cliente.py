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
            dato = input(f"{encabezado}: ").strip().lower()
            if dato == "":
                print("Este espacio no puede estar vacío")
                continue

            if encabezado == "Método de pago (Efectivo/Tarjeta)":
                if dato == "e" or dato == "t":
                    pago = obtener_pago(dato)
                    datos_cliente.append({encabezado: pago}) 
                    break
                else:
                    print("Método inválido. Escriba 'E' para Efectivo o 'T' para Tarjeta.")
                    continue
            else:
                datos_cliente.append({encabezado: dato})
                break
    os.system("cls")
    generar_factura(cliente=datos_cliente, pedidos=obtener_pedido())


def obtener_pago(pago):
    if pago == "e" or pago == "E":
        return "Efectivo"
    else:
        return "Tarjeta"