from funcionesBD import *
class Producto:
    def __init__(self, n, prec, codigo=0):
        self.codigo = codigo
        self.n = n
        self.prec = prec
    def crearProd(self):
        conexion = conectar()
        insProd = "insert into productos (nombre, precio) values (%s,%s);"
        data = (self.n, self.prec)
        c = ejecutar(insProd, data, conexion)
        cerrar(conexion)
    @staticmethod
    def listarProductos():
        conexion = conectar()
        c = ejecutar("select * from productos", 0, conexion)
        lRes = []
        for elem in c:
            result = "Código: " + str(elem[0]) + " | Nombre: " + str(elem[1]) + " | Precio: " + str(elem[2])
            lRes.append(result)
        return lRes
    