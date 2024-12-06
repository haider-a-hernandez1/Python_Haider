# ejemplo 1

# import matplotlib.pyplot as plt

# # Crear un gráfico simple
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Gráfico de ejemplo")
# plt.show()




#ejemplo 2 Grafico de barras

# import matplotlib.pyplot as plt

# # Datos de ejemplo
# categorias = ["A", "B", "C", "D"]
# valores = [10, 15, 7, 10]

# # Crear gráfico de barras
# plt.bar(categorias, valores, color="skyblue")
# plt.title("Gráfico de Barras")
# plt.xlabel("Categorías")
# plt.ylabel("Valores")
# plt.show()






# ejemplo 3 Grafico de lineas

# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Crear gráfico de líneas
# plt.plot(x, y, marker="o", color="green", linestyle="--")
# plt.title("Gráfico de Líneas")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.show()



# ejemplo 4 Grafico de dispersion

# import matplotlib.pyplot as plt

# # Datos de ejemplo
# x = [5, 7, 8, 7, 2, 17, 2, 9]
# y = [99, 86, 87, 88, 100, 86, 103, 87]

# # Crear gráfico de dispersión
# plt.scatter(x, y, color="purple")
# plt.title("Gráfico de Dispersión")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.show()



# ejemplo 5 Histograma


# import matplotlib.pyplot as plt

# # Datos de ejemplo
# datos = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# # Crear histograma
# plt.hist(datos, bins=5, color="orange", edgecolor="black")
# plt.title("Histograma")
# plt.xlabel("Valores")
# plt.ylabel("Frecuencia")
# plt.show()



# ejemplo 6 mapas de calor

# import matplotlib.pyplot as plt
# import numpy as np

# # Datos de ejemplo
# datos = np.random.rand(10, 10)

# # Crear mapa de calor
# plt.imshow(datos, cmap="viridis", interpolation="nearest")
# plt.title("Mapa de Calor")
# plt.colorbar()
# plt.show()




# ejemplo 7 Grafico circular


# import matplotlib.pyplot as plt

# # Datos de ejemplo
# categorias = ["Categoría A", "Categoría B", "Categoría C"]
# tamaños = [40, 35, 25]

# # Crear gráfico circular
# plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
# plt.title("Gráfico Circular")
# plt.show()


# ejemplo 8 Grafico de poblacion durante los ultomos 20 años


import matplotlib.pyplot as plt

# Datos de población de 8 países (en millones, por ejemplo)
paises = ["China", "India", "Estados Unidos", "Indonesia", "Pakistán", "Brasil", "Nigeria", "Bangladesh"]
poblacion = [1444, 1406, 331, 276, 240, 216, 223, 173]  # Población aproximada en millones

# Crear el gráfico circular
plt.figure(figsize=(8, 8))  # Ajustar el tamaño del gráfico
plt.pie(
    poblacion,
    labels=paises,
    autopct="%1.1f%%",  # Mostrar porcentajes
    startangle=140,  # Ángulo de inicio
    colors=plt.cm.tab10.colors,  # Usar una paleta de colores diferente
    wedgeprops={'edgecolor': 'black'}  # Bordes para mayor visibilidad
)

# Agregar título
plt.title("Comparación de población entre 8 países (2023)", fontsize=14)
plt.show()

