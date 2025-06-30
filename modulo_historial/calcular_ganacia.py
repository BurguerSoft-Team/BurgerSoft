from modulo_guardar.guardar_datos import verificar_archivo
from datetime import datetime
from pathlib import Path
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import input_fecha, limpiar_pantalla, input_si_no
import json

ARCHIVO_VENTAS = Path(__file__).resolve().parent.parent / "ventas.txt"

def filtrar_ganancias(fechas):
    fecha_inicio = fechas[0]
    fecha_fin = fechas[1]

    total = 0
    ventas_por_fecha = {}

    with open(ARCHIVO_VENTAS, "r") as ventas:
        for linea in ventas:
            venta = json.loads(linea)
            db_fecha = convertir_cadena_a_datetime(venta=venta["fecha"])

            if fecha_inicio <= db_fecha <= fecha_fin:
                fecha_str = venta["fecha"]
                if fecha_str not in ventas_por_fecha:
                    ventas_por_fecha[fecha_str] = {
                        "detalles": [],
                        "subtotal": 0
                    }
                for item in venta["pedido"]:
                    item_total = item["precio_unitario"] * item["cantidad"]
                    ventas_por_fecha[fecha_str]["subtotal"] += item_total
                    ventas_por_fecha[fecha_str]["detalles"].append(
                        f"- {item['producto']} x{item['cantidad']} = ${item_total:.2f}"
                    )
                total += ventas_por_fecha[fecha_str]["subtotal"]

    if ventas_por_fecha:
        print("\n" + MENSAJES['detalle_ventas'])
        for fecha, datos in ventas_por_fecha.items():
            print(f"\nFecha: {fecha}")
            for d in datos["detalles"]:
                print(d)
            print(f"Subtotal venta: ${datos['subtotal']:.2f}")
            print("\n---------------------------------------")
        print(MENSAJES['total_ganado'].format(total=sum(d["subtotal"] for d in ventas_por_fecha.values())))
    else:
        print(MENSAJES['no_ventas_periodo'])

def convertir_cadena_a_datetime(venta):
    return datetime.strptime(venta, "%Y-%m-%d").date()



