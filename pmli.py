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

class PMLI(object):

    #constructor principal 
    
    def __init__(self,l: str):
    #{Pre: True}
        assert(True)
        self.letra = l
        self.palabras = []

        #postcondicion
        assert(self.letra == l and self.palabras == [])

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
            else:
                palabras.append(p)
        else:
           print(f"Palabra {p} no valida, por favor revise que todos los elementos esten en minusculas")


        
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
                palabras.remove(p)
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
                for word in palabras:
                    if word == p:
                        buscar = True
                    else:
                        pass
            print(buscar)
        else:
            print(f"Palabra {p} no valida, por favor revise que todos los elementos esten en minusculas")
            
    "Muestra la instancia self.palabras con sus elementos ordenados en forma lexicografica"
    #{pre: True}
    #{post: mostrarPalabras = (All p: 0<=p< len(palabras) : palabras[p] <= palabras[p+1])}
    def mostrarPalabras(self):
        assert(True)
        palabras = self.palabras
        palabras.sort()
        print(palabras)


if __name__ == "__main__":
    arreglo = PMLI("a")
    arreglo.agregarPalabra("ale")
    arreglo.agregarPalabra("arrida")
    arreglo.agregarPalabra("r5@batar")
    arreglo.mostrarPalabras()

    arreglo.eliminarPalabra("ale")
    arreglo.mostrarPalabras()
    arreglo.buscarPalabra("ale")


