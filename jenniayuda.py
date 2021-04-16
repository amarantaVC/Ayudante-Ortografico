#!/usr/bin/env python
# Python3 
#
# Propietario: Jennifer Gamez
#		   ID: 16-10396
# Editado : 08/04/2021

from pmli import PMLI       
import string
import re
import sys
from funcPalabra_Valida import esPalabraValida
from distanciaLevenshtein import editDistance
import pathlib

# Funcion
# abecedario(out alfabeto: arr) 
#   Construye un array con las letras letras del alfabeto latino 
#   incluyendo la "ñ".
def abc():
    # Precondicion
    assert(True)

    abced = list(string.ascii_lowercase)
    alfabeto = abced[:14] + ["ñ"] + abced[14:]
    return alfabeto 
    
    # Postcondicion
    #{alfabeto[0]=="a" and alfabeto[1]=="b" and ... and alfabeto[26]=="z" }

##########
#   TAD Ayudante Ortografico
#       Este TAD de ayudante orografico, carga un diccionario desde un
#       archivo . txt, ademas es capaz de de corregir un texto con palabras 
#       validas que no se encuentren en el diccionario. A cada una de 
#       las estas palabras que no estan en el diccionario, se les
#       va a buscar las palabras que les sean mas cercanas para 
#       presentarlas al usuario como recomendaciones.
##########

