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


# import matplotlib.pyplot as plt

# # Datos de población de 8 países (en millones, por ejemplo)
# paises = ["China", "India", "Estados Unidos", "Indonesia", "Pakistán", "Brasil", "Nigeria", "Bangladesh"]
# poblacion = [1444, 1406, 331, 276, 240, 216, 223, 173]  # Población aproximada en millones

# # Crear el gráfico circular
# plt.figure(figsize=(8, 8))  # Ajustar el tamaño del gráfico
# plt.pie(
#     poblacion,
#     labels=paises,
#     autopct="%1.1f%%",  # Mostrar porcentajes
#     startangle=140,  # Ángulo de inicio
#     colors=plt.cm.tab10.colors,  # Usar una paleta de colores diferente
#     wedgeprops={'edgecolor': 'black'}  # Bordes para mayor visibilidad
# )

# # Agregar título
# plt.title("Comparación de población entre 8 países (2023)", fontsize=14)
# plt.show()




# ejemplo 9 


# import matplotlib.pyplot as plt

# # Datos de población por continentes (en millones)
# continentes = ["Asia", "África", "Europa", "América", "Oceanía", "Antártida"]
# poblacion_continentes = [4600, 1400, 750, 1000, 42, 6.01]  # Población estimada en millones

# # Crear el gráfico circular
# plt.figure(figsize=(8, 8))  # Ajustar el tamaño del gráfico
# plt.pie(
#     poblacion_continentes,
#     labels=continentes,
#     autopct="%1.1f%%",  # Mostrar porcentajes
#     startangle=140,  # Ángulo de inicio
#     colors=plt.cm.Paired.colors,  # Usar una paleta de colores diferente
#     wedgeprops={'edgecolor': 'black'}  # Bordes para mayor visibilidad
# )

# # Agregar título
# plt.title("Distribución de la población mundial por continentes (2023)", fontsize=14)
# plt.show()


# ejemplo 10


# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar el archivo CSV
# df = pd.read_csv('orders.csv')

# # Convertir las columnas de fecha a formato datetime
# df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
# df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors='coerce')

# # Crear nuevas columnas para mes, año y día
# df["dt_month"] = df["Order Date"].dt.month
# df["dt_year"] = df["Order Date"].dt.year
# df["dt_dia"] = df["Order Date"].dt.day

# # Mostrar las primeras filas del DataFrame para verificar que se cargó correctamente
# print(df.head())

# # Si deseas hacer un gráfico, por ejemplo, por cantidad de pedidos por mes:
# orders_per_month = df.groupby("dt_month").size()

# # Crear el gráfico
# plt.figure(figsize=(10, 6))
# orders_per_month.plot(kind='bar', color='skyblue')
# plt.title("Cantidad de Pedidos por Mes")
# plt.xlabel("Mes")
# plt.ylabel("Número de Pedidos")
# plt.xticks(rotation=0)
# plt.show()



# ejemplo 11   totalrevenue by year



# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar el archivo CSV
# df = pd.read_csv('orders.csv')

# # Convertir las fechas a datetime
# df["Order Date"] = pd.to_datetime(df["Order Date"])

# # Extraer el año de la fecha de la orden
# df["dt_year"] = df["Order Date"].dt.year

# # Agrupar por año y calcular el total de ventas por año (suma de 'Amount')
# df_sales_by_year = df.groupby('dt_year')['Amount'].sum()

# # Mostrar el DataFrame resultante
# print(df_sales_by_year)

# # Graficar el total de ventas por año
# plt.figure(figsize=(10, 6))
# df_sales_by_year.plot(kind='bar', color='skyblue')
# plt.title('Total Revenue by Year')
# plt.xlabel('Year')
# plt.ylabel('Total Revenue ($)')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



#comando para verficar las columnas del archivo:

# import pandas as pd

# # Cargar el archivo CSV
# df = pd.read_csv('orders.csv')

# # Ver las columnas del archivo CSV
# print(df.columns)







# 1)primer consulta hospital : consultas Género enero - junio 2024



