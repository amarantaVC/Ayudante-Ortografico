#!/usr/bin/env python
# Python3 
#
# Propietario: Jennifer Gamez
#		   ID: 16-10396
# Editado : 08/04/2021

# Impotando modulos
from ayudante_ortografico import ayudanteOrtografico
import sys

########
#   Aplicacion cliente: 
#       Esta aplicacion ofrece al usario un menu simple
#       de 6 opciones disponibles por el ayudante ortografico.
#       La aplicacion del cliente de ayudante ortografico hace uso
#       de la salida estandar, al seleccionar un opcion se siguen las
#       instrucciones que dicta la aplicacion.
########

menu = True # Permite la iteracion con el usuario
ayudante = None 

while menu:
    print(" ")
    print("\t _________________________")
    print("\t|                         |")
    print("\t----- [ Aplicación ] -----")
    print("\t|_________________________|")
    print("Elija una opción:")
    print("""
    1. Crear un nuevo ayudante ortográfico.
    2. Cargar un diccionario.
    3. Eliminar palabra.
    4. Corregir texto.
    5. Mostrar diccionario.
    6. Salir de la aplicación.
    """)

    opcion = input("Opción: ")
    try:
        opcion = int(opcion)
        assert(opcion in range(1,7))
    except:
        print(" ")
        print("\tPor favor, seleccione una opción válida.")
    
    if opcion == 6: # Salir de la aplicacion
        menu = False
        print(" ")
        print("------------------ Aplicación finalizada.")

    elif opcion == 1: # Crear ayudante
        ayudante = ayudanteOrtografico()

    elif opcion == 2: # Cargar diccionario
        if ayudante:
            textoDiccionario = input("Nombre/ruta del archivo diccionario: ")
            if not textoDiccionario:
                print("Error:\t Es necesario que indique el nombre/ruta de un archivo.")
            else:
                print(" ")
                ayudante.cargarDiccionario(textoDiccionario)
        else:
            print(" ")
            print("\tEs necesario crear un ayudante ortográfico.")
            print("\tPor favor, cree un ayudante ortográfico.")

    elif opcion == 3: # Eliminar palabra
        if ayudante:
            palabraEliminar = input("Palabra a eliminar: ")
            if not palabraEliminar:
                print("Error:\t Debe introducir una palabra.")
            else:
                print(" ")
                ayudante.borrarPalabra(palabraEliminar)
        else:
            print(" ")
            print("\tEs necesario crear un ayudante ortográfico.")
            print("\tPor favor, cree un ayudante ortográfico.")
        
    elif opcion == 4: # Corregir texto
        if ayudante:
            textoCorregir = input("Nombre/ruta del archivo texto a corregir: ")
            if not textoCorregir:
                print("Error:\t No ha introducido el nombre/ruta del texto a corregir.")
            else: 
                print(" ")
                ayudante.corregirTexto(textoCorregir)
        else:
            print(" ")
            print("\tEs necesario crear un ayudante ortográfico.")
            print("\tPor favor, cree un ayudante ortográfico.")

    elif opcion == 5: # Imprimir diccionario
        if ayudante:
            print("\n")
            ayudante.imprimirDiccionario()
        else:
            print(" ")
            print("\tEs necesario crear un ayudante ortográfico.")
            print("\tPor favor, cree un ayudante ortográfico.")