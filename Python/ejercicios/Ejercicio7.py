# Pirámide de Asteriscos
# Este ejercicio pide imprimir una pirámide de asteriscos 
# con la altura que el usuario ingrese.

altura = int(input("Introduce la altura de la pirámide: "))

for i in range(1, altura + 1):
    print(" " * (altura - i) + "*" * (2 * i - 1))
