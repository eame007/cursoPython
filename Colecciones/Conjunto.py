#1) Realiza un programa que siga las siguientes instrucciones: 
# Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
# Crea un conjunto llamado administradores con los administradores Juan y Marta.
# Borra al administrador Juan del conjunto de administradores.
# Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
# Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
# Notas: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "no es admin")