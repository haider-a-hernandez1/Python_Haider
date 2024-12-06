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





# import pandas as pd

# # Leer el archivo CSV
# df = pd.read_csv("poblacion.csv")

# # Primeras 5 filas del DataFrame
# print("Primeras 5 filas:")
# print(df.head())

# # Últimas 5 filas del DataFrame
# print("\nÚltimas 5 filas:")
# print(df.tail())

# # Información general sobre el DataFrame (tipo de datos, valores no nulos, etc.)
# print("\nInformación general:")
# print(df.info())

# # Estadísticas descriptivas sobre los datos numéricos (promedio, desviación estándar, etc.)
# print("\nEstadísticas descriptivas:")
# print(df.describe())









# import pandas as pd

# # Leer el archivo CSV
# df = pd.read_csv("poblacion.csv")

# # Selección de una columna (por ejemplo, 'Nombre')
# nombres = df["Nombre"]

# # Imprimir los primeros valores de la columna 'Nombre'
# print(nombres.head())


#  comando para consultar la poblacion de personas en cada año

import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('poblacion.csv')

# Verificar las primeras filas para asegurarte de que el archivo se cargó correctamente
print(df.head())

# Consultas de población de diferentes países en años específicos
# Cambia los países y años según sea necesario en tus consultas

# Población de USA en 1960
usa_1960 = df.loc[df['Date'] == 1960, 'USA'].values
if len(usa_1960) > 0:
    print(f'La población de USA en 1960 fue: {usa_1960[0]}')

# Población de Brasil en 1970
bra_1970 = df.loc[df['Date'] == 1970, 'BRA'].values
if len(bra_1970) > 0:
    print(f'La población de Brasil en 1970 fue: {bra_1970[0]}')

# Población de Argentina en 1980
arg_1980 = df.loc[df['Date'] == 1980, 'ARG'].values
if len(arg_1980) > 0:
    print(f'La población de Argentina en 1980 fue: {arg_1980[0]}')

# Población de China en 1990
chn_1990 = df.loc[df['Date'] == 1990, 'CHN'].values
if len(chn_1990) > 0:
    print(f'La población de China en 1990 fue: {chn_1990[0]}')

# Población de México en 2000
mex_2023 = df.loc[df['Date'] == 2023, 'MEX'].values
if len(mex_2023) > 0:
    print(f'La población de México en 2023 fue: {mex_2023[0]}')

# Población de India en 2010
ind_2020 = df.loc[df['Date'] == 2020, 'IND'].values
if len(ind_2020) > 0:
    print(f'La población de India en 2020 fue: {ind_2020[0]}')

# Población de Rusia en 2020
rus_2020 = df.loc[df['Date'] == 2020, 'RUS'].values
if len(rus_2020) > 0:
    print(f'La población de Rusia en 2020 fue: {rus_2020[0]}')

# Población de Alemania en 2023
ger_2023 = df.loc[df['Date'] == 2023, 'DEU'].values
if len(ger_2023) > 0:
    print(f'La población de Alemania en 2023 fue: {ger_2023[0]}')

# Población de Japón en 1999
jpn_1999 = df.loc[df['Date'] == 1999, 'JPN'].values
if len(jpn_1999) > 0:
    print(f'La población de Japón en 1999 fue: {jpn_1999[0]}')

# Población de Canadá en 2015
can_2015 = df.loc[df['Date'] == 2015, 'CAN'].values
if len(can_2015) > 0:
    print(f'La población de Canadá en 2015 fue: {can_2015[0]}')

# Población de Francia en 2022
fra_2022 = df.loc[df['Date'] == 2022, 'FRA'].values
if len(fra_2022) > 0:
    print(f'La población de Francia en 2022 fue: {fra_2022[0]}')

# Puedes agregar más países y años según necesites.



