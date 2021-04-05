"""
Archivo: pmli.py

contiene a un conjunto de palabras, las cuales comienzan por una misma letra. A
continuaci´on se presenta la especificacion del TAD.

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


class PMLI(object):

    #constructor principal 
    
    def __init__(self,l: str):
    #{Pre: True}
        assert(True)
        self.letra = l
        self.palabras = OpenHtable(5)

        #postcondicion
        assert(self.letra == l)

    "agregarPalabra tiene como tarea agregar una palabra p que inicie con self.letra a la instancia self.palabras"
    #{pre: p[0] == self.letra}
    #{post: palabras == palabras U p }
    def agregarPalabra(self,p:str):
        palabras = self.palabras
        letra = self.letra

            #precondicion
        if esPalabraValida(p) == True:
            if p[0] != letra:
                print(f"Sorry, la palabra {p} no comienza con la letra {letra}")
                exit(p)
            else:
                
                palabras.hash_insert(p)
        else:
            print(f"Palabra {p} no valida, por favor revise que todos los elementos esten en minusculas")
            exit(p)   

        
        return palabras

    #{precondicion: p[0] == self.letra}
    #{palabras == palabras - p }
    "eliminarPalabra tiene la tarea de eliminar una palabra p que se encuentra en la instancia self.palabras"
    def eliminarPalabra(self, p:str):

        palabras = self.palabras
        letra = self.letra
        if esPalabraValida(p) == True:
                
            if p[0] != letra:
                print(f"Sorry, la palabra {p} no comienza con la letra {letra}")

            else:
                palabras.hash_search(p)
                if palabras.hash_search == True:

                    palabras.hash_delete(p)
                else:
                    print(f"Sorry, la palabra {p} no fue se encuentra en el diccionario")    
        else:
            print(f"Palabra {p} no valida, por favor revise que todos los elementos esten en minusculas")
        return palabras

    
    #{pre: p[0] == self.letra}
    #{post: buscar == False v buscar == True }
    "buscarPalabra es una funcion que tiene la tarea de indicar si una palabra p valida se encuentra en la instancia self.palabras o no, retorna un booleano "
    def buscarPalabra(self, p:str) ->  bool:
        palabras = self.palabras
        letra = self.letra
        buscar = False
        if esPalabraValida(p) == True:
            if p[0] != letra:
                print(f"Sorry, la palabra {p} no comienza con la letra {letra}")

            else:
                if palabras.hash_search(p) != None:
                    buscar = True
                else:
                    pass
            return buscar
        else:
            print(f"Palabra {p} no valida, por favor revise que todos los elementos esten en minusculas")

    "Muestra la instancia self.palabras con sus elementos ordenados en forma lexicografica"
    
    #{pre: True}
    #{post: mostrarPalabras = (All p: 0<=p< len(palabras) : palabras[p] <= palabras[p+1])}
    def mostrarPalabras(self):
        lista = []
        for palabra in self.palabras.tabla :
            if palabra != None:
                lista.append(palabra)
            else:
                pass
        lista = sorted(lista)
        enunciado = f"\nletra\t  {self.letra} "
        enunciado += f"-> {lista }"
        print(enunciado)
"""
    def __repr__(self):
        enunciado = f"\nletra\t  {self.letra} "
        enunciado += f"-> {self.lista }"
        return enunciado
"""

if __name__ == "__main__":
    arreglo = PMLI("a")
    arreglo.agregarPalabra("ale")
    arreglo.agregarPalabra("arrida")
    arreglo.eliminarPalabra("ale")
    arreglo.buscarPalabra("ale")
    arreglo.buscarPalabra("arrida")
    arreglo.agregarPalabra("aola")
    arreglo.agregarPalabra("azul")
    arreglo.agregarPalabra("aliza")
    arreglo.mostrarPalabras()

    

