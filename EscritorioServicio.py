
class EscritorioServicio:
    
    def __init__ (self, numero,codigo, identificacion, encargado, activo):
        self.numero = numero
        self.codigo = codigo
        self.identificacion = identificacion
        self.encargado = encargado
        self.activo = activo
        
    def activar_escritorio(self):
        self.activo = True