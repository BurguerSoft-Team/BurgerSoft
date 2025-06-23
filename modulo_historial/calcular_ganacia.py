from modulo_guardar.guardar_datos import verificar_archivo
from datetime import datetime
from pathlib import Path
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import input_fecha, limpiar_pantalla, input_si_no
import json

ARCHIVO_VENTAS = Path(__file__).resolve().parent.parent / "ventas.txt"
def historial():
    while True:
        limpiar_pantalla()
        print(MENSAJES['historial_ganancias'])
        
        
        encabezados = ["Ingrese la fecha de inicio (YYYY-MM-DD):", "Ingrese la fecha de fin (YYYY-MM-DD): "]
        fechas = []
        for encabezado in encabezados:
            fechas.append(input_fecha(encabezado))

        if fechas[1] < fechas[0]:
            fechas.clear()
            print(MENSAJES['fecha_fin_menor'])
            continue

        
        if not verificar_archivo():
            print(MENSAJES['base_datos_vacia'])
        else:
            filtrar_ganancias(fechas)
        
        print("\n" + "=" * 50)
        if input_si_no("¿Deseas hacer otra consulta de historial? (sí/no): "):
            continue
        else:
            break

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
    ventas_en_periodo = []

    with open(ARCHIVO_VENTAS, "r") as ventas:
        for linea in ventas:
            venta = json.loads(linea)
            db_fecha = convertir_cadena_a_datetime(venta=venta["fecha"])

            if fecha_inicio <= db_fecha <= fecha_fin:
                subtotal = 0
                detalles = []
                for item in venta["pedido"]:
                    item_total = item["precio_unitario"] * item["cantidad"]
                    subtotal += item_total
                    detalles.append(f"- {item['producto']} x{item['cantidad']} = ${item_total:.2f}")
                ventas_en_periodo.append({
                    "fecha": venta["fecha"],
                    "detalles": detalles,
                    "subtotal": subtotal
                })
                total += subtotal

    if ventas_en_periodo:
        print("\n" + MENSAJES['detalle_ventas'])
        for v in ventas_en_periodo:
            print(f"\nFecha: {v['fecha']}")
            for d in v["detalles"]:
                print(d)
            print(f"Subtotal venta: ${v['subtotal']:.2f}")
        print("\n---------------------------------------")
        print(MENSAJES['total_ganado'].format(total=total))
    else:
        print(MENSAJES['no_ventas_periodo'])
    

def convertir_cadena_a_datetime(venta):
    return datetime.strptime(venta, "%Y-%m-%d").date()



