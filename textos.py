nombre = "Haider"
numero_1 = 10
numero_2 = 15
resultado = numero_1 + numero_2
print(resultado)
print(nombre.upper())



texto = "   Hola mundo   "
resultado = texto.strip()
print(f"Texto original: '{texto}'")
print(f"Texto después de strip(): '{resultado}'")



lineas = ["   Hola   ", "  Mundo  ", " Python  "]
lineas_limpias = [linea.strip() for linea in lineas]
print(f"Líneas originales: {lineas}")
print(f"Líneas después de strip(): {lineas_limpias}")



texto = "Hola mundo"
resultado = texto.replace("mundo", "Python")
print(f"Texto original: '{texto}'")
print(f"Texto después de replace(): '{resultado}'")

# Ejemplos de operadores aritméticos
x = 10
y = 3
print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x % y)   # 1
print(x ** y)  # 1000
print(x // y)  # 3

# Ejemplos de operadores lógicos
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# Ejemplos de operadores de asignación
x = 5
x += 3   # x = x + 3 -> x es ahora 8
x -= 2   # x = x - 2 -> x es ahora 6
x *= 4   # x = x * 4 -> x es ahora 24
x /= 6   # x = x / 6 -> x es ahora 4.0

def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()  # Imprime "¡Hola, mundo!"

num_1 = int(input("Ingrese numero 1"))
num_2 = int(input("ingrese numero 2"))

result = (num_1 + num_2)
print(result)