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
import numpy as np
from numpy import*
import collections

"Ayudante_Ortografico es un TAD que posee un arreglo con 27 PMLI que corresponde a cada letra del alfabeto latin y tiene como funcion almacenar las palabras del diccionario que se van a usar "
class Ayudante_Ortografico(object):
    
    assert(True)
    #inciailizamos la estructura dicc con las 27 instancias de PMLI
    def __init__(self):
        self.alfabeto = list(string.ascii_lowercase)
        self.alfabeto.append('ñ')
        self.MAX = 27
        self.dicc = [PMLI(letra) for letra in self.alfabeto]
    
    def crearAyudante(self) -> "Ayudante_Ortografico":
        return self

    "cargarDiccionario tiene la tarea de leer un archivo de entrada con las palabras de un diccionario y almacenarlas en la estructura dicc"
    #{pre: fn}
    def cargarDiccionario(self, fname):
        archivo = open(fname,"r")
        with archivo as fp: 
            #readlines lee las lineas del archivo
            dicci = fp.readlines()

        for linea in dicci:

            linea = linea.strip()

            if esPalabraValida(linea) :
                    #strip quita los espacios
                    #linea[0] significa primera letra de la palabra
                    #index entrega la posicion para obtener el PMLI del diccionario
                    index = self.alfabeto.index(linea[0])
                    buscar = self.dicc[index].buscarPalabra(linea)
                    if buscar == False:

                        self.dicc[index].agregarPalabra(linea)
                    else:
                        pass
            else:
                print(f"archivo invalido por palabra no valida: {linea}")    
    
    "borrarPalabra tiene como tarea recibir una palabra y verificar si esta se encuentra en la estructura dicc, si esto es verdad procede a eliminar la palabra "
    def borrarPalabra(self,p):
        #precondicion
        assert(esPalabraValida(p) == True)

        index = self.alfabeto.index(p[0])
        self.dicc[index].eliminarPalabra(p)

    def levenshtein_distance(self,s1,s2):
        size_s1 = len(s1) + 1
        size_s2 = len(s2) +1

        m = np.zeros((size_s1,size_s2))
        
        for i in range(size_s1):
            m[i,0] = i
        
        for j in range(size_s2):
            m[0,j] = j 

        for i in range(1,size_s1):
            for j in range(1,size_s2):
                if s1[i-1] == s2[j-1]:
                    diferencia = 0
                else:
                    diferencia = 1
                imenos1 = m[i-1,j] + 1 #[i-1,j]
                imenos1_jmenos1 = m[i-1,j-1] + diferencia #[i-1,j-1]
                jmenos1 = m[i,j-1] + 1 #[i,j-1]
                m[i,j] = min(imenos1,imenos1_jmenos1,jmenos1)
        return (int(m[size_s1 - 1, size_s2 - 1]))
    
    "corregirTexto recibe como entrada un archivo co"
    def corregirTexto(self,finput):
        archivo = open(finput,"r")
        with archivo as fp:
            documento = fp.readlines()
        NoDicc = []
        for linea in documento:
            #devuelve una lista con las palabras en el string, utilizando un separador #especificado como delimitador entre palabras
            linea = linea.strip('\n').split(" ")
            
            for palabra in linea:  
                valida = esPalabraValida(palabra)
                if valida == True :
                    index = self.alfabeto.index(palabra[0])
                    buscar = self.dicc[index].buscarPalabra(palabra)
                    if buscar == False and (palabra not in NoDicc):

                        NoDicc.append(palabra)
                    else:
                        pass
                        """
                        m = self.sugerencia()
                        for i in range(len(m)):
                            y = self.levenshtein_distance(palabra,m[i-1])
                            w = self.levenshtein_distance(palabra,m[i])
                        """
        NoDicc = sorted(NoDicc)
        
        for palabra in NoDicc:
            print()
            print("palabra", palabra)
            print()
            self.sugerencia(palabra)

                                       
        
    
    def sugerencia(self,elemento:str):

        Arreglo = []           
        for diccionario in self.dicc:
            for palabra in diccionario.palabras.tabla:
                if palabra != None:
                    Arreglo.append(palabra)
        
        sugerencia = []

        for i in range(len(Arreglo)):
            # = self.levenshtein_distance(elemento,Arreglo[i-1])
            w = self.levenshtein_distance(elemento,Arreglo[i])
            sugerencia.append((Arreglo[i],w))
        sugerencia.sort(key = lambda x: x[1])
        print(sugerencia)
        print()
        Orden = [a for (a,b) in sugerencia]
        print(Orden)


    def __str__(self):
        return f"{self.dicc}"


a = Ayudante_Ortografico()

a.cargarDiccionario('prueba.txt')

a.levenshtein_distance("Amaranta","barbara")
#a.borrarPalabra("maria")
a.sugerencia("auto")
a.corregirTexto("corregir.txt")
#for diccionario in a.dicc:
    #if diccionario.palabras:
        #diccionario.mostrarPalabras()