import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos del año 2024 y meses de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) & 
                 (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Contar las consultas por género y mes
consultas_genero = data_2024.groupby(['MES DE LA CONSULTA', 'GENERO']).size().unstack()

# Ordenar los meses correctamente
meses_ordenados = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']
consultas_genero = consultas_genero.reindex(meses_ordenados)

# Crear el gráfico de barras
consultas_genero.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'pink'], edgecolor='black')

# Personalización del gráfico
plt.title('Consultas Realizadas (Enero - Junio 2024) por Género', fontsize=16)
plt.xlabel('Mes de la Consulta', fontsize=14)
plt.ylabel('Cantidad de Consultas', fontsize=14)
plt.legend(title='Género', labels=['Masculino', 'Femenino'])

# Etiquetas precisas sobre las barras
for i in range(len(consultas_genero)):
    if 'MASCULINO' in consultas_genero.columns:
        plt.text(i - 0.15, consultas_genero.iloc[i]['MASCULINO'] + 0.5, 
                 str(int(consultas_genero.iloc[i]['MASCULINO'])), 
                 fontsize=10, ha='center', color='blue')
    if 'FEMENINO' in consultas_genero.columns:
        plt.text(i + 0.15, consultas_genero.iloc[i]['FEMENINO'] + 0.5, 
                 str(int(consultas_genero.iloc[i]['FEMENINO'])), 
                 fontsize=10, ha='center', color='red')

# Ajustar el diseño
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#1.1 



import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos del año 2024 y meses de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) & 
                 (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Contar las consultas por género y mes
consultas_genero = data_2024.groupby(['MES DE LA CONSULTA', 'GENERO']).size().unstack()

# Ordenar los meses correctamente
meses_ordenados = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']
consultas_genero = consultas_genero.reindex(meses_ordenados)

# Crear el gráfico de barras
ax = consultas_genero.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'pink'], edgecolor='black')

# Personalización del gráfico
plt.title('Consultas Realizadas (Enero - Junio 2024) por Género', fontsize=16)
plt.xlabel('Mes de la Consulta', fontsize=14)
plt.ylabel('Cantidad de Consultas', fontsize=14)
plt.legend(title='Género', labels=['Masculino', 'Femenino'])

# Añadir los valores dentro de las barras
for i in range(len(consultas_genero)):
    if 'MASCULINO' in consultas_genero.columns:
        plt.text(i - 0.15, consultas_genero.iloc[i]['MASCULINO'] + 0.5, 
                 str(int(consultas_genero.iloc[i]['MASCULINO'])), 
                 fontsize=10, ha='center', color='blue', fontweight='bold')
    if 'FEMENINO' in consultas_genero.columns:
        plt.text(i + 0.15, consultas_genero.iloc[i]['FEMENINO'] + 0.5, 
                 str(int(consultas_genero.iloc[i]['FEMENINO'])), 
                 fontsize=10, ha='center', color='red', fontweight='bold')

# Ajustar el diseño para mejor visualización
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico
plt.show()




# 2) ciclo de vida y tipo de regimen


import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos del año 2024 y meses de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) &
                 (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Tabla de conteo cruzado: Ciclo de Vida vs Tipo de Régimen
cycle_vs_regimen = pd.crosstab(data_2024['CICLO DE VIDA'], data_2024['REGIMEN'])

# Crear el gráfico de barras apiladas
cycle_vs_regimen.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6), edgecolor='black')

# Personalización del gráfico
plt.title('Ciclo de Vida por Tipo de Régimen (Enero - Junio 2024)', fontsize=16)
plt.xlabel('Ciclo de Vida', fontsize=14)
plt.ylabel('Cantidad de Consultas', fontsize=14)
plt.legend(title='Régimen', title_fontsize=12, fontsize=10, loc='upper right')

# Etiquetas precisas sobre las barras
for i, bar_group in enumerate(cycle_vs_regimen.iterrows()):
    total_values = bar_group[1]
    cumulative_height = 0
    for value in total_values:
        if value > 0:  # Mostrar solo si hay valores
            plt.text(i, cumulative_height + value / 2, str(value),
                     ha='center', va='center', fontsize=9, color='white', fontweight='bold')
            cumulative_height += value

