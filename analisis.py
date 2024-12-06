# import pandas as pd

# # Leer el archivo CSV
# df = pd.read_csv("poblacion.csv")

# # Ver las primeras filas del archivo para asegurarte de que los datos se han cargado correctamente
# print(df.head())

# # Supongamos que quieres filtrar los datos (ejemplo: seleccionar solo las filas donde la población sea mayor a 100,000)
# df_filtrado = df[df['Poblacion'] > 100000]

# # Ver el DataFrame filtrado
# print(df_filtrado)

# # Escribir el DataFrame filtrado en un nuevo archivo CSV
# df_filtrado.to_csv("poblacion_filtrada.csv", index=False)





import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("poblacion.csv")

# Primeras 5 filas del DataFrame
print("Primeras 5 filas:")
print(df.head())

# Últimas 5 filas del DataFrame
print("\nÚltimas 5 filas:")
print(df.tail())

# Información general sobre el DataFrame (tipo de datos, valores no nulos, etc.)
print("\nInformación general:")
print(df.info())

# Estadísticas descriptivas sobre los datos numéricos (promedio, desviación estándar, etc.)
print("\nEstadísticas descriptivas:")
print(df.describe())









import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("poblacion.csv")

# Selección de una columna (por ejemplo, 'Nombre')
nombres = df["Nombre"]

# Imprimir los primeros valores de la columna 'Nombre'
print(nombres.head())
