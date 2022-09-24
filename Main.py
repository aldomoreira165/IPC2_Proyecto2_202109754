from ArchivoConfigServicio import ArchivoConfigServicio
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
        archivo = None
        while True:
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
                opcion = int(input("Seleccione una opción: "))
                self.clearConsole()
                
                if opcion == 1:
                    pass
                elif opcion == 2:
                    self.clearConsole()
                    ruta = input("Ingresa la ruta del archivo de configuración del sistema: ")
                    archivo = ArchivoConfigServicio(ruta)
                    archivo.agregarArchivo()
                    self.clearConsole()
            elif opcion == 2:
                self.clearConsole()
                if archivo == None:
                    print("No hay datos existentes. Verifica que hayas ingresado un archivo al sistema.")
                else:
                    #imprimiendo lista dee empresas
                    empresa = archivo.listaEmpresas.primero
                    for i in range(archivo.listaEmpresas.sizeOfList()):
                        print(empresa.dato.numero, empresa.dato.nombre)
                        empresa = empresa.siguiente
                    
                    numero = int(input("Selecciona un número de empresa: "))
                    
                    empresa_seleccionada = archivo.listaEmpresas.primero
                    for i in range(archivo.listaEmpresas.sizeOfList()):
                        if numero == empresa_seleccionada.dato.numero:
                            punto_atencion = empresa_seleccionada.dato.puntosAtencion.primero
                            for i in range(empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                                print(punto_atencion.dato.numero, punto_atencion.dato.codigo, punto_atencion.dato.nombre)
                                punto_atencion = punto_atencion.siguiente
                            numero = int(input("Selecciona un número de punto de atención: "))
                            punto_seleccionado = empresa_seleccionada.dato.puntosAtencion.primero
                            for i in range(empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                                if numero == punto_seleccionado.dato.numero:
                                    escritorio = punto_seleccionado.dato.escritorios.primero
                                    for i in range(punto_seleccionado.dato.escritorios.sizeOfList()):
                                        print(escritorio.dato.numero, escritorio.dato.codigo, escritorio.dato.identificacion, escritorio.dato.encargado)
                                        escritorio = escritorio.siguiente
                                else:
                                    punto_seleccionado = punto_seleccionado.siguiente    
                            break
                        else:
                            empresa_seleccionada = empresa_seleccionada.siguiente

            
aplicacion = main()