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
    Capítol __"2.2.1 `Series`"__ del llibre [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python][llibre-pandas]{:target="_blank"}.

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
    Capítol __"2.2.2 `DataFrame`"__ del llibre [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python][llibre-pandas]{:target="_blank"}.

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

## Operacions de lectura i escriptura
`pandas` permet llegir i escriure dades de diferents formats,
com ara CSV o JSON.

!!! docs
    Capítol __"2.4. IO Tools"__ del llibre [Practical Tutorial on Data Manipulation with Numpy and Pandas in Python][llibre-pandas]{:target="_blank"}.

### Carregar dades
Per carregar dades, es fa servir la funció `read_<tipus>()`,
on `<tipus>` pot ser `csv`, `json` o altres.

En el cas de carregar dades d'un fitxer CSV, es fa servir la funció
[`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html){:target="_blank"}.

!!! example "Carregar dades d'un fitxer CSV"

    ```python
    # Crear un DataFrame a partir d'un fitxer CSV
    cotxes_df = pd.read_csv('../../files/ud3/cotxes.csv')
    print("DataFrame a partir d'un fitxer CSV")
    print(cotxes_df)
    ```
    /// html | div.result
    ```text
    DataFrame a partir d'un fitxer CSV
             marca     km data_matriculacio
    0         Ford  39031        08/12/2000
    1         Seat  10542        02/01/2001
    2   Volkswagen   8065        02/04/2001
    ...
    56        Fiat  18358        06/11/2002
    57     Porsche  19791        02/01/2012
    58      Nissan  18722        02/04/2001
    59    Mercedes  48813        10/03/2005
    ```
    ///

### Guardar dades
Per guardar dades, es fa servir la funció `to_<tipus>()`,
on `<tipus>` pot ser `csv`, `json` o altres.

En el cas de guardar dades en un fitxer CSV, es fa servir la funció
[`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html){:target="_blank"}.

!!! example "Guardar dades en un fitxer CSV"
    !!! info
        `index=False` evita que s'afegisca
        una columna amb l'índex de les files (0, 1, 2, ...).

    ```python
    # Guardar un DataFrame en un fitxer CSV
    df = pd.DataFrame({
        'nom': ['Aina', 'Mar', 'Pere'],
        'edat': [25, 30, 35],
        'ciutat': ['València', 'Mislata', 'Alboraia']
    })
    df.to_csv('../../files/ud3/persones.csv', index=False)
    ```
    /// html | div.result
    ```shellconsole
    jpuigcerver@fp:~/pandas $ cat persones.csv
    nom,edat,ciutat
    Aina,25,València
    Mar,30,Mislata
    Pere,35,Alboraia
    ```
    ///

## Informació de les dades
`pandas` proporciona diverses funcions per a obtindre
informació de les dades.

El mètode [`df.info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html){:target="_blank"}
mostra informació bàsica del `DataFrame`,
com ara el nombre de files, columnes, tipus de dades, etc.

!!! example
    ```python
    # Mostrar informació bàsica del DataFrame cotxes_df
    print("Informació bàsica del DataFrame cotxes_df")
    cotxes_df.info()
    ```
    /// html | div.result
    ```text
    Informació bàsica del DataFrame cotxes_df
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 60 entries, 0 to 59
    Data columns (total 3 columns):
     #   Column             Non-Null Count  Dtype 
    ---  ------             --------------  ----- 
     0   marca              60 non-null     object
     1   km                 60 non-null     int64 
     2   data_matriculacio  60 non-null     object
    dtypes: int64(1), object(2)
    memory usage: 1.5+ KB
    ```
    ///

El mètode [`df.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html){:target="_blank"}
les primeres files del `DataFrame`.

- El paràmetre `n` indica el nombre de files a mostrar,
    que per defecte és 5.

!!! example
    ```python
    # Mostrar les primeres files del DataFrame cotxes_df
    print("Primeres files del DataFrame cotxes_df")
    print(cotxes_df.head())
    ```
    /// html | div.result
    ```text
    Primeres files del DataFrame cotxes_df
    Primeres files del DataFrame cotxes_df
        marca     km data_matriculacio
    0        Ford  39031        08/12/2000
    1        Seat  10542        02/01/2001
    2  Volkswagen   8065        02/04/2001
    3     Peugeot  48623        28/11/2001
    4        Audi  57737        05/12/2001
    ```
    ///

