
from gestion_operaciones import verificar_archivo
from gestion_operaciones import ARCHIVO_VENTAS
from datetime import datetime
import json

def historial():
    print("Historial de ganacias \n")
    while True:
        encabezados = ["Ingrese la fecha de inicio (YYYY-MM-DD):", "Ingrese la fecha de fin (YYYY-MM-DD): "]
        fechas = []
        for encabezado in encabezados:
            while True:
                dato = pedir_fecha(message=encabezado)
                if dato != "":
                    fechas.append(dato)
                    break
        # Verifica que la fecha de fin no sea menor que la de inicio
        if fechas[1] < fechas[0]:
            fechas.clear()
            print("La fecha de fin no puede ser menor que la fecha de inicio. Intenta de nuevo.\n")
            continue
        break

    if not verificar_archivo():
        print("La base de datos esta vacia!")
    else:
        filtrar_ganancias(fechas)
def pedir_fecha(message):
    while True:
        fecha_str = input(message)
        try:
            fecha = convertir_cadena_a_datetime(fecha_str)
            return fecha
        except ValueError:
            print("Fecha inválida. Usa el formato YYYY-MM-DD.")


def filtrar_ganancias(fechas):
    fecha_inicio = fechas[0]
    fecha_fin = fechas[1]

    total = 0

    with open(ARCHIVO_VENTAS,"r") as ventas:
        for linea in ventas:
            venta = json.loads(linea)
            db_fecha = convertir_cadena_a_datetime(venta=venta["fecha"])

            if fecha_inicio <= db_fecha <= fecha_fin:
                for item in venta["pedido"]:
                    total += item["precio_unitario"] * item["cantidad"]
    print("El total es: ",total)
            


def convertir_cadena_a_datetime(venta):
    return datetime.strptime(venta, "%Y-%m-%d").date()

if __name__ == "__main__":
    historial()

