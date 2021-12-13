class nodo:
    def __init__(self, numero = None, nombre= None, apellido = None,siguiente = None):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.siguiente = siguiente

class lista: 
    def __init__(self):
        self.cabeza = None

    def añadir_inicio(self, numero, nombre, apellido):
        self.cabeza = nodo(numero=numero,nombre=nombre,apellido=apellido, siguiente=self.cabeza)  
    
    #def es_vacia(self):
# return self.cabeza == None

#def obtener_ultimo(self):
# temp = self.cabeza
# while(temp.siguiente is not None):
# temp = temp.siguiente
# return temp.numero

#def borrar(self, key):
# actual = self.cabeza
# anterior = None
# while actual and actual.numero != key:
# anterior = actual
# actual = actual.siguiente
# if anterior is None:
# self.cabeza = actual.siguiente
# elif actual:
# anterior.siguiente = actual.siguiente
# actual.siguiente = None

    def verificarRepetido( self, x ):
        contador=1
        nodo = self.cabeza
        while nodo != None:
            if nodo.numero == x:
                return True
            else:
                nodo = nodo.siguiente
        return False

    def imprimir( self ):
        contador=1
        nodo = self.cabeza
        while nodo != None:
            print(str(contador)+") "+nodo.nombre+" "+nodo.apellido+": "+str(nodo.numero)+"\n")
            contador+=1
            nodo = nodo.siguiente