# Ajustar diseño
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 3) consultas por genero enero a junio 2024 (grafica lineas)

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Imprimir las columnas para verificar el nombre correcto
print("Nombres de las columnas:", data.columns)

# Asegurarse de que la columna tenga el nombre correcto
data.columns = data.columns.str.strip()  # Eliminar espacios en blanco

# Filtrar solo las consultas del año 2024
data_2024 = data[data['ANO DE LA CONSULTA'] == 2024]

# Filtrar solo los meses de enero a junio
months_first_half = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']
data_2024_first_half = data_2024[data_2024['MES DE LA CONSULTA'].isin(months_first_half)]

# Contar consultas por mes y género (masculino y femenino)
gender_month_count = pd.crosstab(data_2024_first_half['MES DE LA CONSULTA'], data_2024_first_half['GENERO'])

# Ordenar los meses según la lista definida
gender_month_count = gender_month_count.reindex(months_first_half, fill_value=0)

# Gráfico de líneas (latido de frecuencia cardíaca)
plt.figure(figsize=(10, 6))
plt.plot(gender_month_count.index, gender_month_count['MASCULINO'], label='Masculino', marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
plt.plot(gender_month_count.index, gender_month_count['FEMENINO'], label='Femenino', marker='o', color='pink', linestyle='-', linewidth=2, markersize=8)

# Personalización del gráfico
plt.title('Distribución de Consultas por Género (Enero a Junio 2024)', fontsize=16, fontweight='bold', color='#4B0082')
plt.xlabel('Mes', fontsize=14, fontweight='bold')
plt.ylabel('Cantidad de Consultas', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)  # Rotar nombres de los meses
plt.legend(title='Género', loc='upper left')

# Añadir una cuadrícula para mayor visibilidad
plt.grid(True, linestyle='--', alpha=0.7)

# Estilo general de fondo
plt.gca().set_facecolor('#F9F9F9')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar gráfico
plt.show()


# 4 consultas por edad y genero enero a junio 2024


import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Filtrar los datos solo para el año 2024 y de enero a junio
data_2024 = data[(data['ANO DE LA CONSULTA'] == 2024) & (data['MES DE LA CONSULTA'].isin(['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']))]

# Crear rangos de edad
bins = [0, 18, 30, 40, 50, 60, 100]
labels = ['Menor de 18', '18-30', '31-40', '41-50', '51-60', 'Mayor de 60']
data_2024['RANGO DE EDAD'] = pd.cut(data_2024['EDAD'], bins=bins, labels=labels)

# Contar consultas por rango de edad y género
age_gender_count = data_2024.groupby(['RANGO DE EDAD', 'GENERO']).size().unstack(fill_value=0)

# Gráfico de barras apiladas
ax = age_gender_count.plot(kind='bar', stacked=True, color=['skyblue', 'pink'])

# Añadir las cifras sobre las barras
for p in ax.patches:
    height = p.get_height()
    width = p.get_width()
    x, y = p.get_xy()  # obtiene las coordenadas del bloque de la barra
    ax.text(x + width / 2, y + height / 2, str(int(height)), 
            ha='center', va='center', color='black', fontsize=10)

# Títulos y etiquetas
plt.title('Consultas por Edad y Género (Enero a Junio 2024)')
plt.xlabel('Rango de Edad')
plt.ylabel('Cantidad de Consultas')
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()


#5).1 consultas por municipio


import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar consultas por municipio
municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# Crear gráfico de barras horizontales con más espacio entre las columnas
plt.figure(figsize=(10, 6))  # Aumentar el tamaño de la figura

# Asignar colores diferentes a cada barra usando una paleta de colores
colors = plt.cm.get_cmap('tab10', len(municipality_count))  # Usamos una paleta de 10 colores

# Gráfico de barras horizontales con colores diferentes
ax = municipality_count.plot(kind='barh', color=colors(range(len(municipality_count))))

# Títulos y etiquetas
plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)', fontsize=14)
plt.xlabel('Cantidad de Consultas', fontsize=12)
plt.ylabel('Municipio', fontsize=12)

