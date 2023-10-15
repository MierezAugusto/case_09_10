menu="""

----------MENU PRINCIPAL----------

1*  Ingresar los sueldos de los empleado, agregarlos a una lista.
    e imprimir los sueldos superiores

2*  Cargar un numero a una lista y buscar.
    retornar true si lo encuentra o false si no esta 
    dentro de la lista. 

3*  Hacer un programa que ingrese el codigo, sueldo,
    nombre y apellido de los empleados hasta que se ingrese un 0,
    crear las lista necesarias para que desde un menu el adminstrador
    ingrese el codigo y nos muestre por pantalla el codigo,
    el sueldo y nombre y apellido

4*  Ingresar 10 numeros por telcado y agregarlos a una lista,
    los numeros ingresados pasarlos a una nueva lista pero 
    invertidos

5*  Administracion del stock de una tienda de comestibles

6*  Salir
"""
def imprimirMenu():
    print(menu)

menuEmpleados="""

---------- Administrador de Empleados----------

1. Ingresar Nuevo Empleado
2. Buscar Empleado
3. Salir
"""
def imprimirMenuSueldos():
    print(menuEmpleados)

menuComercio = """

---------- Menu Comercio ----------

1. Dar de alta un producto
2. Buscar un producto
3. Modificar un producto
4. Guardar Venta
5. Salir
"""
def imprimirMenuComercio():
    print(menuComercio)