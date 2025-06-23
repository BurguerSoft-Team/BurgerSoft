import os
from datetime import datetime

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() == '':
            print('¡El campo no puede estar vacío!')
            continue
        try:
            return int(valor)
        except ValueError:
            print('Solo se permiten números.')

def input_fecha(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return datetime.strptime(valor, '%Y-%m-%d').date()
        except ValueError:
            print('Fecha inválida. Usa el formato YYYY-MM-DD.')

def input_si_no(mensaje):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif valor in ['n', 'no']:
            return False
        else:
            print("Por favor, responde con 'sí' o 'no'.") 