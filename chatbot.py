# # Función para mostrar el saludo inicial
# def saludo():
#     print("¡Hola! Soy tu chatbot. ¿En qué puedo ayudarte hoy?")
#     print("Escribe 'salir' para terminar la conversación.")

# # Función para procesar la entrada del usuario
# def procesar_entrada(entrada):
#     if 'hola' in entrada or 'buenas' in entrada:
#         return "¡Hola! ¿Cómo estás?"
#     elif 'adiós' in entrada or 'salir' in entrada:
#         return "Adiós. ¡Hasta luego!"
#     elif 'nombre' in entrada:
#         return "Soy un chatbot creado por Python."
#     elif 'como estas' in entrada:
#         return "Estoy bien, gracias por preguntar. ¿Y tú?"
#     elif 'tiempo' in entrada:
#         return "Lo siento, no puedo proporcionar información sobre el clima, pero puedes consultar en línea."
#     else:
#         return "Lo siento, no entendí eso. ¿Puedes reformular tu pregunta?"

# # Función principal que ejecuta el chatbot
# def iniciar_chat():
#     saludo()
#     while True:
#         entrada_usuario = input("Tú: ").lower()  # Recibe la entrada del usuario
#         respuesta = procesar_entrada(entrada_usuario)
#         print(f"Chatbot: {respuesta}")
        
#         # Si el usuario escribe "salir", termina la conversación
#         if entrada_usuario == "salir":
#             break

# # Ejecutar el chatbot
# iniciar_chat()


# Función para mostrar el saludo inicial



def saludo():
    print("¡Hola! Soy tu chatbot. ¿En qué puedo ayudarte hoy?")
    print("Puedes preguntarme cosas como la suma de dos números, tu edad, o incluso el clima. Escribe 'salir' para terminar la conversación.")

# Función para procesar la entrada del usuario
def procesar_entrada(entrada):
    entrada = entrada.lower()  # Convertir la entrada a minúsculas para evitar problemas con mayúsculas

    # Respuestas básicas a palabras clave
    if 'hola' in entrada or 'buenas' in entrada:
        return "¡Hola! ¿Cómo estás?"
    elif 'adios' in entrada or 'salir' in entrada:
        return "Adiós. ¡Hasta luego!"
    elif 'nombre' in entrada:
        return "Soy un chatbot creado por Python. Mi creador me ha diseñado para ayudarte con preguntas básicas."
    elif 'como estas' in entrada:
        return "Estoy bien, gracias por preguntar. ¿Y tú?"
    elif 'edad' in entrada:
        return "¡No tengo edad, soy un chatbot! Pero ¿cuál es tu edad?"
    
    # Procesar preguntas con números (por ejemplo, sumas)
    elif 'suma' in entrada or 'sumar' in entrada:
        return sumar_numeros(entrada)
    
    # Procesar números en general
    elif 'numero' in entrada or 'cuál' in entrada:
        return "Soy capaz de realizar cálculos. Por ejemplo, puedes decirme dos números para sumar."
    
    else:
        return "Lo siento, no entendí eso. ¿Puedes reformular tu pregunta?"

# Función para realizar la suma de dos números
def sumar_numeros(entrada):
    try:
        # Buscar números en la entrada del usuario
        partes = entrada.split()
        num1 = int(partes[-3])  # El primer número debe estar antes de la palabra 'sumar' o 'suma'
        num2 = int(partes[-1])  # El segundo número debe estar después de la palabra 'sumar' o 'suma'
        suma = num1 + num2
        return f"La suma de {num1} y {num2} es {suma}."
    except (IndexError, ValueError):
        return "Lo siento, no pude entender los números. Asegúrate de escribir dos números para sumar, por ejemplo: 'sumar 5 y 7'."

# Función principal que ejecuta el chatbot
def iniciar_chat():
    saludo()
    while True:
        entrada_usuario = input("Tu: ").lower()  # Recibe la entrada del usuario
        respuesta = procesar_entrada(entrada_usuario)
        print(f"Chatbot: {respuesta}")
        
        # Si el usuario escribe "salir", termina la conversación
        if entrada_usuario == "salir":
            break

# Ejecutar el chatbot
iniciar_chat()