El mètode [`df.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html){:target="_blank"}
les últimes files del `DataFrame`.

- El paràmetre `n` indica el nombre de files a mostrar,
    que per defecte és 5.

!!! example
    ```python
    # Mostrar les últimes files del DataFrame cotxes_df
    print("Últimes files del DataFrame cotxes_df")
    print(cotxes_df.tail())
    ```
    /// html | div.result
    ```text
    Últimes files del DataFrame cotxes_df
           marca     km data_matriculacio
    55      Seat  15734        15/07/2015
    56      Fiat  18358        06/11/2002
    57   Porsche  19791        02/01/2012
    58    Nissan  18722        02/04/2001
    59  Mercedes  48813        10/03/2005
    ```
    ///

## Accés a les dades
### Accés a les columnes
Es pot accedir a les dades d'una columna del `DataFrame` de dues maneres:

- Amb l'operador `[]`.
- Com un atribut de l'objecte `DataFrame`.

En cas que s'accedisca a una sola columna, el resultat és una `Series`.
    
!!! example
    ```python
    # Accedir a la columna 'marca' del DataFrame cotxes_df
    print("Columna 'marca' del DataFrame cotxes_df")
    print("Amb []")
    print(cotxes_df['marca'].head(2))
    print("Com atribut")
    print(cotxes_df.marca.head(2))
    print()
    ```
    /// html | div.result
    ```text
    Columna 'marca' del DataFrame cotxes_df
    Amb []
    0    Ford
    1    Seat
    Name: marca, dtype: object
    Com atribut
    0    Ford
    1    Seat
    Name: marca, dtype: object
    ```
    ///

També es pot accedir a més d'una columna del `DataFrame` utilitzant l'operador `[]`,
indicant la llista de les etiquetes.

!!! example
    ```python
    # Accedir a les columnes 'marca' i 'km' del DataFrame cotxes_df
    print("Columnes 'marca' i 'km' del DataFrame cotxes_df")
    print(cotxes_df[['marca', 'km']].head(2))
    ```
    /// html | div.result
    ```text
    Columnes 'marca' i 'km' del DataFrame cotxes_df
      marca     km
    0  Ford  39031
    1  Seat  10542
    ```
    ///

### Accés a les files per índex
Es pot accedir a les dades d'una fila del `DataFrame` amb la funció
[`df.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html){:target="_blank"}.

El primer paràmetre de la funció `loc` és l'índex de la fila (no necessàriament numèric) o una condició.

- `df.loc[n]`: Accedeix a la fila amb índex `n`.
- `df.loc[[n1, n2, ...]]`: Accedeix a les files amb índexs `n1`, `n2`, ...
- `df.loc[n:m]`: Accedeix a les files amb índexs de `n` a `m`.
- `df.loc[condicio]`: Accedeix a les files que compleixen la condició.

El segon paràmetre de la funció `loc` és l'etiqueta de la columna que volem obtindre.

- `df.loc[param1, 'columna']`: Accedeix a la columna `columna` de la fila especificada.
- `df.loc[param1, ['columna1', 'columna2']]`: Accedeix a les columnes `columna1` i `columna2` de la fila especificada.

!!! example
    ```python
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
    ```
    /// html | div.result
    ```text
    Fila amb índex 0 del DataFrame cotxes_df
    marca                      Ford
    km                        39031
    data_matriculacio    08/12/2000
    Name: 0, dtype: object

    Files amb índex 0 i 2 del DataFrame cotxes_df
            marca     km data_matriculacio
    0        Ford  39031        08/12/2000
    2  Volkswagen   8065        02/04/2001

    Files amb índex 0 fins 2 i columnes 'marca' i 'km' del DataFrame cotxes_df
            marca     km
    0        Ford  39031
    1        Seat  10542
    2  Volkswagen   8065
    ```
    ///

### Accés a les files per posició
Es pot accedir a les dades d'una fila del `DataFrame` mitjançant la seua posició amb la funció
[`df.iloc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html){:target="_blank"}.

El funcionament és pràcticament igual que amb `loc`, però en aquest cas s'utilitza la posició numèrica de la fila
en compte de l'índex (que pot ser numèric o no).

### Accés condicional
Es pot accedir a les dades del `DataFrame` utilitzant condicions lògiques,
que permet filtrar les dades.

Utilitem l'operador `[]` amb una condició per a filtrar les dades.

!!! example
    ```python
    # Filtrar els cotxes amb 'km' major que 70000
    print("Cotxes amb més de 100000 km")
    print(cotxes_df.loc[cotxes_df['km'] > 70000])
    print()

    # Filtrar els cotxes de la marca 'Ford' amb 'km' menor que 50000
    print("Cotxes de la marca 'Ford' amb menys de 50000 km")
    print(cotxes_df.loc[(cotxes_df['marca'] == 'Ford') & (cotxes_df['km'] < 50000)])
    print()
    ```
    /// html | div.result
    ```text
    Cotxes amb més de 100000 km
               marca     km data_matriculacio
    26  Mercedes  72868        04/06/2001
    50      Audi  70279        19/01/2001

    Cotxes de la marca 'Ford' amb menys de 50000 km
      marca     km data_matriculacio
    0  Ford  39031        08/12/2000
    ```
    ///

## Modificació de les dades
`pandas` permet diferents operacions per a modificar les dades d'un `DataFrame`.

### Modificar una columna
Es pot modificar una columna del `DataFrame` amb l'operador `[]`.

```python
# Assignar un valor constant a tota la columna
df['nom_columna'] = 10

# Aplicar una operació a la columna
df['nom_columna'] = df['nom_columna'] * 2
```

!!! important
    Si la columna especificada no existeix, es crea una columna nova.

### Eliminar una columna
Es pot eliminar una columna del `DataFrame` amb el mètode [`df.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html){:target="_blank"}.

