import pandas as pd

# Crear una Serie
serie = pd.Series([1, 2, 3, 4, 5])
print(serie)
# Crear un DataFrame
datos = {"Nombre": ["Ana", "Juan", "Pedro"], "Edad": [25, 30, 35]}
df = pd.DataFrame(datos)
print(df)