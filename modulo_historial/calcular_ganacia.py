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

def filtrar_ganancias(fechas):
    fecha_inicio = fechas[0]
    fecha_fin = fechas[1]
    ventas_por_fecha = {}

    with open(ARCHIVO_VENTAS,"r") as ventas:
        for linea in ventas:
            venta = json.loads(linea)

            db_fecha = convertir_cadena_a_datetime(venta=venta["fecha"])

            if fecha_inicio <= db_fecha <= fecha_fin:
                fecha_str = venta["fecha"]
                if fecha_str not in ventas_por_fecha:
                    ventas_por_fecha[fecha_str] = {
                        "detalles":[],
                        "subtotal":0
                    }
                for item in venta["pedido"]:
                    subtotal = item["precio_unitario"] * item["cantidad"]
                    ventas_por_fecha[fecha_str]["subtotal"] += subtotal
                    ventas_por_fecha[fecha_str]["detalles"].append(
                        f"- {item["producto"]} x {item["cantidad"]} = {subtotal:.2f}"
                    )
                    
                
    if ventas_por_fecha:
        print("\n" + MENSAJES['detalle_ventas'])
        for fecha, venta in ventas_por_fecha.items():
            print(f"\nFecha: {fecha}")
            for d in venta["detalles"]:
                print(d)
            print(f"Subtotal venta: ${venta["subtotal"]:.2f}")
            print("\n---------------------------------------")
        print(MENSAJES["total_ganado"].format(total=sum(d["subtotal"] for d in ventas_por_fecha.values())))
    else:
        print(MENSAJES['no_ventas_periodo'])

def convertir_cadena_a_datetime(venta):
    return datetime.strptime(venta, "%Y-%m-%d").date()



