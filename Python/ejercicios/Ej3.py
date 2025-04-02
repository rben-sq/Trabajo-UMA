class Animal:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def hacerSonido(self):
        print("Grrrrr")

class Perro(Animal) :
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacerSonido(self):
        print("Guau")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacerSonido(self):
        print("Miau")

toby= Perro("Toby")
lucky= Perro("Lucky")
chispa= Perro("Chispa")

misifu= Gato("Misifí")
leo= Gato("Leo")
gato= Gato("Gato")


lista = [toby, misifu, leo, lucky, gato, chispa]

for a in lista:
    a.hacerSonido()