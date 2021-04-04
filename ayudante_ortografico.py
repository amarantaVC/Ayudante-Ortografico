#! /usr/bin/python3
"""
Archivo: ayudante_ortografico.py

contiene a un conjunto de palabras, las cuales comienzan por una misma letra. A
continuacion se presenta la especificacion del TAD.

Autor:
#   Estudiante: Amaranta Villegas
#   Carnet: 16-11247
# Ultima modificación 16/04/2021

Proyecto2: Ayudante Ortografico 
prof : Guillermo Palma
"""
"PMLI contiene a un conjunto de palabras que comienzan por una misma letra"

import esPalabraValida
from esPalabraValida import esPalabraValida
import open_htable
from open_htable import OpenHtable
import pmli
from pmli import PMLI
import string


class Ayudante_Ortografico(object):
    

    def __init__(self):
        self.alfabeto = list(string.ascii_lowercase)
        self.alfabeto.append('ñ')
        self.MAX = 27
        self.dicc = [PMLI(letra) for letra in self.alfabeto]
    
    def cargarDiccionario(self, fname):
        self.dicc
        archivo = open(fname,"r")
        with archivo as fp: 
            for linea in (fp.readlines()):
                print(linea)
                if esPalabraValida(linea):
                    pass
                else:
                    pass



    def __str__(self):
        return f"{self.dicc}"


a = Ayudante_Ortografico()
a.cargarDiccionario('prueba.txt')
print(a)