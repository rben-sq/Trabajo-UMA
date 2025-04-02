class Titular:
    def __init__(self, edad):
        self.edad=edad
    def getEdad(self):
        return self.edad


class CuentaJoven:
    def __init__(self, titular, saldo, bonificacion):
        if self.esTitularValido(titular):
            self.titular= titular
            self.saldo= saldo
            self.bonificacion= bonificacion
        else:
            del self
            print("No se ha podido crear la cuenta, el titular no es válido")
    
    def getTitular(self):
        return self.titular
    
    def getSaldo(self):
        return self.saldo
    
    def getBonificacion(self):
        return self.bonificacion
    
    def setTitular(self, titular):
        self.titular=titular
    
    def setSaldo(self, saldo):
        self.saldo= saldo
    
    def setBonificacion(self, bonificacion):
        self.bonificacion= bonificacion
    

    def esTitularValido(self, titular):
        return titular.getEdad()>=18 and titular.getEdad()<=25
    
    def retirarSaldo(self, cantidad):
        if cantidad > self.getSaldo():
            print("No hay suficiente saldo")
        else:
            self.setSaldo(self.getSaldo()-cantidad)
            print(f"Se han retirado {cantidad}€ de la cuenta, quedan {self.getSaldo()}")

    def mostrar(self):
        return f"\nCuenta Joven\n============\n\nBonificación: {self.getBonificacion()}%\n"
    
pepe= Titular(22)
pepa= Titular(12)
a= CuentaJoven(pepe, 20, 5)
b= CuentaJoven(pepa, 50, 15)
print(a.esTitularValido(a.getTitular()))
""" print(b.esTitularValido(b.getTitular())) """

print(a.getTitular().getEdad())
""" print(b.getTitular().getEdad()) """

print(a.mostrar())
""" print(b.mostrar()) """

