import os,time

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
    
    def grafica(self):
        anterior=""
        nodos=""
        uniones=""
        quotes='"'
        contador=1
        nodo = self.cabeza
        while nodo != None:
            #print(str(contador)+") "+nodo.nombre+" "+nodo.apellido+": "+str(nodo.numero)+"\n")
            nodos=nodos+nodo.nombre+'[label='+quotes+nodo.nombre+" "+nodo.apellido+quotes+']\n'
            if anterior!="":
                uniones=uniones+anterior+"->"+nodo.nombre+"\n"
                anterior=nodo.nombre
            else:
                anterior=nodo.nombre
            contador+=1
            nodo = nodo.siguiente
        grafico="digraph {\nrankdir=LR;\n"+nodos+uniones+"}"
        print(grafico)
        file = open("archivo.dot", "w", encoding='utf-8')
        file.write(grafico)
        file.close()
        os.system('dot -Tpng archivo.dot -o salida.png')

        self.generando()
        os.system("xdg-open salida.png")

    def generando(self):
        for x in range(3):
            print(x)
            os.system("clear")
            print("Generando grafico, espere un momento")
            time.sleep(0.5)
            os.system("clear")
    
            print("Generando grafico, espere un momento.")
            time.sleep(0.5)
            os.system("clear")
    
            print("Generando grafico, espere un momento..")
            time.sleep(0.5)
            os.system("clear")
    
            print("Generando grafico, espere un momento...")
            time.sleep(0.5)
            os.system("clear")


    
    #    digraph {
    #rankdir=LR;
    #inicio [label="Inicio", shape = "plaintext"]
    #A [label="A", shape = doublecircle]
    #B [label="B", shape = circle]
    #C [label="C", shape = doublecircle]
    #inicio ->A
    #A->F [label = "1"]
    #A->B [label = "0"]
    #B->B [label = "1"]
    #B->C [label = "0"]
    #C->C [label = "1"]
    #C->C [label = "0"]
    #}
