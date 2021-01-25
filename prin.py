from producto import Producto
from factura import Factura
from funcionesBD import *
conexion = conectar()
print("Ingrese usuario y contraseña... [UTIICE: usuario: user | contraseña: mipass]")
usuario = input("Ingrese usuario")
miPass = input("Ingrese pass")
data = (usuario, miPass)
c = ejecutar("select * from users where nombre = '%s' and pass = '%s'", data, conexion)
while(c == None):
    print("ERROR, ingrese datos nuevamente...")
    usuario = input("Ingrese usuario")
    miPass = input("Ingrese pass")
    data = (usuario, miPass)
    c = ejecutar("select * from users where nombre = %s and pass = %s", data, conexion)


print("------ MENU:-------\n 1 - Crear producto\n 2 - Listar productos \n 3-Crear facturas\n 4-Listar facturas\n 5-Salir")
opc = int(input(""))
while opc!=5:
    if opc == 1:
        print("Ingrese nombre del producto a crear:")
        nomProd = input("")
        print("Ingrese precio:")
        precProd = float(input(""))
        miProd = Producto(nomProd, precProd)
        miProd.crearProd()
        print("Producto creado con éxito")
    elif opc == 2:
        print("Listado de productos:")
        lista = Producto.listarProductos()
        for i in range(len(lista)):
            print(lista[i])
    elif opc == 3:
        print("Ingrese fecha de la factura:")
        fec = input("")
        miFac = Factura(fec)
        print("Seleccione por codigo productos de la lista. Toque -1 para dejar de cargar")
        lista = Producto.listarProductos()
        for i in range(len(lista)):
            print(lista[i])
        codProd = int(input("Ingrese el codigo del que desea agregar"))
        while codProd !=-1:

            cantidad = int(input("Ingrese la cantidad que desea cargar de este producto"))
            miFac.agregarProd(codProd, cantidad)
            for i in range(len(lista)):
                print(lista[i])
            codProd = int(input("Ingrese el codigo del que desea agregar"))
        miFac.grabar()
        print("Factura creada con éxito")
    elif opc == 4:
        print("Lista de facturas. Ingrese el código de la que quiera ver")
        lista = Factura.listarFacturas()
        for j in range(len(lista)):
            print(lista[j])
        print("Ingrese el código de una de ellas para ver el detalle; al finalizar, o -1 para salir")
        cod = int(input("Ingrese código..."))
        while cod!=-1:
            lista = Factura.verPorId(cod)
            for i in range(len(lista)):
                print(lista[i])
            
            cod = int(input("Ingrese código..."))
            
            
        
        
        
    print("------ MENU:-------\n 1 - Crear producto\n 2 - Listar productos \n 3-Crear facturas\n 4-Listar facturas\n 5-Salir")
    opc = int(input(""))
cerrar(conexion)