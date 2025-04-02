from turtle import st


class Libro:
    def __init__(self, titulo:str, autor:str, año:int):
        self.titulo= titulo
        self.autor= autor
        self.año= año

    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getAño(self):
        return self.año
    
    def __str__(self):
        return f"\nTitulo: {self.getTitulo()}\nAutor: {self.getAutor()}\nAño: {self.getAño()}\n"

class Biblioteca:
    
    def __init__(self):
        self.inventario=[]
    
    def añadir(self, libro):
        self.inventario.append(libro)

    def buscarLibro(self, busqueda):
        libro=None
        for a in self.inventario:
            if a.getTitulo() == busqueda or a.getAutor() == busqueda:
                libro= a
        return libro

    def eliminar(self, titulo):
        for a in self.inventario:
            if a.titulo == titulo:
                del self.inventario[self.inventario.index(a)]

    def listarLibros(self):
        for a in self.inventario:
            print(a)

    def listarPorAutor(self, autor):
        for a in self.inventario:
            if a.getAutor()==autor:
                print(a)
    
    def prestar(self, libro):
        if self.inventario.count(libro) !=0:
            self.inventario.remove(libro)
        else: print("No se ha encontrado el libro especificado")

    def devolver(self, libro):
        self.inventario.append(libro)
        print("Libro devuelto correctamente, gracias!")

    def cantidadLibros(self):
        return len(self.inventario)
    
    
a=Libro("Juego de tronos", "George", 1990)
b=Libro("Juego de tronos", "George", 1990)
c=Libro("Juego de tronos", "George", 1990)
d=Libro("Juego de tronos", "George", 1990)
e=Libro("Juego de tronos", "George", 1990)
f=Libro("Juego de tronos", "George", 1990)

inventario = Biblioteca()
global opcion
opcion=5
inventario.añadir(a)
inventario.añadir(b)
inventario.añadir(c)
inventario.añadir(d)
inventario.añadir(e)
inventario.añadir(f)

while opcion!=0:
    print("1. Listar")
    print("2. Añadir")
    print("3. Eliminar")
    print("4. Total de libros en el inventario")
    print("5. Prestar")
    print("6. Devolver")
    print("7. Buscar por autor")


    opcion = int(input("Introduce la opcion: "))

    match opcion:
        case 1:
            inventario.listarLibros()
        case 2:
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = int(input("Año: "))

            libro = Libro(titulo, autor, año)
            inventario.añadir(libro)
        case 3:
            titulo = input("Título: ")
            inventario.eliminar(titulo)
        case 4:
            print(inventario.cantidadLibros())
        case 5:
            nombre = input("Nombre: ")
            inventario.prestar(inventario.buscarLibro(nombre))
        case 6:
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = int(input("Año: "))

            libro = Libro(titulo, autor, año)
            inventario.devolver(libro)
        case 7:
            autor = input("Autor: ")
            inventario.listarPorAutor(autor)
        case _: 
            opcion= 0
    

