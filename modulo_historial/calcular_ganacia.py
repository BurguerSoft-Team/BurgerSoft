# Importaciones necesarias para el módulo de historial
from modulo_guardar.guardar_datos import verificar_archivo
from datetime import datetime
from pathlib import Path
from modulo_utils.mensajes import MENSAJES
from modulo_utils.utils import input_fecha, limpiar_pantalla, input_si_no
import json

# Ruta al archivo de ventas
ARCHIVO_VENTAS = Path(__file__).resolve().parent.parent / "ventas.txt"

def historial():
    """
    Función principal para mostrar el historial de ganancias.
    Permite al usuario seleccionar un rango de fechas para consultar.
    """
    while True:
        # Limpia pantalla y muestra encabezado
        limpiar_pantalla()
        print(MENSAJES['historial_ganancias'])
        
        # Captura las fechas de inicio y fin
        encabezados = ["Ingrese la fecha de inicio (YYYY-MM-DD):", "Ingrese la fecha de fin (YYYY-MM-DD): "]
        fechas = []
        for encabezado in encabezados:
            fechas.append(input_fecha(encabezado))

        # Valida que la fecha de fin no sea menor que la de inicio
        if fechas[1] < fechas[0]:
            fechas.clear()
            print(MENSAJES['fecha_fin_menor'])
            continue

        # Verifica si existe el archivo de ventas
        if not verificar_archivo():
            print(MENSAJES['base_datos_vacia'])
        else:
            # Filtra y muestra las ganancias del periodo
            filtrar_ganancias(fechas)
        
        # Pregunta si desea hacer otra consulta
        print("\n" + "=" * 50)
        if input_si_no("¿Deseas hacer otra consulta de historial? (sí/no): "):
            continue
        else:
            break

def filtrar_ganancias(fechas):
    """
    Filtra las ventas por rango de fechas y calcula las ganancias.
    
    Args:
        fechas: Lista con fecha de inicio y fin
    """
    fecha_inicio = fechas[0]
    fecha_fin = fechas[1]
    ventas_por_fecha = {}

    # Lee el archivo de ventas y filtra por fechas
    with open(ARCHIVO_VENTAS,"r") as ventas:
        for linea in ventas:
            venta = json.loads(linea)

            # Convierte la fecha de la venta para comparación
            db_fecha = convertir_cadena_a_datetime(venta=venta["fecha"])

            # Filtra ventas dentro del rango de fechas
            if fecha_inicio <= db_fecha <= fecha_fin:
                fecha_str = venta["fecha"]
                if fecha_str not in ventas_por_fecha:
                    ventas_por_fecha[fecha_str] = {
                        "detalles":[],
                        "subtotal":0
                    }
                
                # Calcula subtotales por producto
                for item in venta["pedido"]:
                    subtotal = item["Total"]
                    ventas_por_fecha[fecha_str]["subtotal"] += subtotal
                    ventas_por_fecha[fecha_str]["detalles"].append(
                        f"- {item["producto"]} x {item["cantidad"]} = {subtotal:.2f}"
                    )
                    
    # Muestra los resultados filtrados
    if ventas_por_fecha:
        print("\n" + MENSAJES['detalle_ventas'])
        for fecha, venta in ventas_por_fecha.items():
            print(f"\nFecha: {fecha}")
            for d in venta["detalles"]:
                print(d)
            print(f"Subtotal venta: ${venta["subtotal"]:.2f}")
            print("\n---------------------------------------")
        
        # Muestra el total ganado en el periodo
        total_periodo = sum(d["subtotal"] for d in ventas_por_fecha.values())
        print(MENSAJES["total_ganado"].format(total=total_periodo))
    else:
        print(MENSAJES['no_ventas_periodo'])

def convertir_cadena_a_datetime(venta):
    """
    Convierte una cadena de fecha a objeto datetime.
    
    Args:
        venta: String con la fecha en formato YYYY-MM-DD
        
    Returns:
        date: Objeto fecha para comparaciones
    """
    return datetime.strptime(venta, "%Y-%m-%d").date()



