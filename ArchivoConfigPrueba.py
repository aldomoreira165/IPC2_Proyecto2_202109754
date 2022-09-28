from turtle import pu
from typing import List
import xml.etree.ElementTree as ET
from Lista import Lista
from TransaccionCliente import TransaccionCliente
from Cliente import Cliente

class ArchivoConfigPrueba:

    def ArchivoConfigPrueba(self):
        self.lista_configuraciones = Lista()
        
    def agregar(self, ruta_archivo, archivo):
        try:
            xml_file = open(ruta_archivo, encoding="utf-8")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                contador_configuraciones = 0
                for configuracion in xml_data.findall("configInicial"):
                    id_configuracion = configuracion.get("id")
                    id_empresa = configuracion.get("idEmpresa")
                    id_punto = configuracion.get("idPunto")
                    
                    #almacenando los escritorios activos
                    lista_escritorios_activos = Lista()
                    escritorios_activos = xml_data[contador_configuraciones][0] 
                    
                    for escritorio_activo in escritorios_activos:
                        id_escritorio_activo = escritorio_activo.get("idEscritorio")
                        lista_escritorios_activos.agregar_final(id_escritorio_activo)
                        
                    #almacenando los clientes
                    contador_clientes = 0
                    lista_clientes = Lista()
                    clientela = xml_data[contador_configuraciones][1]
                                        
                    for cliente in clientela:
                        dpi_cliente = cliente.get("dpi")
                        nombre_cliente = cliente.find("nombre").text
                        
                        #almacenando transacciones
                        contador_transacciones = 0
                        lista_transacciones = Lista()
                        transacciones = clientela[contador_clientes][1]
                        for transaccion in transacciones:
                            id_transaccion = transaccion.get("idTransaccion")
                            cantidad_transaccion = transaccion.get("cantidad")
                            transaccion_cliente_nueva = TransaccionCliente(contador_transacciones, id_transaccion, cantidad_transaccion)
                            lista_transacciones.agregar_final(transaccion_cliente_nueva)
                            contador_transacciones += 1
                        
                        nuevo_cliente = Cliente(contador_clientes, dpi_cliente, nombre_cliente, lista_transacciones)
                        lista_clientes.agregar_final(nuevo_cliente)
                        contador_clientes += 1
                        
                    #validando que exista la empresa y el punto de atencion
                    empresa_seleccionada = archivo.listaEmpresas.primero
                    for i in range(archivo.listaEmpresas.sizeOfList()):
                        if empresa_seleccionada.dato.id == id_empresa:
                            break
                        else:
                            empresa_seleccionada = empresa_seleccionada.siguiente
                            
                    punto_atencion_seleccionado = empresa_seleccionada.dato.puntosAtencion.primero
                    for j in range(empresa_seleccionada.dato.puntosAtencion.sizeOfList()):
                        if punto_atencion_seleccionado.dato.codigo == id_punto:
                            break
                        else:
                            punto_atencion_seleccionado = punto_atencion_seleccionado.siguiente 
                            
                    punto_atencion_seleccionado.dato.agregar_clientes(lista_clientes)
                    
                    #activando los escritorios    
                    escritorio = punto_atencion_seleccionado.dato.escritorios.primero       
                    for k in range(punto_atencion_seleccionado.dato.escritorios.sizeOfList()):
                        esc_activo = lista_escritorios_activos.primero
                        for z in range(lista_escritorios_activos.sizeOfList()):
                            if escritorio.dato.codigo == esc_activo.dato: 
                                escritorio.dato.activar_escritorio()
                                escritorio = escritorio.siguiente
                                break
                            elif z+1 == lista_escritorios_activos.sizeOfList():
                                escritorio = escritorio.siguiente
                                break
                            else:
                                esc_activo = esc_activo.siguiente
                                
                            
                    contador_configuraciones += 1
                                            
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()