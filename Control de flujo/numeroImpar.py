#2) Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, 
# debe repetise el proceso hasta que lo introduzca correctamente.

#Lectura del numero
numero = int(input("\nIngresa un numero impar:\t "))

while( (numero%2) == 0):
    numero = int(input("""
    El numero ingresado NO es valido.
    Ingresa un numero impar:\t """))