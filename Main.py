import os

class main():
    
    def __init__(self):
        self.inicio = self.menuPrincipal()
        
    #funcion para limpiar consola
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
    
    def menuPrincipal(self):
        print("************************************************")
        print("*¡Bienvenido al sistema de atención al cliente!*")
        print("*1.Configuración de empresas                   *")
        print("*2.Selección de empresa y punto de atención    *")
        print("*3.Manejo de puntos  de atención               *")
        print("************************************************")
        opcion = int(input("Seleccione una opción: "))
        self.clearConsole()
        
        if opcion == 1:
            print("**************************************************************")
            print("*1. Limpiar sistema                                          *")
            print("*2. Cargar archivo de configuración al sistema               *")
            print("*3. Crear nueva empresa                                      *")
            print("*4. Cargar archivo con configuración inicial para la prueb   *")
            print("**************************************************************")
        elif opcion == 2:
            pass
        
            
aplicacion = main()