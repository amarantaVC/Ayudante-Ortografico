#! /usr/bin/python3
"""
Archivo: prueba _ortografia.py

Programa cliente que proporciona al usuario un menu simple que permite trabajar con las operaciones del TAD Ayudante Ortografico.

Autor:
#   Estudiante: Amaranta Villegas
#   Carnet: 16-11247
# Ultima modificación 16/04/2021

Proyecto2: Ayudante Ortografico 
prof : Guillermo Palma
"""
import ayudante_ortografico
from ayudante_ortografico import*
import getopt
import sys 
print("¡¡¡ BIENVENIDO AL AYUDANTE ORTOGRAFICO !!!")
print()
print()

def ElegirOpcion():
    correcto = False
    opciones = 0
    while(not correcto):
        try:
            opciones = int(input("Introduza su opcion:"))
            correcto = True
        except ValueError:
            print("Error, por favor introduzca un numero entre el 1 y 6 para elegir una opcion")
        
    return opciones

salir = False
opcion = 0

while not salir:
    print("1. Crear un nuevo Ayudante ortografico")
    print()
    print("2. Cargar un diccionario")
    print()
    print("3. Eliminar palabra")
    print()
    print("4. Corregir Texto")
    print()
    print("5. Mostrar diccinario")
    print()
    print("6. Salir de la aplicacion")
    print()
    print("Por favor, elija una opcion")
    print()

    opcion = ElegirOpcion()
    a = Ayudante_Ortografico()

    if opcion == 1:
        a.crearAyudante()
        
    if opcion == 2:
        args = sys.argv[1]
        a.cargarDiccionario(args)


    elif opcion == 3:
        palabra = str(input("ingrese la palabra a borrar:"))
        a.borrarPalabra(palabra)
    
    elif opcion == 4:
        #preguntaar lo de la opcion 4 de como hacer si no se ha cargado diccionario 
        a.cargarDiccionario("prueba.txt")
        a.corregirTexto("corregir.txt")
        sys.exit()
    
    elif opcion == 5:
        a.imprimirDiccionario()
    
    elif opcion == 6:
        salir = True

    else:
        print("introduzca un numero entero")

print(" Adios ")