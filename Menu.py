from ArchivoConfigServicio import ArchivoConfigServicio
from ArchivoConfigPrueba import ArchivoConfigPrueba
import os

class Menu:
    
    def __init__ (self):
        self.archivo = None
        self.archivop = None
        self.empresa_seleccionada = None
        self.punto_seleccionado = None
        
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
                    
                    self.empresa_seleccionada = self.archivo.listaEmpresas.primero
                    for i in range(self.archivo.listaEmpresas.sizeOfList()):
                        if self.empresa_seleccionada.dato.numero == numero:
                            break
                    else:
                        self.empresa_seleccionada = self.empresa_seleccionada.siguiente
                        
                    punto = self.empresa_seleccionada.dato.puntosAtencion.primero    
                    print(f"Puntos de atención de la empresa '{self.empresa_seleccionada.dato.nombre}': ")
                    for i in range(self.empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                        print(f"[{punto.dato.numero}] Nombre: {punto.dato.nombre}")
                        punto = punto.siguiente
                    
                    numero = int(input("Selecciona un punto de atención: "))
                    self.clearConsole()
                        
                    self.punto_seleccionado = self.empresa_seleccionada.dato.puntosAtencion.primero
                    for j in range(self.empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                        if self.punto_seleccionado.dato.numero == numero:
                            print("Punto de atención seleccionado correctamente.")
                            break
                        else:
                            self.punto_seleccionado = self.punto_seleccionado.siguiente
                    
            elif opcion == 3:
                print("**********************************************")
                print("*1.Ver estado del punto de atención          *")
                print("*2.Activar escritorio de servicio            *")
                print("*3.Desactivar escritorio                     *")
                print("*4.Atender cliente                           *")
                print("*5.Solicitud de atención                     *")
                print("*6.Simular actividad del punto de atención   *")
                print("**********************************************")
                opcion = int(input("Seleccione una opción: "))
                self.clearConsole()
                
                if opcion == 1:
                    if self.punto_seleccionado == None:
                        print("No ha seleccionado ningun punto de atención.")
                    else:
                        print(f"Punto de atención seleccionado: {self.punto_seleccionado.dato.nombre}")
                
                


    