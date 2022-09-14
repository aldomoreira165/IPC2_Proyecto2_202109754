
class main():
    
    def __init__(self):
        self.inicio = self.menuPrincipal()
    
    def menuPrincipal(self):
        print("************************************************")
        print("*¡Bienvenido al sistema de atención al cliente!*")
        print("*1.Configuración de empresas                   *")
        print("*2.Selección de empresa y punto de atención    *")
        print("*3.Manejo de puntos  de atención               *")
        print("************************************************")
        opcion = int(input("Seleccione una opción: "))
        
aplicacion = main()