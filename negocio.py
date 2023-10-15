import utils

#EJERCICIO 1

def imprimirSueldo():
    sueldo=[]
    sueldoSuperior=[]
    vueltas=True
    
    while vueltas:
        sueldoEmpleado= int(input("INGRESE SUELDO DE EMPLEADO: "))
        if sueldoEmpleado >= 60000:
            sueldoSuperior.append(sueldoEmpleado)
        else:
            sueldo.append(sueldoEmpleado)
    
        preguntar= input("Desea continuar ingresando un Sueldo? y/n: ")

        if preguntar == "n":
            vueltas= False
    
    print("Sueldos:\n",sueldo)
    print("Sueldos superiores:\n", sueldoSuperior)
    
#EJERCICIO 2

def cargaryBuscarNum():
    vueltas=True
    numeros=[]
    
    while vueltas:
        num= int(input("Ingrese un Numero: "))
        if num > 0:
            numeros.append(num)
        
        continuar=input("DESEA INGRESAR UN NUMERO MAS? y/n: ")
                
        if continuar == "n":
            vueltas = False
        
    def buscar(numeros, numBuscar):
        for i in range(len(numeros)):
            if numBuscar == numeros[i]:
                return True
        return False

    numBuscar= int(input("Ingrese el numero que quiera buscar en la lista: "))
    resultado= buscar(numeros, numBuscar)
    if resultado == True:
        print("El numero que busca fue encontrado en la lista")
    else:
        print("No se encontro el numero que busca")

#EJERCICIO 3
codigosEmpleados = []
nombreApellidoEmpleados = []
sueldosEmpleados = []

def ingresarEmpleado():
    vuelta=1
    while vuelta != 0:
        codigo = input("Ingrese el codigo del empleado:\n")
        nombre_apellido = input("Ingrese el Nombre y Apellido del empleado:\n")
        sueldo = int(input("Ingrese el sueldo del empleado:\n"))
        codigosEmpleados.append(codigo)
        nombreApellidoEmpleados.append(nombre_apellido)
        sueldosEmpleados.append(sueldo)
        vuelta = int(input("¿Desea continuar ingresando empleados?\n0. Para Finalizar\n1. Para Continuar\nINGRESE RESPUESTA AQUI: "))
    print("CODIGOS:\n", codigosEmpleados)
    print("NOMBRE Y APELLIDO:\n", nombreApellidoEmpleados)
    print("SUELDO:\n",sueldosEmpleados)

def buscarEmpleado():
    ciclo = True
    while ciclo:
        buscarCodigo= input("Ingrese el codigo del empleado que desea buscar: ")
        for i in range (len(codigosEmpleados)):
            if buscarCodigo == codigosEmpleados[i]:
                print("CODIGO DE EMPLEADO:", codigosEmpleados[i])
                print("NOMBRE Y APELLIDO:", nombreApellidoEmpleados[i])
                print("SU SUELDO ES:", sueldosEmpleados[i])
            else:
                print("EL CODIGO NO FUE ENCONTRADO")
                print("INTENTE NUEVAMENTE")
        preguntar = input("Desea realizar una nueva busqueda? y/n: ")
        if preguntar == "n":
            print("BUSQUEDA FINALIZADA")
            ciclo= False

#EJERCICIO 4

def invertirLista():
    num = []
    numInvertidos=[]
    
    for i in range (0,10):
        numero = int(input("INGRESE UN NUMERO: "))
        num.append(numero)

    indice= len(num)
    
    while indice > 0:
        indice = indice - 1
        
        num2 = num[indice]
        numInvertidos.append(num2)

    print("Lista de numeros ingresados:\n",num)
    print("Lista Invertida:\n",numInvertidos)

#EJERCICIO 5
"""productos=[]
precios=[]
stock=[]"""

productos = ["Arroz","Fideo","Galletas","Pan","Gaseosa","Cerveza","Jugo","Leche","Manteca","Queso"]

precios = [430,440,330,1000,450,1000,140,500,558,1050]

stock = [5,4,35,6,45,65,63,7,34,65]

def agregarProducto():
    ciclo= True
    while ciclo:
        productoNuevo= input("INGRESE EL NOMBRE DEL PRODUCTO: ")
        precioProducto= int(input("PRECIO DEL PRODUCTO: "))
        stockProducto= int(input("STOCK DEL PRODUCTO: "))
        productos.append(productoNuevo)
        precios.append(precioProducto)
        stock.append(stockProducto)
        print(productos)
        print(precios)
        print(stock)
        
        preguntar=input("DESEA INGRESAR UN PRODUCTO NUEVO? y/n: ")
        if preguntar == "n":
            ciclo=False

def buscarProducto():
    ciclo = True
    while ciclo:
        
        producto=input("INGRESE EL PRODUCTO QUE DESEA BUSCA: ")
        error= True
        
        for i in range(len(productos)):
            if producto==productos[i]:
                print(productos[i])
                print("Precio:", precios[i])
                print("Stock:", stock[i])
                error = False
        if error == True:
            print("El producto no fue encontrado")
        producto = input("DESEA BUSCAR OTRO PRODUCTO? y/n: ")
        if producto == "n":
            ciclo=False

def modificarProducto():
    vuelta= True
    while vuelta:
        productomod= input("INGRESE PRODUCTO A MODIFICAR:")
        errorbusqueda = True 
        for i in range(len(productos)):
            if productomod == productos[i]:
                print(productos[i])
                print("Precio:",precios[i])
                print("Stock:",stock[i])
                precioViejo = precios[i]
                stockViejo = stock[i]
                nuevoPrecio = int(input("Ingrese el nuevo Precio\n"))
                precios[i] = nuevoPrecio
                print("Precio actualizado correctamente")
                print("Precio anterior:", precioViejo,"\n","Precio actualizado:",precios[i])
                nuevoStock = int(input("Ingrese su nuevo Stock\n"))
                stock[i] = nuevoStock
                print("Stock actualizado correctamente\n")
                print("Stock anterior:", stockViejo,"\n","Stock actualizado:",stock[i])
                print("Su producto se modifico exitosamente")
                print(productos[i])
                print("Precio:",precios[i])
                print("Stock:",stock[i])
                errorbusqueda= False
        if errorbusqueda == True:
            print("!! PRODUCTO NO ENCONTRADO !!")
        preguntar= input("Desea continuar actualizando productos? y/n: ")
        if preguntar == "n":
            print("A finalizado la actualizacion de Stock")
            vuelta= False

def ventaDeProducto():
    bucle= True
    while bucle:
        productoVend= input("Ingrese producto vendido: ")
        encontrar= False
        for i in range(len(productos)):
            if productoVend == productos[i]:
                print("PRODUCTO: ",productos[i])
                print("STOCK: ",stock[i])
                cantVendido=int(input("Ingrese la Cantidad Vendido del producto:"))
                stockActualizado= stock[i] - cantVendido
                ventasEfectivo= precios[i] * cantVendido
                stock[i]= stockActualizado
                print("PRODUCTO:",productos[i],"\nSTOCK:",stock[i], "unidades")
                print("SE VENDIERON:",cantVendido,"a un total de $",ventasEfectivo)
                encontrar= True
        if encontrar == False:
            print("!!NO SE ENCONTRO EL PRODUCTO!!")
        preguntar=input("DESEA INGRESAR UNA NUEVA VENTA? y/n: ")
        if preguntar == "n":
            bucle = False


