"""
Archivo: esPalabraValida.py

contiene una funcion que verifica si un elemento de tipo sting es una palabra valida, es decir que esta formado con caracateres alfabeticos en minuscula

Autor:
#   Estudiante: Amaranta Villegas
#   Carnet: 16-11247
# Ultima modificación 16/04/2021

Proyecto2: Ayudante Ortografico 
prof : Guillermo Palma
"""
import string


def esPalabraValida(p):
    alfabeto = list(string.ascii_lowercase)
    alfabeto.append('ñ')
    valida = True
    for i in p:
        if i in alfabeto:
            pass
        else:
            valida = False
            break
    return valida

   
