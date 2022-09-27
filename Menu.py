from ArchivoConfigServicio import ArchivoConfigServicio
from ArchivoConfigPrueba import ArchivoConfigPrueba
import os

class Menu:
    
    def __init__ (self):
        self.archivo = None
        self.archivop = None
        
    #funcion para limpiar consola
    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
    
    def menuPrincipal(self):
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
                print("*4. Cargar archivo con configuración inicial para la prueba  *")
                print("**************************************************************")
                opcion = int(input("Seleccione una opción: "))
                self.clearConsole()
                
                if opcion == 1:
                    self.clearConsole()
                    if self.archivo == None:
                        print("No hay ningún archivo cargado en el sistema.")
                    else:  
                        self.archivo = None
                        print("Sistema limpiado con éxito.")
                elif opcion == 2:
                    self.clearConsole()
                    ruta = input("Ingresa la ruta del archivo de configuración del sistema: ")
                    if self.archivo == None:        
                        self.archivo = ArchivoConfigServicio()
                        self.archivo.agregar(ruta)
                    else:
                        self.archivo.agregar(ruta)
                elif opcion == 3:
                    self.clearConsole()
                    if self.archivo == None: 
                        self.archivo = ArchivoConfigServicio()
                        self.archivo.agregar_empresa_individual()
                        self.clearConsole()
                        print("Empresa agregada correctamente.")
                    else: 
                        self.archivo.agregar_empresa_individual()
                        print("Empresa agregada correctamente.")
                        self.clearConsole()
                elif opcion == 4:
                    self.clearConsole()
                    if self.archivo != None:
                        ruta = input("Ingresa la ruta del archivo para inicializar la prueba del sistema de atención a clientes: ")
                        if self.archivop == None:
                            self.archivop = ArchivoConfigPrueba()
                            self.archivop.agregar(ruta, self.archivo)
                        else:
                            self.archivop.agregar(ruta, self.archivo)
                    else:
                        print("No ha ingresado ningún archivo de configuración inicial.")
            elif opcion == 2:
                self.clearConsole()
                if self.archivo == None:
                    print("No hay datos existentes. Verifica que hayas ingresado un archivo al sistema.")
                else:
                    #imprimiendo lista dee empresas
                    empresa = self.archivo.listaEmpresas.primero
                    print("Empresas en el sistema: ")
                    for i in range(self.archivo.listaEmpresas.sizeOfList()):
                        print(f"[{empresa.dato.numero}] Nombre: {empresa.dato.nombre}")
                        empresa = empresa.siguiente
                    
                    numero = int(input("Selecciona un número de empresa: "))
                    self.clearConsole()
                    
                    empresa_seleccionada = self.archivo.listaEmpresas.primero
                    for i in range(self.archivo.listaEmpresas.sizeOfList()):
                        if numero == empresa_seleccionada.dato.numero:
                            punto_atencion = empresa_seleccionada.dato.puntosAtencion.primero
                            print(f"Puntos de atención de la empresa '{empresa_seleccionada.dato.nombre}':")
                            for i in range(empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                                print(f"[{punto_atencion.dato.numero}] Código:{punto_atencion.dato.codigo} Nombre:{punto_atencion.dato.nombre}")
                                punto_atencion = punto_atencion.siguiente
                            numero = int(input("Selecciona un número de punto de atención: "))
                            self.clearConsole()
                            punto_seleccionado = empresa_seleccionada.dato.puntosAtencion.primero
                            for i in range(empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                                if numero == punto_seleccionado.dato.numero:
                                    escritorio = punto_seleccionado.dato.escritorios.primero
                                    for i in range(punto_seleccionado.dato.escritorios.sizeOfList()):
                                        print(escritorio.dato.numero, escritorio.dato.codigo, escritorio.dato.identificacion, escritorio.dato.encargado, escritorio.dato.activo)
                                        escritorio = escritorio.siguiente
                                else:
                                    punto_seleccionado = punto_seleccionado.siguiente    
                            break
                        else:
                            empresa_seleccionada = empresa_seleccionada.siguiente


    