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
        
    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
            
    def sizeOfList(self):
        return self.size