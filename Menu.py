from ArchivoConfigServicio import ArchivoConfigServicio
from ArchivoConfigPrueba import ArchivoConfigPrueba
from Cliente import Cliente
from Lista import Lista
from GeneradorGrafica import GeneradorGrafica
import os
from TransaccionCliente import TransaccionCliente

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
            print("*4.Salir                                       *")
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
                        self.archivop = None
                        self.empresa_seleccionada = None
                        self.punto_seleccionado = None
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
                    if self.archivop == None:
                        print("No has ingresado ningún archivo de prueba.")
                    else:
                        if self.punto_seleccionado == None:
                            print("No ha seleccionado ningun punto de atención.")
                        else:
                            contador_escritorios_activos = 0
                            contador_escritorios_inactivos = 0
                            cantidad_clientes_espera = self.punto_seleccionado.dato.clientes.sizeOfList()
                            suma_tiempos = 0
                            contador_tiempos = 0
                            tiempo_promedio_espera = 0
                            print(f"Empresa seleccionada: {self.empresa_seleccionada.dato.nombre}")
                            print(f"Punto de atención seleccionado: {self.punto_seleccionado.dato.nombre}")
                            print("")
                            escritorio = self.punto_seleccionado.dato.escritorios.primero
                            for i in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                                if escritorio.dato.activo == True:
                                    contador_escritorios_activos += 1
                                    escritorio = escritorio.siguiente
                                else:
                                    contador_escritorios_inactivos += 1
                                    escritorio = escritorio.siguiente
                                                        
                            print(f"Cantidad de escritorios de servicio activos: {contador_escritorios_activos}")
                            print(f"Cantidad de escritorios de servicio inactivos: {contador_escritorios_inactivos}")
                            print(f"Cantidad de clientes en espera: {cantidad_clientes_espera}")
                            
                            cliente = self.punto_seleccionado.dato.clientes.primero
                            for i in range(self.punto_seleccionado.dato.clientes.sizeOfList()):
                                transaccion = cliente.dato.transacciones.primero
                                for j in range(cliente.dato.transacciones.sizeOfList()):
                                    transaccion_empresa = self.empresa_seleccionada.dato.transacciones.primero
                                    for k in range(self.empresa_seleccionada.dato.transacciones.sizeOfList()):
                                        if transaccion.dato.codigo == transaccion_empresa.dato.identificacion:
                                            suma_tiempos += int(transaccion_empresa.dato.tiempo)
                                            contador_tiempos += 1
                                            transaccion = transaccion.siguiente
                                            break
                                        elif k+1 == self.empresa_seleccionada.dato.transacciones.sizeOfList():
                                            transaccion = transaccion.siguiente
                                            break
                                        else:
                                            transaccion_empresa = transaccion_empresa.siguiente
                                cliente = cliente.siguiente
                                
                            tiempo_promedio_espera = round(suma_tiempos/contador_tiempos,2)    
                            print(f"Tiempo promedio de atención: {tiempo_promedio_espera} minutos")
                
                            escritorio = self.punto_seleccionado.dato.escritorios.primero
                            for i in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                                if escritorio.dato.activo == True:
                                    contador_escritorios_activos += 1
                                    escritorio = escritorio.siguiente
                                else:
                                    contador_escritorios_inactivos += 1
                                    escritorio = escritorio.siguiente
                elif opcion == 2:
                    if self.archivo == None:
                        print("No hay datos existentes. Verifica que hayas ingresado un archivo al sistema.")
                    else:
                        if self.punto_seleccionado == None:
                            print("No ha seleccionado ningun punto de atención.")
                        else:
                            print(f"Empresa seleccionada: {self.empresa_seleccionada.dato.nombre}")
                            print(f"Punto de atención seleccionado: {self.punto_seleccionado.dato.nombre}")
                            print("")
                            codigo_escritorio_activar = input("Ingrese el código del escritorio que desea activar: ")
                            
                            escritorio = self.punto_seleccionado.dato.escritorios.primero
                            for i in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                                if codigo_escritorio_activar == str(escritorio.dato.codigo):
                                    escritorio.dato.activar_escritorio()
                                    break
                                else:
                                    escritorio = escritorio.siguiente
                elif opcion == 3:
                    if self.archivo == None:
                        print("No hay datos existentes. Verifica que hayas ingresado un archivo al sistema.")
                    else:
                        if self.punto_seleccionado == None:
                            print("No ha seleccionado ningun punto de atención.")
                        else:
                            print(f"Empresa seleccionada: {self.empresa_seleccionada.dato.nombre}")
                            print(f"Punto de atención seleccionado: {self.punto_seleccionado.dato.nombre}")
                            print("")
                            codigo_escritorio_activar = input("Ingrese el código del escritorio que desea desactivar: ")
                            
                            escritorio = self.punto_seleccionado.dato.escritorios.primero
                            for i in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                                if codigo_escritorio_activar == str(escritorio.dato.codigo):
                                    escritorio.dato.desactivar_escritorio()
                                    break
                                else:
                                    escritorio = escritorio.siguiente
                elif opcion == 4:
                    cola_clientes = Lista()
                    cliente = self.punto_seleccionado.dato.clientes.primero
                    for i in range(self.punto_seleccionado.dato.clientes.sizeOfList()):
                        if cliente.dato.atendido == False:
                            cola_clientes.agregar_final(cliente)
                            cliente = cliente.siguiente
                        else:
                            cliente = cliente.siguiente                         
                    
                    pila_escritorios_activos = Lista()   
                    escritorio = self.punto_seleccionado.dato.escritorios.primero
                    for j in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                        if escritorio.dato.activo == True:
                            pila_escritorios_activos.agregar_final(escritorio)
                            escritorio = escritorio.siguiente
                        else:
                            escritorio = escritorio.siguiente
                    
                    #atendiendo clientes
                    escritorio_activo = pila_escritorios_activos.primero
                    for k in range(pila_escritorios_activos.sizeOfList()):
                        if cola_clientes.sizeOfList() > 0:
                            cliente_en_cola = cola_clientes.primero
                            if escritorio_activo.dato.dato.libre == True:
                                escritorio_activo.dato.dato.ocupar_escritorio()
                                print(cliente_en_cola.dato.dato.nombre, escritorio_activo.dato.dato.codigo)
                                
                                #marcando a cliente como atendido
                                cliente_atendido = self.punto_seleccionado.dato.clientes.primero
                                for n in range(self.punto_seleccionado.dato.clientes.sizeOfList()):
                                    if cliente_atendido.dato.dpi == cliente_en_cola.dato.dato.dpi:
                                        cliente_atendido.dato.servido()
                                        cliente_atendido = cliente_atendido.siguiente
                                    else: 
                                        cliente_atendido = cliente_atendido.siguiente
                                
                                cola_clientes.eliminar_inicio()
                                escritorio_activo = escritorio_activo.siguiente
                            else:
                                escritorio_activo = escritorio_activo.siguiente
                                escritorio_activo.dato.dato.ocupar_escritorio()
                                print(cliente_en_cola.dato.dato.nombre, escritorio_activo.dato.dato.codigo)
                                
                                #marcando a cliente como atendido
                                cliente_atendido = self.punto_seleccionado.dato.clientes.primero
                                for n in range(self.punto_seleccionado.dato.cliente.sizeOfList()):
                                    if cliente_atendido.dato.dpi == cliente_en_cola.dato.dato.dpi:
                                        cliente_atendido.dato.servido()
                                        cliente_atendido = cliente_atendido.siguiente
                                    else: 
                                        cliente_atendido = cliente_atendido.siguiente
                                
                                cola_clientes.eliminar_inicio()
                                escritorio_activo = escritorio_activo.siguiente
                        else:
                            break
                                
                    #liberando escritorios luego de haberlos atendido
                    escritorio = self.punto_seleccionado.dato.escritorios.primero
                    for z in range(self.punto_seleccionado.dato.escritorios.sizeOfList()):
                        if escritorio.dato.libre == False:
                            escritorio.dato.liberar_escritorio()
                            escritorio = escritorio.siguiente
                        else:
                            escritorio = escritorio.siguiente                            
                    
                elif opcion == 5:
                    contador_transacciones = 0
                    dpi_cliente = input("Ingrese el DPI del cliente: ")
                    nombre_cliente = input("Ingrese el nombre del cliente: ")
                    self.clearConsole()
 
                    lista_transacciones = Lista()
                    transaccion = self.empresa_seleccionada.dato.transacciones.primero
                    for i in range(self.empresa_seleccionada.dato.transacciones.sizeOfList()):
                        print(transaccion.dato.identificacion, transaccion.dato.nombre)
                        respuesta =  (input("¿Desea agregar esta transacción a su lista de transacciones? S/N")).lower()
                        if respuesta == "s":
                            cantidad_transacciones = int(input("Ingrese la cantidad de transacciones de este tipo que desea realizar: "))
                            contador_transacciones += 1
                            nueva_transaccion = TransaccionCliente(contador_transacciones, transaccion.dato.identificacion, cantidad_transacciones)
                            lista_transacciones.agregar_final(nueva_transaccion)
                            transaccion = transaccion.siguiente
                        else:
                            transaccion = transaccion.siguiente
                            
                    nuevo_cliente = Cliente(dpi_cliente, nombre_cliente, lista_transacciones, False)
                    self.punto_seleccionado.dato.clientes.agregar_final(nuevo_cliente)
                    self.clearConsole()
                    print("Solicitud de atención agregada correctamente.")
                elif opcion == 6:
                    grafica = GeneradorGrafica(self.empresa_seleccionada.dato.nombre, self.punto_seleccionado.dato.escritorios, self.punto_seleccionado.dato.clientes)
                    graph = grafica.generar_grafica()
                    miArchivo = open('graphviz.dot', 'w')
                    miArchivo.write(graph)
                    miArchivo.close()
                    
                    os.system('dot -Tpng graphviz.dot -o graphviz.png')

            elif opcion == 4:
                print("Has salido del sistema.")
                exit()
                    
                    
    