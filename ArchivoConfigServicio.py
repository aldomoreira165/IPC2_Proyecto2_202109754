from Lista import Lista
from EscritorioServicio import EscritorioServicio
from PuntoAtencion import PuntoAtencion
from Empresa import Empresa
import xml.etree.ElementTree as ET

class ArchivoConfigServicio:
    
    def __init__ (self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.listaEmpresas = None 
    
    #abriendo documento xml
    def agregarArchivo(self):
        self.listaEmpresas = Lista()
        try:
            xml_file = open(self.ruta_archivo, encoding="utf-8")
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())
                contador_empresas = 0
                for empresa in xml_data.findall("empresa"):
                    identificacion_empresa = empresa.get("id")
                    nombre_empresa = empresa.find("nombre").text
                    abreviatura_empresa = empresa.find("abreviatura").text

                    lista_puntos_atencion = Lista()
                    contador_puntos_atencion = 0
                    puntos_atencion =  xml_data[contador_empresas][2]    
                    
                    for punto_atencion in puntos_atencion:
                        codigo_punto_atencion = punto_atencion.get("id")
                        nombre_punto_atencion = punto_atencion.find("nombre").text
                        direccion_punto_atencion = punto_atencion.find("direccion").text
                        
                        lista_escritorios = Lista()
                        escritorios = puntos_atencion[contador_puntos_atencion][2]
                        contador_escritorios = 0
                        for escritorio in escritorios:
                            codigo_escritorio = escritorio.get("id")
                            identificacion_escritorio = escritorio.find("identificacion").text
                            encargado_escritorio = escritorio.find("encargado").text
                            nuevo_escritorio = EscritorioServicio(contador_escritorios,codigo_escritorio, identificacion_escritorio, encargado_escritorio)
                            lista_escritorios.agregar_final(nuevo_escritorio)
                            contador_escritorios += 1
                            
                        nuevo_punto_atencion = PuntoAtencion(contador_puntos_atencion, codigo_punto_atencion, nombre_punto_atencion, direccion_punto_atencion, lista_escritorios)
                        lista_puntos_atencion.agregar_final(nuevo_punto_atencion)
                        contador_puntos_atencion += 1   
                        
                    nueva_empresa = Empresa(contador_empresas,identificacion_empresa, nombre_empresa, abreviatura_empresa, lista_puntos_atencion)
                    self.listaEmpresas.agregar_final(nueva_empresa)
                    contador_empresas += 1
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()