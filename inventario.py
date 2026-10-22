from time import sleep

class Inventario:
    def __init__(self):
        self.miInventario = []

    def subirLibro(self,libro_nuevo):
        if libro_nuevo is not None:
            if len(self.miInventario)>0:
                for libro in self.miInventario:
                    if libro_nuevo["codigo"].lower() == libro["codigo"].lower():
                        print("Ya tienes este libro en tu inventario")
                        return
        
        
            self.miInventario.append(libro_nuevo)


    def mostrarMiInventario(self):
        print("==== Mi Inventario ====")
        if len(self.miInventario)>0:
            for libro in self.miInventario:
                print(f"Codigo  : {libro['codigo']}")
                print(f"Título  : {libro['titulo']}")
                print(f"Autor   : {libro['autor']}")
                print(f"Año     : {libro['año']}")
                print("-" * 30) 
        else:
            print("Aun no tienes libros agregados")

    def eliminarLibro(self,codigo):
        libro_encontrado = None
        for libro in self.miInventario:
            if codigo.lower() == libro["codigo"].lower():
                libro_encontrado = libro

        if libro_encontrado is not None:
            print("El libro ")
            print(f"Codigo  : {libro_encontrado['codigo']}")
            print(f"Título  : {libro_encontrado['titulo']}")
            print(f"Autor   : {libro_encontrado['autor']}")
            print(f"Año     : {libro_encontrado['año']}")
            print("-" * 30) 
            print("Se elimino correctamente")
            self.miInventario.remove(libro_encontrado)
        else:
            print(f"El libro con el codigo:{codigo.upper()}, no se encentra en tu inventario")