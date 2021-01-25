from funcionesBD import *
from producto import Producto
class Factura:
    def __init__(self, fecha, codigo=0, listaP=[], listaC=[], total=0, subtotal=0, ivg=0):
        conexion = conectar()
        self.codigo = 0
        self.fecha = fecha
        self.listaProd = listaP
        self.listaCant = listaC
        self.total = total
        self.ivg = ivg
        self.subtotal = subtotal
        c = ejecutar("select factura_id from facturas order by factura_id desc limit 1", 0, conexion)
        for elem in c:
            self.codigo = elem[0]+1
        if self.codigo == 0:
            self.codigo = 1
        insertFact = "insert into facturas (fecha, total, ivg, subtotal) values (%s, %s,%s,%s);"
        
        datos = (self.fecha, str(self.total), str(self.ivg), str(self.subtotal))
        c = ejecutar(insertFact, datos, conexion)
        cerrar(conexion)
    def agregarProd(self, prod, cant):
        conexion = conectar()
        
        c = ejecutar("select * from productos where producto_id =" +str(prod), 0, conexion)
        prec = 0
        for elem in c:
            nuevoProd = Producto(elem[1], elem[2], elem[0])
        hallado = False
        for i in range(len(self.listaProd)):
            if self.listaProd[i].n == nuevoProd.n:
                self.listaCant[i] = cant
                i = len(self.listaProd)
                hallado = True
        if hallado == False:    
            self.listaProd.append(nuevoProd)    
            self.listaCant.append(cant)
        
        self.subtotal = self.subtotal+(nuevoProd.prec*cant)
        self.ivg = self.subtotal*0.18
        self.total = self.subtotal*(1.18)
        print(self.codigo)
    def grabar(self):
        conexion = conectar()
        grabaFact = "update facturas set total = %s, subtotal = %s, ivg = %s where factura_id = %s;"
        datos = (str(self.total), str(self.subtotal), str(self.ivg), str(self.codigo))
        c = ejecutar(grabaFact, datos, conexion)
        for i in range(len(self.listaProd)):
            ingresaRel = "insert into facturas_productos (factura_id, producto_id, cantidad) values (%s,%s,%s);"
            datos = (str(self.codigo), str(self.listaProd[i].codigo), str(self.listaCant[i]))
            c = ejecutar(ingresaRel, datos, conexion)
            
        cerrar(conexion)
    @staticmethod
    def listarFacturas():
        conexion = conectar()
        c = ejecutar("select * from facturas", 0, conexion)
        lRes = []
        for elem in c:
            result = "Código: " + str(elem[0]) + " | Fecha: " + str(elem[1]) + " | Subtotal: " + str(elem[2]) + " | IVG: " + str(elem[3]) + " | Total: " + str(elem[4])
            lRes.append(result)
        cerrar(conexion)
        return lRes

    @staticmethod
    def verPorId(cod):
        conexion = conectar()
        cons = "select * from facturas_productos where factura_id = "+str(cod)+";"
        
        c = ejecutar(cons, 0, conexion)
        lisRes = []
        for elem in c:
            d = ejecutar("select nombre, precio from productos where producto_id = "+str(elem[2]), 0, conexion)
            for elem2 in d:
                nomProd = elem2[0]
                precProd = str(elem2[1])
            resultado = "Producto: " + nomProd + " | Precio: " + str(precProd) + " | Cantidad: " +str(elem[3])
            lisRes.append(resultado)
        cerrar(conexion)
        return lisRes    

    
        