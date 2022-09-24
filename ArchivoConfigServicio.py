from Lista import Lista
from EscritorioServicio import EscritorioServicio
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
                    identificacion = empresa.get("id")
                    nombre = empresa.find("nombre").text
                    abreviatura = empresa.find("abreviatura").text
                    
                    #lista de escritorios para los puntos de atencion
                    lista_escritorios = Lista()
                    puntos_atencion =  xml_data[contador_empresas][2]
                    escritorios = puntos_atencion[0][2]
                    
                    for escritorio in escritorios:
                        codigo_escritorio = escritorio.get("id")
                        identificacion_escritorio = escritorio.find("identificacion").text
                        encargado_escritorio = escritorio.find("encargado").text
                        nuevo_escritorio = EscritorioServicio(codigo_escritorio, identificacion_escritorio, encargado_escritorio)
                        lista_escritorios.agregar_final(nuevo_escritorio)
                        
                    #lista de puntos de atencion 
                    lista_puntos_atencion = Lista()
                    puntos_atencion =  xml_data[contador_empresas][2]
                    
                    for punto_atencion in puntos_atencion:
                        codigo_punto_atencion = punto_atencion.get("id")
                        nombre_punto_atencion = punto_atencion.find("nombre").text
                        direccion_punto_atencion = punto_atencion.find("direccion").text
                                           
                    
                    contador_empresas += 1
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()
            
a = ArchivoConfigServicio("a.xml")
a.agregarArchivo()