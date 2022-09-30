from Nodo import Nodo

class Lista():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
        
    def vacia(self):
        return self.primero == None
         
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
        
    def eliminar_inicio(self):
        if self.vacia():
            print("Está vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1
            
    def eliminar_final(self):
        if self.vacia():
            print("Está vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
       
    def sizeOfList(self):
        return self.size