#!/usr/bin/env python

import pandas as pd

# Crear una Series amb una llista
a = [1, 3, 5, 7, 9]
s = pd.Series(a)
print("Series amb una llista")
print(s)
print()

# Crear una Series amb un diccionari
d = {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9}
s = pd.Series(d)
print("Series amb un diccionari")
print(s)
print()

# Crear una Series amb un valor escalar
s = pd.Series(5, index=[0, 1, 2, 3, 4])
print("Series amb un valor escalar")
print(s)
print()

# Crear un DataFrame amb una llista
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(a)
print("DataFrame amb una llista")
print(df)
print()

# Crear un Dataframe amb una llista, indicant els noms de les columnes
df = pd.DataFrame(a, columns=['A', 'B', 'C'])
print("DataFrame amb una llista i noms de columnes")
print(df)
print()

# Crear un DataFrame amb un diccionari
d = {'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]}
df = pd.DataFrame(d)
print("DataFrame amb un diccionari")
print(df)
print()

# Crear un DataFrame a partir d'un fitxer CSV
cotxes_df = pd.read_csv('../../files/ud3/cotxes.csv')
print("DataFrame a partir d'un fitxer CSV")
print(cotxes_df)
print()

# Guardar un DataFrame en un fitxer CSV
persones_df = pd.DataFrame({
    'nom': ['Aina', 'Mar', 'Pere'],
    'edat': [25, 30, 35],
    'ciutat': ['València', 'Mislata', 'Alboraia']
})
persones_df.to_csv('../../files/ud3/persones.csv', index=False)

# Mostrar informació bàsica del DataFrame cotxes_df
print("Informació bàsica del DataFrame cotxes_df")
cotxes_df.info()
print()

# Mostrar les primeres files del DataFrame cotxes_df
print("Primeres files del DataFrame cotxes_df")
print(cotxes_df.head())
print()

# Mostrar les últimes files del DataFrame cotxes_df
print("Últimes files del DataFrame cotxes_df")
print(cotxes_df.tail())
print()

# Accedir a la columna 'marca' del DataFrame cotxes_df
print("Columna 'marca' del DataFrame cotxes_df")
print("Amb []")
print(cotxes_df['marca'].head(2))
print("Com atribut")
print(cotxes_df.marca.head(2))
print()

# Accedir a les columnes 'marca' i 'km' del DataFrame cotxes_df
print("Columnes 'marca' i 'km' del DataFrame cotxes_df")
print(cotxes_df[['marca', 'km']].head(2))
print()

# Accedir a la fila amb índex 0 del DataFrame cotxes_df
print("Fila amb índex 0 del DataFrame cotxes_df")
print(cotxes_df.loc[0])
print()

# Accedir a les files amb índex 0 i 2 del DataFrame cotxes_df
print("Files amb índex 0 i 2 del DataFrame cotxes_df")
print(cotxes_df.loc[[0, 2]])
print()

# Accedir a les files amb índex 0 i 2 i a les columnes 'marca' i 'km' del DataFrame cotxes_df
print("Files amb índex 0 fins 2 i columnes 'marca' i 'km' del DataFrame cotxes_df")
print(cotxes_df.loc[0:2, ['marca', 'km']])
print()

# Filtrar els cotxes amb 'km' major que 70000
print("Cotxes amb més de 100000 km")
print(cotxes_df.loc[cotxes_df['km'] > 70000])
print()

# Filtrar els cotxes de la marca 'Ford' amb 'km' menor que 50000
print("Cotxes de la marca 'Ford' amb menys de 50000 km")
print(cotxes_df.loc[(cotxes_df['marca'] == 'Ford') & (cotxes_df['km'] < 50000)])
print()

# Agrupar les dades per la columna 'marca' i calcular la mitjana dels 'km'
mean = cotxes_df.groupby('marca')['km'].mean().sort_values(ascending=False)
print("Mitjana dels km per marca")
print(mean)
print()
