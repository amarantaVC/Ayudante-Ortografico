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
        archivo = open(fname,"r")
        with archivo as fp: 
            #readlines lee las lineas del archivo
            dicci = fp.readlines()
        for linea in dicci:
            #strip quita los espacios
            linea = linea.strip()
            #linea[0] significa primera letra de la palabra
            #index entrega la posicion para obtener el PMLI del diccionario
            index = self.alfabeto.index(linea[0])
            buscar = self.dicc[index].buscarPalabra(linea)
            if buscar == False:

                self.dicc[index].agregarPalabra(linea)
            else:
                pass

    def borrarPalabra(self,p):
        assert(esPalabraValida(p) == True)
        index = self.alfabeto.index(p[0])
        self.dicc[index].eliminarPalabra(p)

    def corregirTexto(self,finput):
        archivo = open(finput,"r")
        with archivo as fp:
            documento = fp.readlines()
        for linea in documento:
            #devuelve una lista con las palabras en el string, utilizando un separador #especificado como delimitador entre palabras
            linea = linea.split()
            for palabra in linea:
                valida = esPalabraValida(palabra)
                index = self.alfabeto.index(palabra[0])
                buscar = self.dicc[index].buscarPalabra(palabra)
                if valida == True and buscar == True:
                    pass
                else:
                    pass
        



    def __str__(self):
        return f"{self.dicc}"


a = Ayudante_Ortografico()
a.cargarDiccionario('prueba.txt')

#a.borrarPalabra("preso")
#a.corregirTexto("corregir.txt")

for diccionario in a.dicc:
    if diccionario.palabras:
        diccionario.mostrarPalabras()
