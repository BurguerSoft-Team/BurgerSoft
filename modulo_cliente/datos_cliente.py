# Importaciones necesarias para el módulo de cliente
import os
from modulo_factura.calculo_factura import generar_factura
from modulo_pedido.menu import obtener_pedido
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import limpiar_pantalla, input_si_no

# Lista global para almacenar los datos del cliente
datos_cliente = []

def capturar_datos_cliente(limpiar):
    """
    Captura y valida los datos del cliente para el pedido.
    
    Args:
        limpiar: Booleano que indica si limpiar datos anteriores
    """
    # Limpia los datos si se solicita
    if limpiar:
        datos_cliente.clear()

    # Muestra el encabezado para datos del cliente
    print("=" * 30)
    print(f"   {MENSAJES['datos_cliente']}   ")
    print("=" * 30)
    
    # Lista de campos que se deben capturar
    datos_a_pedir = ["Nombre", "Apellido", "Dirección", "Color de casa", "Método de pago (Efectivo/Tarjeta)"]
    
    # Captura cada campo con validación
    for encabezado in datos_a_pedir:
        while True:
            dato = input(f"{encabezado}: ").strip().lower()
            
            # Valida que el campo no esté vacío
            if dato == "":
                print(MENSAJES['espacio_vacio'])
                continue

            # Valida que no contenga solo números
            if validar_numero(dato):
                print(MENSAJES['numero_no_permitido'])
                continue
            else:
                # Valida que no sea un número negativo
                if validacion_entrada(dato):
                    print(MENSAJES['cantidad_negativa'])
                    continue
                elif encabezado == "Método de pago (Efectivo/Tarjeta)":
                    # Validación especial para método de pago
                    if dato == "e" or dato == "t":
                        pago = obtener_pago(dato)
                        datos_cliente.append({encabezado: pago}) 
                        break
                    else:
                        print(MENSAJES['metodo_pago_invalido'])
                        continue
                else:
                    # Agrega el dato válido a la lista
                    datos_cliente.append({encabezado: dato}) 
                    break
                        
    # Genera la factura con los datos capturados
    limpiar_pantalla()
    generar_factura(cliente=datos_cliente, pedidos=obtener_pedido())
    datos_cliente.clear()

def validacion_entrada(dato):
    """
    Valida si la entrada es un número.
    
    Args:
        dato: String a validar
        
    Returns:
        bool: True si es un número, False en caso contrario
    """
    try:
        int(dato)
        return True
    except ValueError:
        return False

def validar_numero(dato):
    """
    Verifica si la entrada contiene solo dígitos.
    
    Args:
        dato: String a validar
        
    Returns:
        bool: True si contiene solo dígitos, False en caso contrario
    """
    return dato.isdigit()

def obtener_pago(pago):
    """
    Convierte la entrada del método de pago a texto descriptivo.
    
    Args:
        pago: String con la entrada del usuario ('e' o 't')
        
    Returns:
        str: "Efectivo" o "Tarjeta" según la entrada
    """
    if pago == "e" or pago == "E":
        return "Efectivo"
    else:
        return "Tarjeta"