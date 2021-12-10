import time,os,lista

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
numeros=lista.lista()
def menu():
    clearConsole()
    print("1. Ingresar nuevo numero")
    print("2. Listar numeros de telefono guardados")
    print("3. Salida")
    opcion_seleccionada=input("Que desea hacer?\n")

    if opcion_seleccionada=="1":
        clearConsole()
        numero=input("Ingrese el numero de telefono:\n")
        nombre=input("Ingrese el nombre para el numero de telefono:\n")
        numeros.añadir_inicio(numero, nombre)
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
        print("Adios...")
    else:
        print("porfavor elija una opcion valida")
        time.sleep(2)
        clearConsole()
        menu()
menu()