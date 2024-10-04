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
cotxes_df = pd.read_csv('cotxes.csv')
print("DataFrame a partir d'un fitxer CSV")
print(cotxes_df)
print()

# Guardar un DataFrame en un fitxer CSV
persones_df = pd.DataFrame({
    'nom': ['Aina', 'Mar', 'Pere'],
    'edat': [25, 30, 35],
    'ciutat': ['València', 'Mislata', 'Alboraia']
})
persones_df.to_csv('persones.csv', index=False)

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