```python
# Eliminar la columna 'nom_columna'
df.drop(columns=['nom_columna'], inplace=True)

# O utilitzant axis=1
df.drop('nom_columna', axis=1, inplace=True)
```

!!! info
    El paràmetre `inplace=True` fa que la modificació es realitze sobre el mateix `DataFrame`.

    En cas de especificar `inplace=False` (per defecte),
    el mètode `drop` retorna un nou `DataFrame` amb la modificació.

### Modificar una fila
Es pot modificar una fila del `DataFrame` amb el mètode [`df.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html){:target="_blank"}.

```python
# Modificar la fila amb índex 0
df.loc[0] = ['nou_valor', 100, '01/01/2022']
```

### Eliminar una fila

Es pot eliminar una fila del `DataFrame` amb el mètode [`df.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html){:target="_blank"}
utilitzant el paràmetre `axis=0` (per defecte).

```python
# Eliminar la fila amb índex 0
df.drop(0, axis=0, inplace=True)
```



### Modificar una cel·la
Es pot modificar una cel·la concreta del `DataFrame` amb el mètode [`df.loc[]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html){:target="_blank"},
utilitzant l'índex de la fila i el nom de la columna.

```python
# Modificar la cel·la de la fila amb índex 0 i la columna 'A'
df.loc[0, 'A'] = 'nou_valor'
```

### Afegir una fila
Es pot afegir una fila al `DataFrame` amb el mètode [`df.concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html){:target="_blank"}.

```python
files = pd.Series()
# o bé
files = pd.DataFrame()

# Afegir les files al final del DataFrame
df = pd.concat([df, files], axis=0)
```

!!! info
    També es poden afegir columnes amb `axis=1`.


## Funcions d'agregació
`pandas` incorpora diverses funcions d'agregació per a realitzar càlculs sobre les dades.

El mètode [`max()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html){:target="_blank"}
retorna el valor màxim de cada columna.

El mètode [`min()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html){:target="_blank"}
retorna el valor mínim de cada columna.

```python
# Valor mínim i màxim de cada columna
df.min()
df.max()

# Valor mínim i màxim d'una columna concreta
df['nom_columna'].min()
df['nom_columna'].max()
```

El mètode [`sum()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html){:target="_blank"}
retorna la suma de cada columna.

```python
# Suma de cada columna
df.sum()

# Suma d'una columna concreta
df['nom_columna'].sum()
```

El mètode [`mean()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html){:target="_blank"}
retorna la mitjana aritmètica de cada columna.

```python
# Mitjana de cada columna
df.mean()

# Mitjana d'una columna concreta
df['nom_columna'].mean()
```

## Agrupació de les dades
`pandas` permet agrupar les dades segons els valors d'una o més columnes, mitjançant el mètode
[`df.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html){:target="_blank"}.

Després, és possible aplicar [funcions d'agregació](#funcions-dagregació) per a obtindre
informació de les dades agrupades.

!!! example
    ```python
    # Agrupar les dades per la columna 'marca' i calcular la mitjana dels 'km'
    mean = cotxes_df.groupby('marca')['km'].mean()
    print("Mitjana dels km per marca")
    print(mean)
    ```
    /// html | div.result
    ```text
    Mitjana dels km per marca
    marca
    Alfa Romeo    45899.857143
    Audi          60097.333333
    BMW           35245.000000
    Ferrari       34201.000000
    Fiat          35642.333333
    Ford          39031.000000
    Kia           44016.500000
    Mercedes      49078.000000
    Nissan        21125.333333
    Peugeot       48423.125000
    Porsche       28426.400000
    Renault       51360.666667
    Seat          29210.666667
    Toyota        33753.000000
    Volkswagen    18710.333333
    Name: km, dtype: float64
    ```
    ///


## Dades nul·les o invàlides
`pandas` proporciona funcions per a tractar les dades nul·les o invàlides (com `NaN`).

El mètode [`isnull()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html){:target="_blank"}
retorna `True` si la dada és nul·la o invàlida.

```python
# Comprovar el nombre de dades nul·les per columna
df.isnull().sum()
```

El mètode [`dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html){:target="_blank"}
permet eliminar les files amb dades nul·les.

```python
# Eliminar les files amb dades nul·les
df.dropna(inplace=True)
```


## Codi font
- [cotxes.csv](../../files/ud3/cotxes.csv){: download="cotxes.csv"}
- [exemples_pandas.py](../../files/ud3/exemples_pandas.py){: download="exemples_pandas.py"}

    /// collapse-code
    ```python
    --8<-- "docs/files/ud3/exemples_pandas.py"
    ```
    ///

## Bibliografia i recursos addicionals
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
- [Documentació oficial de Pandas](https://pandas.pydata.org/docs/){:target="_blank"}
- [Llibre "pandas: powerful Python data analysis toolkit"][llibre-pandas]{:target="_blank"}
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


[llibre-pandas]: https://pandas.pydata.org/pandas-docs/version/1.4.4/pandas.pdf