class ayudanteOrtografico(object):
    # crearAyudante(out dicc: arr)
    #   Constructor del ayudante ortografico, construye 27 instancias
    #   una por cada letra del alfabeto.
    def __init__(self):
        # Precondicion
        assert(True)

        # 27 instancias (27 letras alfabeto latino, incluye la ñ )
        self.MAX = 27

        self.alfabeto = abc()
        self.dicc = [] 

        for i in range(self.MAX):
            seccionDicc = PMLI(self.alfabeto[i])
            self.dicc.append(seccionDicc)
        
        print("\tAyudante ortográfico creado con éxito.")

        # Postcondicion
        # Queda inicializa la estructura dicc creando las 27 
        # instancias de TAD PMLI, una para cada letra del alfabeto.

    # cargarDiccionario(in fname: str, in-out dicc : arr)
    #   Lee un archivo de texto .txt que contiene las palabras de un 
    #   diccionario, las cuales van a ser almacenadas en la estructura 
    #   de datos dicc.
    #   Casos en donde el archivo no es valido o no existe aborta el proceso
    #   de cargar TAD dicc.
    #   fname : nombre del archivo.
    def cargarDiccionario(self, fname:str):
        
        # Precondicion. 
        #   Archivo valido .txt, existe, y una palabra por linea.
        #   Las palabras son validas, sin tabulaciones ni saltos de lineas.
        try:
            
            path = pathlib.Path(fname)
            ext = "".join(path.suffixes)

            if str(ext) != ".txt": # Evaluando extension .txt
                print("\tError: Solo es posible procesar archivos con extensión .txt ")
                return

            # Lectura del archivo desde la linea de comando
            with open(fname,"r",encoding="utf8") as f:
                
                print(f"\tEvaluando {fname}...")

                palabrasValidas = []
                lineas = f.readlines()
                for linea in lineas: 
                    l = linea.split(" ")
                    if len(l)!=1:
                        # Mas de una palabra por linea. Error.
                        print(f"\tArchivo no válido, {fname} posee tabulaciones, espacios o más de una palabra por linea.")
                        return
                    l = linea.strip('\n')
                    if l: # Evita los saltos de lineas
                        if esPalabraValida(l):
                            palabrasValidas.append(l)
                        else:
                            print(f"\tArchivo no válido, {fname} posee palabras inválidas.")
                            return
                    else:
                        # Saltos de lineas
                        print(f"\tArchivo no válido, {fname} posee saltos de lineas.")
                        return
        except FileNotFoundError as e: # Error cuando el archivo no existe
            print(f"\t{fname} no encontrado. Intente nuevamente. ")
            return

        print(f"\t{fname} válido.")

        print("\tCargando diccionario...")
        
        # Agregando palabras a dicc
        for palabra in palabrasValidas:
            ind = self.alfabeto.index(palabra[0])
            self.dicc[ind].agregarPalabra(palabra)

        print("\tDiccionario cargado.")

        # Postcondicion
        # {Quedan agregadas en dicc las palabras de fname cumpliendo 
        # la especificacion del TAD PMLI.}

    # borrarPalabra(in p:str, in-out dicc : arr)
    #   Recibe como entrada una palabra, si la misma se encuentra
    #   en dicc la elimina. Si la palabra no se encuentra en dicc 
    #   la estructura no sufre ninguna modificacion.
    def borrarPalabra(self, p:str):
        # Precondicion
        try:
            assert(esPalabraValida(p))
        except:
            print(f"\tError: Palabra: {p}, no valida")
            return
        
        letra = self.alfabeto.index(p[0])
        print(f"\t{self.dicc[letra].eliminarPalabra(p)}")

        # Postcondicion
        #assert( dicc = dicc0 - p )

    # corregirTexto(in finput: str, in dicc: arr, in-out foutput: str)
    #   Recibe como entrada un archivo de texto .txt con palabras a revisar. 
    #   Retorna un archivo con las palabras validas no contenidas en dicc
    #   seguido de sugerencias de palabras seleccionadas con la distancia 
    #   de Levenshtein.
    #   Casos en donde el archivo no es valido o no existe aborta el proceso
    #   de cargar TAD dicc.
    def corregirTexto(self, finput:str, foutput:str=None):
        
        # Precondicion. Existe el archivo y es valido.

        path = pathlib.Path(finput)
        ext = "".join(path.suffixes)

        # Es valido
        if str(ext) != ".txt": # Evaluando extension .txt 
            print("\tError: Solo es posible procesar archivos con extensión .txt ")
            return

        # LECTURA DEL ARCHIVO.
        
        try: #Existe el archivo
            archivoEnt = open(finput, 'r',encoding="utf8") # Archivo valido
            print(f"\t{finput} válido.")                
        except FileNotFoundError as e:
            print(f"\tError: {finput} no existe. Intente nuevamente.")
            return

        # DICCIONARIO CONSTRUIDO

        # Diccionario
        diccionario = []
        for seccion in self.dicc:
            if len(seccion.mostrarPalabras()) > 0:
                diccionario += seccion.mostrarPalabras()

        # Assertion. Para corregir texto deben existir palabras en dicc.
        if len(diccionario)==0: # Caso donde no hay palabras en dicc
            print("\tError: No hay un diccionario disponible a consultar.")
            return

        # CAPTANDO PALABRAS VALIDAS CONTENIDAS EN EL TEXTO

        p = [] # Palabras validas contenidas en finput
        
        print(f"\tDeterminando palabras válidas de {finput}.")
        
        lineas = archivoEnt.readlines()
        for linea in lineas:
            # Sustituye cada signo de puntuacion por un espacio
            linea= re.sub(r"[^\w\s]", " ", linea)
            # Separa el string en partes
            line = linea.strip('\n').split(" ")
            for palabra in line:
                # Analiza cada palabra valida
                if palabra and esPalabraValida(palabra) and (palabra not in p) and (palabra not in diccionario) :
                    p.append(palabra)

        archivoEnt.close() 

        # PROCESO DE CORREGIR/SUGERIR PALABRA

        # Abriendo: Archivo de salida.
        if foutput: # Caso donde se ha asignado un archivo de salida
            archivoEsc = open(foutput, "w")
        else:
            archivoEsc = open("foutput.txt", "w")

        # Calcular las cuatro palabras en el diccionario de palabras 
        # (estructura dicc), con menor valor de distancia Levenshtein.
        
        print(f"\tSugiriendo palabras del diccionario para {finput}...")
        
        for NOTinDictionary in p:

            copia = diccionario.copy()
            distanciaL = []

            for pal in copia:
                distL = editDistance(NOTinDictionary,pal)
                distanciaL.append(distL)
                
            # Buscando palabras con distancias minimas en el diccionario
            sugerirPalabras = []
            j = 0
            while j < 4:
                if distanciaL:
                    minimo = min(i for i in distanciaL)
                    ind = distanciaL.index(minimo)
                    # Palabra a sugerir
                    sugerirPalabras.append(copia[ind])
                    distanciaL.remove(distanciaL[ind])
                    copia.remove(copia[ind])
                j += 1
            
            salida = ",".join(sugerirPalabras)
            # ESCRIBIENO ARCHIVO DE SALIDA
            archivoEsc.write(f"{NOTinDictionary},{salida}"+"\n")

        print("\tSe ha terminado de sugerir palabras. Revise el archivo fountput.txt ")

        # Cerrando el archivo
        archivoEsc.close() 
        
        # Postcondicion
        # {Imprime en el archivo foutput cada una de las palabras validas contenidas
        # en el archivo finput que no se encuentren en dicc, seguidas de las cuatro 
        # palabras con menor distancia.}

    # imprimitDiccionario(in-out dicc: arr)
    #   Muestra las 27 instancias, la letra seguido de las palabras 
    #   en orden lexicografico.
    def imprimirDiccionario(self):
        # Precondicion
        assert(True)
        
        print("\t ===== [ Diccionario ] ===== ")
        print(" ")
        for seccion in self.dicc:
            #if len(seccion.mostrarPalabras()) > 0:
            print(f"[ {seccion.letra} ] -> {seccion.mostrarPalabras()} ")
        
        # Postcondicion
        # Imprime el diccionario por letra y palabras en orden lexicografico