class nodo:
    def __init__(self, numero = None, nombre= None, siguiente = None):
        self.numero = numero
        self.nombre = nombre
        self.siguiente = siguiente

class lista: 
    def __init__(self):
        self.cabeza = None

    def añadir_inicio(self, numero, nombre):
        self.cabeza = nodo(numero=numero,nombre=nombre, siguiente=self.cabeza)  

    def imprimir( self ):
        contador=1
        nodo = self.cabeza
        while nodo != None:
            print(str(contador)+") "+nodo.nombre+": "+str(nodo.numero)+"\n")
            contador+=1
            nodo = nodo.siguiente