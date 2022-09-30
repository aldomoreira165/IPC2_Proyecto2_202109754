
class EscritorioServicio:
    
    def __init__ (self, numero,codigo, identificacion, encargado, activo, libre):
        self.numero = numero
        self.codigo = codigo
        self.identificacion = identificacion
        self.encargado = encargado
        self.activo = activo
        self.libre = libre
        
    def activar_escritorio(self):
        self.activo = True
        
    def desactivar_escritorio(self):
        self.activo = False
        
    def liberar_escritorio(self):
        self.libre = True
        
    def ocupar_escritorio(self):
        self.libre = False