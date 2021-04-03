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

    def hash_insert(self,palabra):
        
        tabla = self.tabla 
        n =  self.tamano
        i =0
        while i < n :
            j = self.h(palabra,i)
            if tabla[j] == None:
                tabla[j] = palabra
                self.cantidad += 1
                return j
            else:
                i = i + 1
        else:
            print("desbordamiento de la tabla de hash")

    def hash_search(self,palabra):
        i = 0
        tabla = self.tabla
        n = self.tamano
        while i < n and tabla != None:
            j = self.h(palabra,i)
            if tabla[j] == palabra:
                return j
            i += 1
        if i == n or tabla[j] == None:
            return None
    
    def hash_delete(self,palabra):
        i = 0
        tabla = self.tabla
        n = self.tamano
        while i < n and tabla != None:
            j = self.h(palabra,i)
            if tabla[j] == palabra:
                tabla[j] = None
                self.cantidad -= 1
                return j
            else:
                i += 1
    def numElementos(self):
        
        return self.cantidad
    
    def factor_de_carga(self):
        n = self.tamano

        factor = self.cantidad/n

        return factor
    
    def rehashing(self):
        if self.factor_de_carga() >= 0.7:
            OldTabla = self.tabla
            Oldn = self.tamano
        
        Newtabla = OpenHtable(Oldn*2)

        for casilla in OldTabla:
            if casilla:
                tabla.hash_insert(casilla)
        
        self.tabla = Newtabla.tabla
        self.tamano = Newtabla.tamano

    def mostrar(self):
        print(self.tabla)

}