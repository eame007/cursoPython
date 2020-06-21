#Desarrolla un programa para calcular perfectamente la nota final.


#Lectura de las 3 notas y alamcenadas en variables

nota_1 = int(input("Introduzca la nota 1: "))
nota_2 = int(input("Introduzca la nota 2: "))
nota_3 = int(input("Introduzca la nota 3: "))

#Calculo de la nota promedio y almacenada en variable promedio

promedio = (nota_1+nota_2+nota_3)/3
print("\nLa nota final es:\t")
print(promedio)
