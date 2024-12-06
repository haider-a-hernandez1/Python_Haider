# import matplotlib.pyplot as plt

# # Crear un gráfico simple
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Gráfico de ejemplo")
# plt.show()




import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 10]

# Crear gráfico de barras
plt.bar(categorias, valores, color="skyblue")
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()