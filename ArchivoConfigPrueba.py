from turtle import pu
from typing import List
import xml.etree.ElementTree as ET
from Lista import Lista

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
                    
                    lista_escritorios_activos = Lista()
                    escritorios_activos = xml_data[contador_configuraciones][0] 
                    #almacenando los escritorios activos
                    for escritorio_activo in escritorios_activos:
                        id_escritorio_activo = escritorio_activo.get("idEscritorio")
                        lista_escritorios_activos.agregar_final(id_escritorio_activo)
                    
                    #validando que exista la empresa y el punto de atencion
                    empresa = archivo.listaEmpresas.primero
                    for i in range(archivo.listaEmpresas.sizeOfList()):
                        if empresa.dato.id == id_empresa:
                            punto = empresa.dato.puntosAtencion.primero
                            for j in range(empresa.dato.puntosAtencion.sizeOfList()):
                                if punto.dato.codigo == id_punto:
                                    escritorio = punto.dato.escritorios.primero
                                    for k in range(punto.dato.escritorios.sizeOfList()):
                                        print(escritorio.dato.codigo)  
                                        escritorio = escritorio.siguiente                                                                                 
                                else:
                                    punto = punto.siguiente
                        else: 
                            empresa = empresa.siguiente
                            
                    contador_configuraciones += 1
                                            
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()