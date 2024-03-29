from os import system
import graphviz

class GeneradorGrafica:
    
    def __init__(self, nombre_empresa, lista_escritorios, cola_clientes, clientes_en_atencion):
        self.cadena = ""
        self.nombre_empresa = nombre_empresa
        self.lista_escritorios = lista_escritorios
        self.cola_clientes = cola_clientes
        self.clientes_en_atencion = clientes_en_atencion
        self.numero_clientes_atendidos = 0 
    
    def generar_grafica(self):
        numero_columnas = []
        
        #cadena de estructura inicial
        self.cadena += 'digraph L{\n'
        self.cadena += '    node[shape=box, fillcolor="ORANGE" style=filled]\n'
        self.cadena += '    subgraph cluster_p{\n'
        self.cadena += f'       label = "{self.nombre_empresa}"\n'
        self.cadena += '        bgcolor = "BLUE"\n'       
        self.cadena += '        raiz[label = "Entrada a escritorios"]\n'       
        self.cadena += '        edge[dir = both]\n'
         
        #ciclo para hacer las filas de los  clientes 
        cliente = self.cola_clientes.primero
        contador_clientes_espera = 0
        
        if self.cola_clientes.sizeOfList() > 0:
            for i in range(self.cola_clientes.sizeOfList()):
                if cliente.dato.atendido == False:
                    contador_clientes_espera += 1
                    self.cadena +=f'        Fila{contador_clientes_espera}[label="{cliente.dato.nombre}", group =1, fillcolor=YELLOW];\n'
                    cliente = cliente.siguiente
                else:
                    cliente = cliente.siguiente
        
        #ciclo para enlazar las filas                     
        for j in range(contador_clientes_espera-1):
            self.cadena += f'       Fila{j+1}->Fila{j+2};\n'
            
        #ciclo para unir las columnas de los escritorios de servicio
        escritorio = self.lista_escritorios.primero
        contador_escritorios = 0
        cadena_columnas = ''
        for i in range(self.lista_escritorios.sizeOfList()):
            contador_escritorios += 1
            if contador_escritorios == self.lista_escritorios.sizeOfList():
                cadena_columnas += f'Columna{contador_escritorios}'
            else:
                cadena_columnas += f'Columna{contador_escritorios};'
            color = ""
            if escritorio.dato.activo == True:
                color = "GREEN"
                numero_columnas.append(i+1)
            else:
                color = "RED"
            self.cadena +=f'        Columna{contador_escritorios}[label="{escritorio.dato.codigo}", group ={contador_escritorios+1}, fillcolor={color}];\n'
            escritorio = escritorio.siguiente

        #ciclo para enlazar a los escritorios de servicio
        for n in range(contador_escritorios-1):
            self.cadena += f'       Columna{n+1}->Columna{n+2};\n'
         
        #aqui vamos a unir la raiz a las filas y las columnas    
        self.cadena += '        raiz->Fila1;\n'  
        self.cadena += '        raiz->Columna1;\n'
        
        #aquí vamos a alinear cada nodo cabecera a las columnas
        self.cadena += '        {'+f'rank=same;raiz;{cadena_columnas}'+'}\n'
        
        if self.clientes_en_atencion != None:
            cliente_proceso = self.clientes_en_atencion.primero
            for k in range(self.clientes_en_atencion.sizeOfList()):
                self.cadena += f'        Nodo{k+1}[label="{cliente_proceso.dato.nombre}", fillcolor="YELLOW", group={k+2}\n]'
                cliente_proceso = cliente_proceso.siguiente
        else:
            pass
        
        if self.clientes_en_atencion != None:
            for k in range(self.clientes_en_atencion.sizeOfList()):
                self.cadena += f'        Columna{numero_columnas[k]}->Nodo{k+1}\n'
        else:
            pass
        
                     
        self.cadena += '    }\n'
        self.cadena += '}\n'
    
        return self.cadena
                       