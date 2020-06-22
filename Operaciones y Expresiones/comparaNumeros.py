'''

1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero

'''

#Lectura de los numeros
n = int(input("Ingresa el primer numero: "))
m = int(input("\nIngresa el segundo numero: "))

#Impresion de resultados
print("\nSi los dos números son iguales\t", n==m)
print("\nSi los dos números son diferentes\t", n!=m)
print("\nSi el primero es mayor que el segundo\t",n>m)
print("\nSi el segundo es mayor o igual que el primero\t",n<=m)