---
template: document.html
title: Manipulació de dades amb Pandas
icon: material/book-open-variant
comments: true
tags:
    - python
    - pandas
---


## Introducció a Pandas
[__`pandas`__](https://pandas.pydata.org/) és una llibreria de Python que proporciona
estructures de dades (`Series` i `DataFrame`) i eines per a l'anàlisi de dades.

Existeixen altres llibreries que proporcionen ferramentes semblars, com [`numpy`](https://numpy.org/),
però en aquest cas, els seus casos d'ús son diferents.

## Documentació i recursos addicionals
- [Documentació oficial de Pandas](https://pandas.pydata.org/docs/){:target="_blank"}
- [Llibre "pandas: powerful Python data analysis toolkit"][llibre-git]{:target="_blank"}
- [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python](https://www.hackerearth.com/practice/machine-learning/data-manipulation-visualisation-r-python/tutorial-data-manipulation-numpy-pandas-python/tutorial/){:target="_blank"}
- [12 Amazing Pandas & NumPy Functions](https://towardsdatascience.com/12-amazing-pandas-numpy-functions-22e5671a45b8?gi=443f0701b52d){:target="_blank"}
- [Cleaning Your Data Using Pandas](https://medium.com/geekculture/cleaning-your-data-using-pandas-ffbe21ccea81){:target="_blank"}
- [Pandas Data Wrangling Cheat Sheet 2021](https://towardsdatascience.com/pandas-data-wrangling-cheat-sheet-2021-cf70f577bcdd){:target="_blank"}
- [Análisis Exploratorio de Datos (EDA) con pandas_profiling](https://medium.com/tacosdedatos/an%C3%A1lisis-exploratorio-de-datos-eda-con-pandas-profiling-cf6c19caa8aa){:target="_blank"}
- [Error-free import of CSV files using Pandas DataFrame](https://towardsdatascience.com/how-to-import-csv-files-using-pandas-dataframe-error-free-62da3c31393c){:target="_blank"}
- [10 Tricks for Converting Numbers and Strings to Datetime in Pandas](https://towardsdatascience.com/10-tricks-for-converting-numbers-and-strings-to-datetime-in-pandas-82a4645fc23d){:target="_blank"}
- [Be a more efficient data analyst, a comprehensive guide to pandas](https://manojsaini18.medium.com/be-a-more-efficient-data-analyst-a-comprehensive-guide-to-pandas-63ea057bf828){:target="_blank"}
- [Differences Between concat(), merge() and join() with Python](https://pub.towardsai.net/differences-between-concat-merge-and-join-with-python-1a6541abc08d){:target="_blank"}
- [Simple ways to manipulate datetime variables with pandas](https://towardsdatascience.com/simple-ways-to-manipulate-datetime-variables-with-pandas-cfe9e8d36d24){:target="_blank"}

## Instal·lació
Pots instal·lar la llibreria `pandas` amb `pip`:

```bash
pip install pandas
```

## Importació
Per utilitzar `pandas`, cal importar la llibreria abans:

```python
import pandas as pd# (1)!
```

1. `pd` és un alias que es fa servir com a prefix per a accedir a les funcions de `pandas`.

## Estructura de dades
`pandas` proporciona dues estructures de dades principals:

- `Series`: és un array unidimensional etiquetat.
- `DataFrame`: és una estructura de dades bidimensional etiquetada amb columnes de tipus diferents.

### `Series`
`Series` és un array unidimensional etiquetat, que pot contindre
dades de qualsevol tipus (números, cadenes de caràcters, objectes, etc.).
Les etiquetes son referenciades com a `index`.

La sintaxi bàsica per a crear una `Series` és la següent:

```python
s = pd.Series(data, index=index)
```

- `data`: Dades de la `Series`, que pot ser una llista, un diccionari, un array de `numpy`, un valor escalar, etc.
- `index`: Etiquetes de la `Series`. La mida de `index` ha de coincidir amb la mida de `data`.

!!! info
    Si no s'especifica `index`, es crea un índex numèric de 0 a `len(data) - 1`.

!!! docs
    Capítol __"2.2.1 `Series`"__ del llibre [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python][llibre-git]{:target="_blank"}.

!!! example
    ```python
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
    ```
    /// html | div.result
    ```text
    Series amb una llista
    0    1
    1    3
    2    5
    3    7
    4    9
    dtype: int64

    Series amb un diccionari
    a    1
    b    3
    c    5
    d    7
    e    9
    dtype: int64

    Series amb un valor escalar
    0    5
    1    5
    2    5
    3    5
    4    5
    dtype: int64
    ```
    ///

### `DataFrame`
`DataFrame` és una estructura de dades bidimensional (2D) etiquetada
amb columnes de tipus diferents. Pot considerar-se com una taula de base de dades SQL
o un full de càlcul.

La sintaxi bàsica per a crear un `DataFrame` és la següent:

```python
df = pd.DataFrame(data, index=index, columns=columns)
```

- `data`: Dades del `DataFrame`, que poden ser:

    - Un diccionari de llistes, arrays de `numpy`, `Series`, etc.
    - Un array bidimensional de `numpy`.
    - Un altre `DataFrame`.

- `index`: Etiquetes de les __files__ del `DataFrame`. La mida de `index` ha de coincidir amb el nombre de files de `data`.

- `columns`: Etiquetes de les __columnes__ del `DataFrame`. La mida de `columns` ha de coincidir amb el nombre de columnes de `data`.

!!! info
    Si no s'especifica `index` o `columns`, es creen índexs numèrics de a partir de 0.

!!! docs
    Capítol __"2.2.2 `DataFrame`"__ del llibre [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python][llibre-git]{:target="_blank"}.

!!! example
    ```python
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
    ```
    /// html | div.result
    ```text
    DataFrame amb una llista
       0  1  2
    0  1  2  3
    1  4  5  6
    2  7  8  9

    DataFrame amb una llista i noms de columnes
       A  B  C
    0  1  2  3
    1  4  5  6
    2  7  8  9

    DataFrame amb un diccionari
       A  B  C
    0  1  2  3
    1  4  5  6
    2  7  8  9
    ```
    ///


[llibre-git]: https://pandas.pydata.org/pandas-docs/version/1.4.4/pandas.pdf
