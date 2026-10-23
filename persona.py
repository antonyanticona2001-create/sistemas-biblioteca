from libreria import Libreria
from inventario import Inventario
import json

class Persona:
    def __init__(self):
        self.libreria = Libreria()
        self.inventario = Inventario()
        pass

class Estudiante(Persona):
    def __init__(self, codigo,nombre,tipo,carrera):
        super().__init__(codigo)
        self.nombre = nombre
        self.tipo = tipo
        self.carrera = carrera


class Profesor(Persona):
    def __init__(self, codigo,nombre,tipo,maestria,curso):
        super().__init__(codigo)
        self.nombre = nombre
        self.tipo = tipo
        self.maestria = maestria
        self.curso = curso

def cargar_usuarios():
    usuarios = []

    with open ("usuarios.json","r",encoding="utf-8") as archivo:
        usuarios = json.load(archivo)
    return usuarios

codigo_ingresado = "U7700"

def buscar_usuario(codigo,lista):
    for usuario in lista:
        if codigo.lower == usuario["codigo"]:
            return usuario
        

persona1 = Persona()


libro = persona1.libreria.buscarLibro("lib002")
libro2 = persona1.libreria.buscarLibro("lib008")



persona1.inventario.subirLibro(libro)
persona1.inventario.subirLibro(libro2)

persona1.inventario.mostrarMiInventario()

persona1.inventario.eliminarLibro("lib008")

persona1.inventario.mostrarMiInventario()



