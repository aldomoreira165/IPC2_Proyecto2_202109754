from typing import List
from Lista import Lista

lista = Lista()
lista.agregar_final("1")
lista.agregar_final("2")
lista.agregar_final("3")
lista.agregar_final("4")

print(lista.primero.dato)
lista.eliminar_inicio()
lista.eliminar_inicio()

print(lista.primero.dato)