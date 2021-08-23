import os
from Lista import Lista
from Pila import Pila
from Cola import Cola

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        while True:
            try:
                opc = input("Elija opcion [1....{}]: ".format(len(self.opciones)))
                break
            except ValueError:
                print("Dato no válido, por favor ingrese un número")
        return opc
opc = ""
while True:
    try:
        tam = int(input("Ingres el tamaño que desea de la lista - pila - cola: "))
        break
    except ValueError:
        print("Dato no válido, por favor ingrese un número")
pila1 = Pila(tam)
lista1 = Lista(tam)
cola1 = Cola(tam)
while opc != "4":
    os.system("cls")
    men = Menu("***Menú Principal***",["1) Pila", "2) Cola", "3) Lista", "4) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("***Menú Pila***",["1) Push","2) Pop","3) Show","4) Longitud","5) Empty","6) Salir"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("Ingreso de un numero a la Pila")
                for i in range(tam):
                    while True:
                        try:
                            dato = int(input("Ingrese el numero que desea ingresar a la pila: "))
                            break
                        except ValueError:
                            print("Dato no válido, por favor ingrese un número")
                    pila1.push(dato)
                    print("Dato ingresado")
                input("Presione enter para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Quitar el último dígito de la Pila")
                while True:
                    try:
                        x = int(input("Cuantos elemento desea quitar de la Pila: "))
                        break
                    except ValueError:
                        print("Dato no válido, por favor ingrese un número")
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}".format(pila1.pop()))
                    input("Presione enter para continuar")
                else:
                    print("ERROR numero mayor al tamaño de la pila o no exite una pila")
                    input("Presione enter para continuar")
            elif opc1 =="3":
                os.system("cls")
                print("Mostrar los valores de la Pila")
                pila1.show()
                input("Presione enter para continuar")
            elif opc1 == "4":
                os.system("cls")
                print("Mostrar la longitud de la Pila")
                print("La longitud de la pila es: {}".format(pila1.longitud()))
                input("Presione enter para continuar")
            elif opc1 =="5":
                os.system("cls")
                print("Verificar si la Pila está vacia")
                print("False para pila llena y True para pila vacia")
                print("***{}***".format(pila1.empty()))
                input("Presione enter para continuar")
            elif opc1 =="6":
                print("De regreso al Menú Principal")
                input("Presione enter para continuar")
            else:
                print("Opción ingresada no válida")
                input("Presione enter para continuar")
    elif opc == "2":
        opc2 = ""
        while opc2 != "6":
            os.system("cls")
            men2 = Menu("Menú Cola", ["1) Insertar", "2) Quitar", "3) Mostrar", "4) Longitud", "5) Empty", "6) Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("Ingreso de un numero a la Cola")
                for i in range(tam):
                    dato = int(input("Ingrese el numero que desea agregar a la cola: "))
                    cola1.insentar(dato)
                    print("Dato ingresado")
                input("Presione enter para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("Quitar el primer valor de la Cola")
                x = int(input("¿Cuántos elemento desea quitar de la cola? : "))
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}".format(cola1.quitar()))
                    input("Presione enter para continuar")
                else:
                    print("ERROR numero mayor al tamaño de la cola o no exite una cola")
                    input("Presione enter para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("Mostrar los valores de la Cola")
                cola1.mostrar()
                input("Presione enter para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("Mostrar la longitud de la Cola")
                print("La longitud de la cola es: {}".format(cola1.longitud()))
                input("Presione enter para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("Verificar si la Cola está vacia")
                print("False para cola llena o tiene elementos y True para pila vacia")
                print("{}".format(cola1.empty()))
                input("Presione enter para continuar")
            elif opc2 == "6":
                print("De regreso al Menú Principal")
                input("Presione enter para continuar")
            else:
                print("Opción ingresada no válida")
                input("Presione enter para continuar")
    elif opc == "3":
        opc3 = ""
        while opc3 != "8":
            os.system("cls")
            men3 = Menu("Menú de Listas", ["1)Append", "2)Obtener", "3)ObtenerEliminado", "4)Buscar", "5)Insertar", "6)Eliminar", "7)Mostrar", "8)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                print("Ingreso de un numero a la Lista")
                for i in range(tam):
                    dato = int(input("Ingrese el numero que desea ingresar a la lista: "))
                    lista1.append(dato)
                    print("Dato ingresado")
                input("Presione enter para continuar")
            elif opc3 == "2":
                os.system("cls")
                print("Obtener un dato de una lista-")
                pos =int(input("Ingrese posicion del dato: "))
                print(lista1.obtener(pos))
                input("Presione enter para continuar")
            elif opc3 == "3":
                os.system("cls")
                print("Obtener el valor eliminado junto a la lista")
                pos = int(input("Ingrese posicion del dato: "))
                lista1.obtenerEliminando(pos)
                input("Presione enter para continuar")
            elif opc3== "4":
                os.system("cls")
                print("Busca el elemento en la lista y retorna la posicion")
                pos = int(input("Ingresa el dato a buscar: "))
                print(lista1.buscar(pos))
                input("Presione enter para continuar")
            elif opc3 == "5":
                os.system("cls")
                print("Insertar un dato en la lista solo sino existía ya en la lista")
                dato = int(input("Ingresa un dato a buscar para insertarlo: "))
                print(lista1.insertar(dato))
                input("Presione enter para continuar")
            elif opc3 == "6":
                os.system("cls")
                print("Eliminar dato de la lista si ya existe en la lista")
                dato = int(input("Ingresa el dato a buscar para eliminarlo: "))
                print(lista1.eliminar(dato))
                input("Presione enter para continuar")
            elif opc3 == "7":
                os.system("cls")
                print("Mostrar los datos que hay en la lista")
                lista1.mostrar()
                input("Presione enter para continuar")
            elif opc3 == "8":
                print("De vuelta al Menu Principal")
                input("Presione enter para continuar")
            else:
                print("Opción ingresada no valida")
                input("Presione enter para continuar")
    elif opc == "4":
        print("Lo esperamos en una proxima ocasión")
    else:
        print("Opción no valida")
        input("Presione una tecla para continuar ")