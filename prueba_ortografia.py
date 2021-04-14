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
print("-------------------------------------------------------------------")
print("             Bienvenido al Ayudante Ortografico ")
print("-------------------------------------------------------------------")
print()
print()

def ElegirOpcion():
    correcto = False
    opciones = 0
    while(not correcto):
        try:
            opciones = int(input("Introduzca su opcion:"))
            #print(f"Usted seleccionó la opcion {opciones } ")
            correcto = True
        except ValueError:
            print("-------------------------------------------------------------------")
            print("Error, por favor introduzca un numero entre el 1 y 6 para elegir una opcion")
            print("-------------------------------------------------------------------")
    return opciones

salir = False
opcion = 0
a = None
b = False
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
    print()
    

    if opcion == 1:
        a = Ayudante_Ortografico()
        print("-------------------------------------------------------------------")
        print(  "Ayudante ortografico creado con exito")
        print("-------------------------------------------------------------------")

    if opcion == 2:
        if a == None:
            print("-------------------------------------------------------------------")
            print("Error: No se ha creado un Ayudante. Por favor cree uno e intente de nuevo.")
            print("-------------------------------------------------------------------")
        
        else:
            diccionario = input("Ingrese el diccionario a cargar:")
            print("-------------------------------------------------------------------")
            print(f"Diccionario {diccionario} cargado con exito")
            print("-------------------------------------------------------------------")
            b = a.cargarDiccionario(diccionario) 


            if b == False:
                print("-------------------------------------------------------------------")
                print(f"Error: {diccionario} No es un diccionario válido. Inténte de nuevo")
                print("-------------------------------------------------------------------")
            else:
                pass

    if opcion == 3:
        if a == None:
            print("-------------------------------------------------------------------")
            print("Error: No se ha creado un Ayudante. Por favor cree uno e intente de nuevo.")
            print("-------------------------------------------------------------------")
        
        else:
            if b == True:
                palabra = input("ingrese la palabra a borrar:")
                borrar = a.borrarPalabra(palabra)

            else:
                print("-------------------------------------------------------------------")
                print("Error: No se ha cargado un diccionario válido. Inténte de nuevo.")
                print("-------------------------------------------------------------------")

    
    if opcion == 4:
        if a == None:
            print("-------------------------------------------------------------------")
            print("Error: No se ha creado un Ayudante. Por favor cree uno e intente de nuevo.")
            print("-------------------------------------------------------------------")
        
        else:
            if b:
                b = a.cargarDiccionario(diccionario)
                texto = input("ingrese el archivo a corregir:")
                print("-------------------------------------------------------------------")
                print(f"archivo {texto} cargado con exito")
                print("-------------------------------------------------------------------")
                a.corregirTexto(texto)
                
            else:
                print("-------------------------------------------------------------------")
                print("Error: No se ha cargado un diccionario válido. Inténte de nuevo.")
                print("-------------------------------------------------------------------")


    if opcion == 5:
        if a == None:
            print("-------------------------------------------------------------------")
            print("Error: No se ha creado un Ayudante. Por favor cree uno e intente de nuevo.")
            print("-------------------------------------------------------------------")
            
        else:
            if b:
                a.imprimirDiccionario()
            else:
                print("-------------------------------------------------------------------")
                print("Error: No se ha cargado un diccionario válido. Inténte de nuevo.")
                print("-------------------------------------------------------------------")

    if opcion == 6:
        salir = True

    else:
        print()
        print("introduzca una opcion")
        print()
print("-------------------------------------------------------------------")
print("Usted ha salido del Ayudante Ortografico")
print("-------------------------------------------------------------------")