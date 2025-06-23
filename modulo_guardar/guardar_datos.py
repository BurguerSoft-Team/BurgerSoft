import os
import json
from datetime import date



ARCHIVO_VENTAS = "ventas.txt"

def verificar_archivo():
    return os.path.exists(ARCHIVO_VENTAS)

def leer_archivo():
    try:
        with open(ARCHIVO_VENTAS, "r") as f:
            lineas = f.readlines()
            return len(lineas) + 1
    except FileNotFoundError:
        return 1

def agregar_pedido(cliente, orden, codigo):
    pedido = {
        "codigo": codigo,
        "cliente": cliente,
        "pedido": orden,
        "fecha": str(date.today())
    }
    with open(ARCHIVO_VENTAS, "a") as venta:
        venta.write(json.dumps(pedido) + "\n")

def crear_archivo():
    with open(ARCHIVO_VENTAS, "w"):
        pass

def gestionar_operaciones(cliente,pedido):
    if not verificar_archivo():
        crear_archivo()
    codigo = leer_archivo()
    agregar_pedido(cliente,pedido,codigo)


