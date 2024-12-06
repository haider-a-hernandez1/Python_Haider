frutas = ["manzana", "plátano", "cereza"]
print(frutas)




frutas = ["manzana", "plátano", "cereza"]
print(frutas[0])  # Primer elemento
print(frutas[-1])  # Último elemento



frutas = ["manzana", "plátano", "cereza"]
frutas[1] = "pera"  # Cambiar "plátano" por "pera"
print(frutas)



# Usando append()
frutas = ["manzana", "plátano"]
frutas.append("cereza")
print(frutas)

# Usando insert()
frutas.insert(1, "kiwi")  # Insertar "kiwi" en la posición 1
print(frutas)



# Usando remove()
frutas = ["manzana", "plátano", "cereza"]
frutas.remove("plátano")
print(frutas)

# Usando pop()
frutas.pop()  # Elimina el último elemento
print(frutas)

# Usando del
del frutas[0]  # Elimina el primer elemento
print(frutas)

# Usando clear()
frutas.clear()  # Vacía la lista
print(frutas)




frutas = ["manzana", "plátano", "cereza"]

for fruta in frutas:
    print(fruta)




frutas = ["manzana", "plátano", "cereza"]
print("manzana" in frutas)  # True
print("pera" in frutas)  # False




numeros = [4, 2, 9, 1]
numeros.sort()  # Orden ascendente
print(numeros)

numeros.sort(reverse=True)  # Orden descendente
print(numeros)




frutas = ["manzana", "plátano", "cereza"]
print(len(frutas))




frutas = ["manzana", "plátano", "cereza"]

# Usando copy()
copia = frutas.copy()
print(copia)

# Usando slicing
copia2 = frutas[:]
print(copia2)



lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Usando el operador +
resultado = lista1 + lista2
print(resultado)

# Usando extend()
lista1.extend(lista2)
print(lista1)



# Crear una lista con números pares
numeros = [x for x in range(10) if x % 2 == 0]
print(numeros)

# Convertir elementos a mayúsculas
frutas = ["manzana", "plátano", "cereza"]
mayusculas = [fruta.upper() for fruta in frutas]
print(mayusculas)



frutas = ["manzana", "plátano", "cereza"]
indice = frutas.index("plátano")
print(indice)



numeros = [1, 2, 2, 3, 3, 3]
print(numeros.count(2))  # Número de veces que aparece el 2
print(numeros.count(3))  # Número de veces que aparece el 3



numeros = [1, 2, 2, 3, 3, 3]
print(numeros.count(2))  # Número de veces que aparece el 2
print(numeros.count(3))  # Número de veces que aparece el 3




frutas = ["manzana", "plátano", "cereza"]

# Desempaquetar en variables
fruta1, fruta2, fruta3 = frutas
print(fruta1, fruta2, fruta3)

# Desempaquetar con "*"
fruta1, *resto = frutas
print(fruta1, resto)




numeros = [1, 2, 3, 4]
numeros.reverse()
print(numeros)

