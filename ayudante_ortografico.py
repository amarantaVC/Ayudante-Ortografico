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
import time 
from time import perf_counter
"Ayudante_Ortografico es un TAD que posee un arreglo con 27 PMLI que corresponde a cada letra del alfabeto latin y tiene como funcion almacenar las palabras del diccionario que se van a usar "
class Ayudante_Ortografico(object):
    
    
    "crearAyudante tiene la tarea de crear un nuevo TAD Ayudante Ortogradico en donde la estructura de datos dicc se inicializa "
    #inciailizamos la estructura dicc con las 27 instancias de PMLI
    def __init__(self):
        self.alfabeto = list(string.ascii_lowercase)
        self.alfabeto.append('ñ')
        self.MAX = 27
        self.dicc = [PMLI(letra) for letra in self.alfabeto]
   
    "cargarDiccionario tiene la tarea de leer un archivo de entrada con las palabras de un diccionario y almacenarlas en la estructura dicc"
    
    def cargarDiccionario(self, fname):
        try:
            archivo = open(fname,"r")
            cargo = True
            with archivo as fp: 
                #readlines lee las lineas del archivo
                dicci = fp.readlines()
            
            for linea in dicci:
                #preguntarRR 
                linea = linea.strip()
                #precondicion
                if esPalabraValida(linea) :
                        #strip quita los espacios
                        #linea[0] significa primera letra de la palabra
                        #index entrega la posicion para obtener el PMLI del diccionario
                        index = self.alfabeto.index(linea[0])
                        buscar = self.dicc[index].buscarPalabra(linea)
                        if buscar == False:
                            #postcondicion
                            self.dicc[index].agregarPalabra(linea)
                        else:
                            pass
                else:
                    print(f"archivo invalido por palabra no valida: {linea}")    
            
            return cargo

        except FileNotFoundError:
            cargo = False
            return cargo
    "borrarPalabra tiene como tarea recibir una palabra y verificar si esta se encuentra en la estructura dicc, si esto es verdad procede a eliminar la palabra "
    def borrarPalabra(self,p):
        #precondicion
        assert(esPalabraValida(p) == True)

        index = self.alfabeto.index(p[0])


        self.dicc[index].eliminarPalabra(p)

    "levenshtein_distance es el metodo que permite determinar la distancia entre dos elementos tipo String mediante la metrica de conocida como distancia levenshtein"
    def levenshtein_distance(self,s1:str,s2:str):
        
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

    "corregirTexto recibe como entrada un archivo con palabras a revisar y extrae unicamente las palabras validas que se encuentren en el texto y si no se encuentran en el diccionario retornar un archivo con la palabra que no se encuentra en el diccionario y 4 palabras con la menor distancia levenstein las cuales seran las que el programa considere como sugerencias."
    def corregirTexto(self,finput):
        
        archivo = open(finput,"r")
        with archivo as fp:
            documento = fp.readlines()
        #creamos un arreglo NoDicc que almacena las palabras validas que no se encuentre en el diccionario    
        NoDicc = []
        for linea in documento:
            #devuelve una lista con las palabras en el string, utilizando un separador #especificado como delimitador entre palabras
            linea = linea.strip('\n').split(" ")
            print(linea)
    
            for palabra in linea:
                if palabra == '':
                    pass
                else:
                        
                    valida = esPalabraValida(palabra)
                    if valida == True :
                        index = self.alfabeto.index(palabra[0])
                        buscar = self.dicc[index].buscarPalabra(palabra)

                        if buscar == False and (palabra not in NoDicc):

                            NoDicc.append(palabra)
                        else:
                            pass
                    else:
                        pass
        NoDicc = sorted(NoDicc)
        foutput = None
        if foutput:
            ArchivoSalida = open(foutput, "w")
        else:
            ArchivoSalida = open("foutput.txt" ,"w")

        for palabra in NoDicc:

            m = self.sugerencia(palabra)

            salida = ",".join(m)
            #escribiendo archivo de salida
            ArchivoSalida.write(f"{palabra},{salida}"+"\n")
        ArchivoSalida.close()

    "sugerencia es un metodo auxiliar que tiene como tarea devolver las  cuatro palabras con menor distancia levensthein que seran las palabras que va a sugerir el ayudante ortografico"
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

        Orden = [a for (a,b) in sugerencia]
        a = []
        for i in range(4):
            a.append(Orden[i])
        return a
    
    "imprimirDiccionario tiene como funcion mostrar las palabras del diccionario en orden lexicografico"
    def imprimirDiccionario(self):
        assert(True)
        print("#----------------Diccionario---------------#")
        for diccionario in self.dicc:
            if diccionario.palabras:
                r = (diccionario.mostrarPalabras())

    

if __name__ == "__main__":

    a = Ayudante_Ortografico()
    a.cargarDiccionario("prueba.txt")
    a.corregirTexto("corregir.txt")
    
    