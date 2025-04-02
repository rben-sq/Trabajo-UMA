año_1= int(input ("Introduce el primer año: "))
año_f= int(input ("Introduce el último año: "))
años = []
for i in range(año_1, año_f+1):
    años.append(i)

""" for i in range(len(años)):
    pass """

print ("Introduce los ingresos de cada año")
beneficios = []
for i in años:
    print(i, ": ", sep='', end='')
    beneficios.append(int(input()))

print ("Introduce los gastos de cada año")
gastos = []
profit = []
for i in años:
    print(i, ": ", sep='', end='')
    gastos.append(int(input()))

print("")
print("Lista de resumen: ")
for i in años:
    print(i, ": ", " Beneficios: ", beneficios[años.index(i)],", Gastos: ", gastos[años.index(i)],", Han habido beneficios?: ", beneficios[años.index(i)] > gastos[años.index(i)] , sep='')
