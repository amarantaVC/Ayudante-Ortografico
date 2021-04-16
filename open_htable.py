"""
Archivo: open_htable.py

contiene una funcion que verifica si un elemento de tipo sting es una palabra valida, es decir que esta formado con caracateres alfabeticos en minuscula

Autor:
#   Estudiante: Amaranta Villegas
#   Carnet: 16-11247
# Ultima modificación 16/04/2021

Proyecto2: Ayudante Ortografico 
prof : Guillermo Palma
"""
import hashlib
from hashlib import sha256 
import math
from math import factorial
class OpenHtable(object):
    
    def __init__(self,n):
        
        self.tamano = n
        self.tabla = [None for i in range(n)]
        self.cantidad = 0
    
    #creamos la funcion de hash para el sondeo lineal 
    def h(self,palabra,i):
        h = sha256(palabra.encode())
        
        h1 = int(h.hexdigest(), base=16)
        resultado = (h1 + i) % self.tamano
        return (resultado)
    
    "hash_insert tiene como funcion insertar las palabras a la tabla de hash"
    #{pre: self.tabla != []}
    #{post: self.tabla u palabra}
    def hash_insert(self,palabra):
        
        self.rehashing()
        tabla = self.tabla 
        assert(tabla != [])
        i =0
        while i < len(tabla) :
            j = self.h(palabra,i)  
            if tabla[j] is None:
                tabla[j] = palabra
                self.cantidad += 1
                return j
            else:
                i = i + 1
        
        else:
            print("desbordamiento de la tabla de hash")

    "hash_search tiene como funcion buscar una palabra en la tabla hash"
    #{pre: palabra: str}
    #{post: buscar == j y buscar == None}
    def hash_search(self,palabra):
        #precondicion


        i = 0
        tabla = self.tabla
        n = self.tamano
        buscar = False
        while i < n and tabla != None:
            j = self.h(palabra,i)
            if tabla[j] == palabra:
                buscar = True
                return j 
            i += 1
        if tabla[j] == None or i == n:
            return None

        #postcondicion

    "hash_delete tiene como funcion eliminar una palabra que se encuentre en la tabla de hash"
    #{pre: palabra: str}
    #{post: self.tabla == self.tabla - palabra}
    def hash_delete(self,palabra):
        #precondicion

        i = 0
        self.tabla
        n = self.tamano
        while i < n and self.tabla != None:
            j = self.h(palabra,i)
            if self.tabla[j] == palabra:
                self.tabla[j] = None
                self.cantidad -= 1
                return j
            else:
                i += 1

        #postcondicion
        #{self.tabla = self.tabla - palabra}
    "numElementos contiene la cantidad de elementos que se encuentran almacenados en el arreglo"
    def numElementos(self):
        #precondicion
        assert(True)

        return self.cantidad

    "factor_de_carga contiene el numero promedio de elementos por slot en la tabla de hash"
    def factor_de_carga(self):
        #precondicion
        assert(self.tamano > 0)
        n = self.tamano

        factor = self.cantidad/n

        return factor

        #postcondicon
        #{0 <= factor <= 1}
        
    "como su nombre lo indica rehashing es hacer hashing otra vez y eso se realiza en el momento en el que el factor de carga es mayor de 0.7 para dublicar el tamano de nuestra tabla hash"
    #{pre: True}
    #{post: self.tabla == self.tabla*2n}
    def rehashing(self):
        assert(True)

        if self.factor_de_carga() < 0.7:
            return
               
        Newtabla = OpenHtable(self.tamano*2)

        for casilla in self.tabla:
            if casilla is not None:
                Newtabla.hash_insert(casilla)
        self.tabla = Newtabla.tabla
        self.tamano = Newtabla.tamano
        self.cantidad = Newtabla.cantidad

    def __str__(self):
        return f'{self.tabla}'

