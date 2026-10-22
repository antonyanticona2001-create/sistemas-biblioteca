import json

class Libreria:
    def __init__(self):
        self.libros = []
        self.cargarlibros()

    def cargarlibros(self):
        with open("libreria.json","r",encoding="utf-8") as archivo:
            self.libros =  json.load(archivo)

    def mostrar(self,libro):
        if libro is not None:
            print(f"Codigo  : {libro['codigo']}")
            print(f"Título  : {libro['titulo']}")
            print(f"Autor   : {libro['autor']}")
            print(f"Año     : {libro['año']}")
            print("-" * 30) 

    def mostrarLibros(self):
        for libro in self.libros:
            print(f"Codigo  : {libro['codigo']}")
            print(f"Título  : {libro['titulo']}")
            print(f"Autor   : {libro['autor']}")
            print(f"Año     : {libro['año']}")
            print("-" * 30)

    def buscarLibro(self,codigo):
        for libro in self.libros:
            if codigo.lower() == libro["codigo"].lower():
                return libro
            
        return None