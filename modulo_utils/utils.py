# Importaciones necesarias para las funciones de utilidad
import os
from datetime import datetime

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Funciona tanto en Windows (cls) como en sistemas Unix (clear).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def input_numero(mensaje):
    """
    Captura y valida entrada numérica del usuario.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        
    Returns:
        int: Número válido ingresado por el usuario
    """
    while True:
        valor = input(mensaje)
        # Valida que el campo no esté vacío
        if valor.strip() == '':
            print('¡El campo no puede estar vacío!')
            continue
        try:
            return int(valor)
        except ValueError:
            print('Solo se permiten números.')

def input_fecha(mensaje):
    """
    Captura y valida una fecha en formato YYYY-MM-DD.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        
    Returns:
        date: Fecha válida ingresada por el usuario
    """
    while True:
        valor = input(mensaje)
        try:
            return datetime.strptime(valor, '%Y-%m-%d').date()
        except ValueError:
            print('Fecha inválida. Usa el formato YYYY-MM-DD.')

def input_si_no(mensaje):
    """
    Captura una respuesta de sí/no del usuario.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        
    Returns:
        bool: True para sí, False para no
    """
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif valor in ['n', 'no']:
            return False
        else:
            print("Por favor, responde con 'sí' o 'no'.") 