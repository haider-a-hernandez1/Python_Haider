# Ejemplo: Días de la semana
def dia_de_la_semana(dia):
            match dia:
                case "lunes":
                    return "Inicio de la semana laboral."
                case "viernes":
                    return "¡Es viernes, casi fin de semana!"
                case "sábado" | "domingo":
                    return "Fin de semana."
                case _:
                    return "Día no válido."
        
        # Uso del switch
print(dia_de_la_semana("lunes"))   # Salida: Inicio de la semana laboral.
print(dia_de_la_semana("sábado")) # Salida: Fin de semana.



edad = 18

if edad >= 18:
    print("Eres mayor de edad.")


hora = 14

if hora < 12:
    print("Buenos días")
else:
    print("Buenas tardes")


nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Aprobado")
else:
    print("Reprobado")


edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)


hora = 10
dia = "lunes"

if hora < 12 and dia == "lunes":
    print("Es lunes por la mañana.")


numero = 5

if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.")
else:
    print("El número es negativo.")



frutas = ["manzana", "plátano", "naranja"]

if "manzana" in frutas:
    print("La manzana está en la lista.")
else:
    print("La manzana no está en la lista.")



usuario = "admin"

if usuario == "admin":
    print("Bienvenido, administrador.")
else:
    print("Acceso denegado.")


numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")



edad = 16

if edad >= 18:
    pass  # Este bloque se deja vacío por ahora
else:
    print("Eres menor de edad.")





numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")



numero = 7
resultado = "Par" if numero % 2 == 0 else "Impar"
print(resultado)  # Impar



edad = 17
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Menor de edad



a, b = 5, 10
mayor = a if a > b else b
print(mayor)  # 10




numero = -3
tipo = "Positivo" if numero > 0 else "Negativo"
print(tipo)  # Negativo


frutas = ["manzana", "pera", "naranja"]
mensaje = "Fruta encontrada" if "pera" in frutas else "Fruta no encontrada"
print(mensaje)  # Fruta encontrada



password = "1234"
mensaje = "Acceso concedido" if password == "1234" else "Acceso denegado"
print(mensaje)  # Acceso concedido



anio = 2024
es_bisiesto = "Bisiesto" if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0) else "No bisiesto"
print(es_bisiesto)  # Bisiesto



texto = ""
estado = "Vacío" if not texto else "No vacío"
print(estado)  # Vacío


monto = 120
descuento = 0.1 if monto > 100 else 0.05
print(descuento)  # 0.1



rol = "admin"
acceso = "Acceso permitido" if rol == "admin" else "Acceso denegado"
print(acceso)  # Acceso permitido



edad = 20

if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes 18 años.")
else:
    print("Eres mayor de edad.")




edad = 25

if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")



edad = 65

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")


a, b = 10, 20

if a > b:
    print("a es mayor que b.")
elif a < b:
    print("a es menor que b.")
else:
    print("a y b son iguales.")



numero = -5

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Aprobado")
elif nota >= 50:
    print("Necesitas mejorar")
else:
    print("Reprobado")



usuario = input("Ingresa tu usuario: ")

if usuario == "admin":
    print("Bienvenido, administrador.")
elif usuario == "invitado":
    print("Bienvenido, invitado.")
else:
    print("Usuario no reconocido.")




color = "rojo"

if color == "rojo":
    print("El color es rojo.")
elif color == "azul":
    print("El color es azul.")
elif color == "verde":
    print("El color es verde.")
else:
    print("Color no identificado.")


frutas = ["manzana", "pera", "naranja"]

if "pera" in frutas:
    print("La lista contiene una pera.")
elif "uva" in frutas:
    print("La lista contiene una uva.")
else:
    print("La lista no contiene peras ni uvas.")



palabra = "Python"

if palabra == "python":
    print("La palabra es 'python'.")
elif palabra.lower() == "python":
    print("La palabra es 'Python' (ignorando mayúsculas).")
else:
    print("La palabra no es 'python'.")



anio = 2023

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("Es un año bisiesto.")
        else:
            print("No es un año bisiesto.")
    else:
        print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.")




experiencia = 5

if experiencia < 1:
    print("Nivel: Principiante")
elif 1 <= experiencia <= 3:
    print("Nivel: Intermedio")
elif experiencia > 3:
    print("Nivel: Avanzado")
else:
    print("Nivel desconocido.")



edad = 30
nacionalidad = "colombiano"

if edad >= 18 and nacionalidad == "colombiano":
    print("Eres mayor de edad y colombiano.")
elif edad >= 18:
    print("Eres mayor de edad, pero no colombiano.")
else:
    print("Eres menor de edad.")




dia = "sábado"

if dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "jueves" or dia == "viernes":
    print("Es un día laboral.")
elif dia == "sábado" or dia == "domingo":
    print("Es un día de descanso.")
else:
    print("Día inválido.")




dia = "viernes"

match dia:
    case "lunes":
        print("Hoy es lunes, inicio de semana.")
    case "martes":
        print("Hoy es martes, segundo día de la semana.")
    case "viernes":
        print("Hoy es viernes, último día laboral.")
    case _:
        print("Día no especificado.")



def lunes():
    return "Hoy es lunes, inicio de semana."

def martes():
    return "Hoy es martes, segundo día de la semana."

def otros_dias():
    return "Día no especificado."

# Simulación del switch con un diccionario
dias = {
    "lunes": lunes,
    "martes": martes
}

dia = "lunes"
print(dias.get(dia, otros_dias)())  # Llama a la función asociada al día




operacion = "+"
a, b = 10, 5

match operacion:
    case "+":
        print(f"Resultado: {a + b}")
    case "-":
        print(f"Resultado: {a - b}")
    case "*":
        print(f"Resultado: {a * b}")
    case "/":
        print(f"Resultado: {a / b}")
    case _:
        print("Operación no válida.")





nivel = "admin"

match nivel:
    case "admin":
        print("Tienes acceso completo al sistema.")
    case "editor":
        print("Puedes editar contenido, pero no configuraciones.")
    case "viewer":
        print("Solo tienes permisos de lectura.")
    case _:
        print("Nivel de acceso no reconocido.")



        nivel = "admin"

match nivel:
    case "admin":
        print("Tienes acceso completo al sistema.")
    case "editor":
        print("Puedes editar contenido, pero no configuraciones.")
    case "viewer":
        print("Solo tienes permisos de lectura.")
    case _:
        print("Nivel de acceso no reconocido.")




def get_mes(mes):
    return {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }.get(mes, "Mes no válido")

mes = 7
print(get_mes(mes))




calificacion = 85

match calificacion:
    case _ if calificacion >= 90:
        print("Excelente")
    case _ if 75 <= calificacion < 90:
        print("Muy bien")
    case _ if 50 <= calificacion < 75:
        print("Aprobado")
    case _:
        print("Reprobado")




animal = "perro"

match animal:
    case "gato":
        print("El animal dice: Miau.")
    case "perro":
        print("El animal dice: Guau.")
    case "vaca":
        print("El animal dice: Muuu.")
    case _:
        print("Sonido desconocido.")



operaciones = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "División por cero"
}

a, b = 10, 2
operacion = "*"

print(operaciones.get(operacion, lambda x, y: "Operación no válida")(a, b))



numero = 0

match numero:
    case _ if numero > 0:
        print("El número es positivo.")
    case _ if numero < 0:
        print("El número es negativo.")
    case _:
        print("El número es cero.")




transporte = "avión"

match transporte:
    case "carro":
        print("Elegiste viajar en carro. Velocidad promedio: 100 km/h.")
    case "tren":
        print("Elegiste viajar en tren. Velocidad promedio: 200 km/h.")
    case "avión":
        print("Elegiste viajar en avión. Velocidad promedio: 800 km/h.")
    case _:
        print("Medio de transporte no válido.")




# Bucles

frutas = ["manzana", "plátano", "cereza"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")




# Imprimir números del 0 al 4
for i in range(5):
    print(f"Número: {i}")

# Imprimir números del 2 al 10, saltando de 2 en 2
for i in range(2, 11, 2):
    print(f"Par: {i}")



contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar el contador



palabra = "Python"

for letra in palabra:
    print(f"Letra: {letra}")



for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")



for numero in range(10):
    if numero == 5:
        print("¡Encontré el número 5!")
        break
    print(f"Número: {numero}")



for numero in range(5):
    if numero == 2:
        print("Saltando el número 2")
        continue
    print(f"Número: {numero}")




contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador == 5:
        break  # Salir del bucle cuando el contador alcance 5







frutas = ["manzana", "plátano", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")



precios = {"manzana": 0.5, "plátano": 0.3, "cereza": 0.8}

for fruta, precio in precios.items():
    print(f"La {fruta} cuesta ${precio}")



# El bloque `else` se ejecuta solo si el bucle termina sin un `break`
for numero in range(5):
    if numero == 7:
        print("Encontré el número 7")
        break
else:
    print("El número 7 no fue encontrado.")




numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero

print(f"La suma total es: {suma}")



while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("¡Adiós!")
        break
    else:
        print(f"Escribiste: {entrada}")



numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




numero = 5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



# 

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
contador = {}

for numero in numeros:
    contador[numero] = contador.get(numero, 0) + 1

print("Ocurrencias:", contador)
