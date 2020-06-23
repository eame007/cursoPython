'''

1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta

'''

#Lectura de los numeros
n = int(input("Ingresa el primer numero: "))
m = int(input("Ingresa el segundo numero: "))

#Lectura de la opcion del menu
opcion = int(input("""
Selecccione una opcion:
1. Mostrar una suma de los dos números
2.Mostrar una resta de los dos números (el primero menos el segundo)
3.Mostrar una multiplicación de los dos números\t"""))

print(opcion)
#Ciclo while para validar la opcion seleccionada

while(opcion >3 or opcion<1):
    print("\nLa opcion seleccionada no es valida ")

    opcion = int(input("""
    Selecccione una opcion:
    1. Mostrar una suma de los dos números
    2.Mostrar una resta de los dos números (el primero menos el segundo)
    3.Mostrar una multiplicación de los dos números\t""")))

#condicionales anidadas para la opcion seleccionada
if(opcion == 1):
    print("\nLa suma de los dos números es: ", (n+m))
elif(opcion == 2):
    print("\nLa resta de los dos números es: ", (n-m))
else:
    print("\nEl producto de los dos números es: ", (n*m))