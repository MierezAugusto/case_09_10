import negocio
import utils
accionMenu= True
while accionMenu:
    utils.imprimirMenu()
    user = int(input("Ingrese el numero de opción que desea realizar: "))
    if user == 1:
        negocio.imprimirSueldo()
    elif user == 2:
        negocio.cargaryBuscarNum()        
    elif user == 3:
        bucle= True
        while bucle:
            utils.imprimirMenuSueldos()
            user = int(input("Ingrese el numero de opción que desea realizar: "))
            if user == 1:
                negocio.ingresarEmpleado()                
            elif user == 2:
                negocio.buscarEmpleado()                
            elif user == 3:
                print("PROGRAMA EMPLEADO FINALIZADO")
                bucle=False
            elif user > 3 or user < 0:
                print("##########La opción es incorrecta, Vuelva a intentarlo#######")
    elif user == 4:
        negocio.invertirLista()
    elif user == 5:
        vuelta=True
        while vuelta:
            utils.imprimirMenuComercio()
            user = int(input("Ingrese el numero de opción que desea realizar: "))
            if user == 1:
                negocio.agregarProducto()               
            elif user == 2:
                negocio.buscarProducto()                
            elif user == 3:
                negocio.modificarProducto()                
            elif user == 4:
                negocio.ventaDeProducto()                
            elif user == 5:
                print("PROGRAMA COMERCIO FINALIZADO")
                vuelta=False
            elif user > 3 or user < 0:
                print("\n\n\n**** ERROR: LA OPCIÓN ES INCORRECTA, VUELVA A INTENTARLO ****")
    elif user == 6:
        print("\n\n\n**************PROGRAMA FINALIZADO***************")
        accionMenu=False
        
    elif user > 6 or user < 0:
        print("\n\n\n**** ERROR: LA OPCIÓN ES INCORRECTA, VUELVA A INTENTARLO ****")