import os
from modulo_factura.calculo_factura import generar_factura
from modulo_pedido.menu import obtener_pedido
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_si_no

datos_cliente = []
def capturar_datos_cliente(limpiar):
    if limpiar:
        datos_cliente.clear()

    print("=" * 30)
    print(f"   {MENSAJES['datos_cliente']}   ")
    print("=" * 30)
    datos_a_pedir = ["Nombre", "Apellido", "Dirección", "Color de casa", "Método de pago (Efectivo/Tarjeta)"]
    
    for encabezado in datos_a_pedir:
        while True:
            dato = input(f"{encabezado}: ").strip().lower()
            if dato == "":
                print(MENSAJES['espacio_vacio'])
                continue

            
            if validar_numero(dato):
                print(MENSAJES['numero_no_permitido'])
                continue
            else:
                if validacion_entrada(dato):
                    print(MENSAJES['cantidad_negativa'])
                    continue
                elif encabezado == "Método de pago (Efectivo/Tarjeta)":
                        if dato == "e" or dato == "t":
                            pago = obtener_pago(dato)
                            datos_cliente.append({encabezado: pago}) 
                            break
                        else:
                            print(MENSAJES['metodo_pago_invalido'])
                            continue
                else:
                    datos_cliente.append({encabezado: dato}) 
                    break
                        
                            
    limpiar_pantalla()
    generar_factura(cliente=datos_cliente, pedidos=obtener_pedido())
    datos_cliente.clear()

def validacion_entrada(dato):
    try:
        int(dato)
        return True
    except ValueError:
        return False

def validar_numero(dato):
    return dato.isdigit()

def obtener_pago(pago):
    if pago == "e" or pago == "E":
        return "Efectivo"
    else:
        return "Tarjeta"