# Añadir los valores exactos dentro de las barras
for i, v in enumerate(municipality_count):
    ax.text(v + 10, i, str(v), color='black', va='center', fontweight='bold')  # Ajusta el valor de '10' según sea necesario

# Ajustar el diseño para más espacio entre las barras y las etiquetas
plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)  # Ajustar márgenes

# Rotar las etiquetas del eje Y para mayor claridad si son largas
plt.yticks(rotation=0, fontsize=10)  # Puedes ajustar el tamaño de las etiquetas si es necesario

# Mostrar el gráfico
plt.show()



#5.2 

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar consultas por municipio
municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# Gráfico de líneas
ax = municipality_count.plot(kind='line', marker='o', color='orange', linestyle='-', linewidth=2)

# Títulos y etiquetas
plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)')
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Consultas')

# Añadir los valores exactos en cada punto de la curva
for i, v in enumerate(municipality_count):
    ax.text(i, v + 10, str(v), color='black', ha='center', fontweight='bold')  # Ajusta la posición del texto

# Mostrar el gráfico
plt.show()



# 5.3

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar consultas por municipio
municipality_count = data['MUNICIPIO'].value_counts().head(10)  # Mostrar los 10 municipios con más consultas

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfico de barras
municipality_count.plot(kind='bar', color='skyblue', ax=ax, width=0.7)

# Gráfico de línea (curva) sobre las barras
municipality_count.plot(kind='line', marker='o', color='orange', ax=ax, linewidth=2, linestyle='-', markerfacecolor='red')

# Añadir los valores exactos en las barras
for i, v in enumerate(municipality_count):
    ax.text(i, v + 10, str(v), color='black', ha='center', fontweight='bold')  # Ajustar la posición del texto

# Títulos y etiquetas
plt.title('Top 10 de Municipios con Más Consultas (Enero a Junio 2024)')
plt.xlabel('Municipio')
plt.ylabel('Cantidad de Consultas')

# Mostrar el gráfico
plt.show()


# 6 grafico de cantidad de consultas por tipo de consulta


import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar las consultas por tipo de consulta
type_of_consultation_count = data['TIPO DE CONSULTA'].value_counts()  # Contar las consultas por tipo de consulta

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfico de barras
type_of_consultation_count.plot(kind='bar', color='lightblue', ax=ax, width=0.7)

# Gráfico de línea sobre las barras
type_of_consultation_count.plot(kind='line', marker='o', color='orange', ax=ax, linewidth=2, linestyle='-', markerfacecolor='red')

# Añadir los valores exactos en las barras
for i, v in enumerate(type_of_consultation_count):
    ax.text(i, v + 5, str(v), color='black', ha='center', fontweight='bold')  # Ajustar la posición del texto

# Títulos y etiquetas
plt.title('Cantidad de Consultas por Tipo de Consulta')
plt.xlabel('Tipo de Consulta')
plt.ylabel('Cantidad de Consultas')

# Mostrar el gráfico
plt.show()



#6.2

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('hospital.csv')

# Contar las consultas por tipo de consulta
type_of_consultation_count = data['TIPO DE CONSULTA'].value_counts()  # Contar las consultas por tipo de consulta

# Crear la figura y el eje
fig, ax = plt.subplots()

# Gráfico de barras
type_of_consultation_count.plot(kind='bar', color='lightblue', ax=ax, width=0.7)

# Gráfico de línea sobre las barras
type_of_consultation_count.plot(kind='line', marker='o', color='orange', ax=ax, linewidth=2, linestyle='-', markerfacecolor='red')

# Añadir los valores exactos en las barras
for i, v in enumerate(type_of_consultation_count):
    ax.text(i, v + 5, str(v), color='black', ha='center', fontweight='bold')  # Ajustar la posición del texto

# Títulos y etiquetas
plt.title('Cantidad de Consultas por Tipo de Consulta')
plt.xlabel('Tipo de Consulta')
plt.ylabel('Cantidad de Consultas')

# Mostrar el gráfico
plt.show()


