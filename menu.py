import time,os,lista
from xml.dom import minidom

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
numeros=lista.lista()
def menu():
    clearConsole()
    print("1. Ingresar nuevo numero")
    print("2. Listar numeros de telefono guardados")
    print("3. Cargar XML")
    print("4. Generar Grafico")
    opcion_seleccionada=input("Que desea hacer?\n")

    if opcion_seleccionada=="1":
        clearConsole()
        numero=input("Ingrese el numero de telefono:\n")
        nombre=input("Ingrese el nombre para el numero de telefono:\n")
        apellido=input("Ingrese el apellido: \n")
        numeros.añadir_inicio(numero, nombre, apellido)
        print("Regresando al menu principal...")
        time.sleep(3)
        clearConsole()
        menu()
    elif opcion_seleccionada=="2":
        clearConsole()
        numeros.imprimir()
        time.sleep(3)
        input("Presione enter para volver al menu principal...")
        clearConsole()
        menu()
    elif opcion_seleccionada=="3":
        clearConsole()
        docXML= minidom.parse(input("Ingrese la ruta del archivo XML: \n"))
        contactos= docXML.getElementsByTagName("contactos")
        contador=1 
        for x in contactos:
            print("Cargando contacto No. "+str(contador))
            telefono=x.getElementsByTagName("telefono")
            telefono_valor=telefono[0].firstChild.nodeValue.strip('"')
            #print("Artista: "+artista_valor)
            nombre=x.getElementsByTagName("nombre")
            nombre_valor=nombre[0].firstChild.nodeValue.strip('"')
            apellido=x.getElementsByTagName("apellido")
            apellido_valor=apellido[0].firstChild.nodeValue.strip('"')
            if numeros.verificarRepetido(telefono_valor):
                print("El contacto No. "+str(contador)+" ya es repetido, no se agrego...")
                time.sleep(3)
                contador+=1
                continue
            else:
                numeros.añadir_inicio(telefono_valor, nombre_valor, apellido_valor)
                contador+=1
        print("Regresando al menu principal...")
        time.sleep(3)
        clearConsole()
        menu()
    elif opcion_seleccionada=="4":
        numeros.grafica()
        input("Presione enter para volver al menu principal...")
        clearConsole()
        menu()
    else:
        print("porfavor elija una opcion valida")
        time.sleep(2)
        clearConsole()
        menu()
menu()