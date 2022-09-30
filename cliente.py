
class Cliente:
    
    def __init__ (self, dpi, nombre, transacciones, atendido):
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = transacciones
        self.atendido = atendido
        
    def servido(self):
         self.atendido = True 
         