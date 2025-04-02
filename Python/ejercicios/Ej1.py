class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\n"
    

class Inventario:
    def __init__(self):
        self.inventario=[]
    
    def añadir(self, producto):
        self.inventario.append(producto)

    def eliminar(self, nombre):
        for a in self.inventario:
            if a.nombre ==nombre:
                self.inventario.remove(a)

    def calcularValor(self):
        total=0
        for a in self.inventario:
            total += a.precio*a.cantidad
        return total
    
    def mostrar_inventario(self):
        for producto in self.inventario:
            print(producto)


inventario = Inventario()
global opcion
opcion=5


while opcion!=0:
    print("1. Listar")
    print("2. Añadir")
    print("3. Eliminar")
    print("4. Valor total inventario")

    opcion = int(input("Introduce la opcion: "))

    if opcion == 1:
        inventario.mostrar_inventario()
    elif opcion == 2:
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        producto = Producto(nombre, precio, cantidad)
        inventario.añadir(producto)
    elif opcion ==3:
        nombre = input("Nombre: ")
        inventario.eliminar(nombre)
    elif opcion== 4:
        print(inventario.calcularValor())
    else: 
        opcion= 0
    