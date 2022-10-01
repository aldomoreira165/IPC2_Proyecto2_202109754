from os import system
import graphviz

class GeneradorGrafica:
    
    def __init__(self, nombre_empresa, lista_escritorios):
        self.cadena = ""
        self.nombre_empresa = nombre_empresa
        self.lista_escritorios = lista_escritorios
    
    def generar_grafica(self):

        self.cadena += 'digraph L{\n'
        self.cadena += '    node[shape=box, fillcolor="RED" style=filled]\n'
        self.cadena += '    subgraph cluster_p{\n'
        self.cadena += f'       label = "{self.nombre_empresa}"\n'
        self.cadena += '        bgcolor = "BLUE"\n'       
        self.cadena += '        edge[dir = both]\n'
        
        escritorio = self.lista_escritorios.primero
        contador = 0
        for i in range(self.lista_escritorios.sizeOfList()):
            contador += 1
            color = ""
            if escritorio.dato.activo == True:
                color = "GREEN"
            else:
                color = "RED"
            self.cadena +=f'        Fila{contador}[label="{escritorio.dato.codigo}", group =1, fillcolor={color}];\n'
            escritorio = escritorio.siguiente
              
        self.cadena += '    }\n'
        self.cadena += '}\n'
    
        return self.cadena
                       