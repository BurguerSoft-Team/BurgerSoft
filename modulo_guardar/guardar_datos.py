# Importaciones necesarias para el manejo de archivos y fechas
import os
import json
from datetime import date

# Nombre del archivo donde se guardan las ventas
ARCHIVO_VENTAS = "ventas.txt"

def verificar_archivo():
    """
    Verifica si existe el archivo de ventas.
    
    Returns:
        bool: True si el archivo existe, False en caso contrario
    """
    return os.path.exists(ARCHIVO_VENTAS)

def obtener_codigo():
    """
    Obtiene el siguiente código disponible para una nueva venta.
    
    Returns:
        int: Código único para la nueva venta
    """
    try:
        # Cuenta las líneas existentes y suma 1 para el nuevo código
        with open(ARCHIVO_VENTAS, "r") as f:
            lineas = f.readlines()
            return len(lineas) + 1
    except FileNotFoundError:
        # Si el archivo no existe, comienza con código 1
        return 1

def agregar_pedido(cliente, orden, codigo):
    """
    Agrega un nuevo pedido al archivo de ventas.
    
    Args:
        cliente: Nombre del cliente
        orden: Lista con los productos del pedido
        codigo: Código único de la venta
    """
    # Crea el diccionario con los datos de la venta
    pedido = {
        "codigo": codigo,
        "cliente": cliente,
        "pedido": orden,
        "fecha": str(date.today())
    }
    
    # Escribe la venta en formato JSON al archivo
    with open(ARCHIVO_VENTAS, "a") as venta:
        venta.write(json.dumps(pedido) + "\n")

def crear_archivo():
    """
    Crea el archivo de ventas si no existe.
    """
    with open(ARCHIVO_VENTAS, "w"):
        pass

def gestionar_operaciones(cliente,pedido):
    """
    Función principal para gestionar el guardado de operaciones.
    
    Args:
        cliente: Nombre del cliente
        pedido: Lista con los productos del pedido
    """
    # Verifica si existe el archivo, si no, lo crea
    if not verificar_archivo():
        crear_archivo()
    
    # Agrega el pedido con un código único
    agregar_pedido(cliente,pedido,codigo=obtener_codigo())


