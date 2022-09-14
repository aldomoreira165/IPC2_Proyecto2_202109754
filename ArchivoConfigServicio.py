from Lista import Lista
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
                for empresa in xml_data.findall('listaEmpresas'):
                    print(empresa)
        except Exception as err:
            print("Error: ", err)
        finally:
            xml_file.close()
            
a = ArchivoConfigServicio("a.xml")
a.agregarArchivo()