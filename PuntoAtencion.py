
class PuntoAtencion: 
    
    def __init__(self, numero, codigo, nombre, direccion, escritorios, clientes):
        self.numero = numero
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = escritorios
        self.clientes = clientes
        
    def agregar_clientes(self, clientes):
        self.clientes = clientes