# 7 edad de 60 a 105 años

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos para personas entre 60 y 105 años
data_age_filtered = data[(data['EDAD'] >= 60) & (data['EDAD'] <= 105)]

# Contar personas por edad y género
age_gender_count = pd.crosstab(data_age_filtered['EDAD'], data_age_filtered['GENERO'])

# Crear el gráfico de barras apiladas
age_gender_count.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='coolwarm', edgecolor='black')

# Personalizar el gráfico
plt.title('Distribución de Personas por Edad (60-105 años) y Género', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Cantidad de Personas', fontsize=14)
plt.legend(title='Género', title_fontsize=12, fontsize=10)
plt.xticks(rotation=45)  # Gira las etiquetas del eje X para mayor claridad

# Etiquetas precisas sobre las barras
for i, age in enumerate(age_gender_count.index):
    cumulative_height = 0
    for gender in age_gender_count.columns:
        value = age_gender_count.loc[age, gender]
        if value > 0:  # Mostrar etiquetas solo si hay valores
            plt.text(i, cumulative_height + value / 2, str(value),
                     ha='center', va='center', fontsize=8, color='white', fontweight='bold')
            cumulative_height += value

# Ajustar diseño
plt.tight_layout()
plt.show()



#  7.1

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos para personas entre 60 y 105 años
data_age_filtered = data[(data['EDAD'] >= 60) & (data['EDAD'] <= 105)]

# Contar personas por edad y género
age_gender_count = pd.crosstab(data_age_filtered['EDAD'], data_age_filtered['GENERO'])

# Crear el gráfico de barras
ax = age_gender_count.plot(kind='bar', figsize=(12, 6), colormap='coolwarm', edgecolor='black')

# Personalizar el gráfico
plt.title('Distribución de Personas por Edad (60-105 años) y Género', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Cantidad de Personas', fontsize=14)
plt.legend(title='Género', title_fontsize=12, fontsize=10)
plt.xticks(rotation=45)  # Gira las etiquetas del eje X para mayor claridad

# Etiquetas precisas sobre las barras (mostrar el valor dentro de cada barra)
for i, age in enumerate(age_gender_count.index):
    # Para cada barra de la edad, obtener las barras de cada género
    cumulative_height = 0
    for gender in age_gender_count.columns:
        value = age_gender_count.loc[age, gender]
        if value > 0:  # Mostrar solo si hay valores
            # Calcular la posición de la etiqueta dentro de la barra
            ax.text(i, cumulative_height + value / 2, str(value),
                    ha='center', va='center', fontsize=10, color='white', fontweight='bold')
            cumulative_height += value

# Ajustar diseño
plt.tight_layout()
plt.show()

# sangre



import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('hospital.csv')

# Filtrar datos para personas entre 60 y 105 años
data_age_filtered = data[(data['EDAD'] >= 60) & (data['EDAD'] <= 105)]

# Contar personas por edad y género
age_gender_count = pd.crosstab(data_age_filtered['EDAD'], data_age_filtered['GENERO'])

# Crear un gráfico de barras apiladas
plt.figure(figsize=(14, 6))



# Segundo gráfico: Barras no apiladas
plt.subplot(1, 2, 2)
age_gender_count.plot(kind='bar', stacked=False, colormap='coolwarm', edgecolor='black', ax=plt.gca())
plt.title('Gráfico de Barras No Apiladas', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Cantidad de Personas', fontsize=14)
plt.xticks(rotation=45)

# Ajustar diseño
plt.tight_layout()

# Mostrar los gráficos
plt.show()



import matplotlib.gridspec as gridspec

plt.figure(figsize=(12, 6))
grid = gridspec.GridSpec(1, 3)  # Divide la figura en 3 columnas
ax = plt.subplot(grid[:, 1])   # Ocupa solo la columna central

age_gender_count.plot(kind='bar', stacked=False, colormap='coolwarm', edgecolor='black', ax=ax)
plt.title('Gráfico de Barras No Apiladas', fontsize=16)
plt.xlabel('Edad', fontsize=14)
plt.ylabel('Cantidad de Personas', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




