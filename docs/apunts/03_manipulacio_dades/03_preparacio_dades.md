---
template: document.html
title: Preparació de les dades
icon: material/book-open-variant
alias: preparacio-dades
comments: true
---

## Preparació de les dades
Quan treballem en la resolució d'un problema d'aprenentatge automàtic,
el primer pas fonamental és conèixer les dades amb les quals treballarem
i preparar-les adequadament.

!!! warning
    Treballar amb dades sense cap preparació impedirà obtenir resultats
    satisfactoris en la majoria dels casos.

En aquesta secció, veurem com preparar les dades per poder-les utilitzar
en els models d'aprenentatge automàtic.

!!! prep "Conjunt de dades `adult-dataset`"
    En aquests apunts treballarem en el següent conjunt de dades
    [adult-dataset](https://www.kaggle.com/datasets/mlbysoham/adult-dataset){target=_blank}.

### Informació sobre les dades
El primer pas és conèixer les dades amb les quals treballarem.

Podem obtindre informació sobre les dades utilitzant diferents mètodes.

Els mètodes `head()`, `tail()`, `info()` vists a
[[pandas#informacio-de-les-dades]]{target=_blank})
ens permeten obtenir una visió general de les dades.

??? example "Exemple: `head()`, `tail()` i `info()`"
    
    ```python
    file_path = "../../files/ud3/adult.data"
    df = pd.read_csv(file_path, header=None)

    print("Head of the dataset:")
    print(df.head(), "\n")
    print("Tail of the dataset:")
    print(df.tail(), "\n")
    print("Info of the dataset:")
    df.info()
    print()
    ```

    /// html | div.result
    ```
    Head of the dataset:
       0                  1       2           3   4                    5                   6               7       8        9     10  11  12              13      14
    0  39          State-gov   77516   Bachelors  13        Never-married        Adm-clerical   Not-in-family   White     Male  2174   0  40   United-States   <=50K
    1  50   Self-emp-not-inc   83311   Bachelors  13   Married-civ-spouse     Exec-managerial         Husband   White     Male     0   0  13   United-States   <=50K
    2  38            Private  215646     HS-grad   9             Divorced   Handlers-cleaners   Not-in-family   White     Male     0   0  40   United-States   <=50K
    3  53            Private  234721        11th   7   Married-civ-spouse   Handlers-cleaners         Husband   Black     Male     0   0  40   United-States   <=50K
    4  28            Private  338409   Bachelors  13   Married-civ-spouse      Prof-specialty            Wife   Black   Female     0   0  40            Cuba   <=50K 

    Tail of the dataset:
           0              1       2            3   4                    5                   6           7       8        9      10  11  12              13      14
    32556  27        Private  257302   Assoc-acdm  12   Married-civ-spouse        Tech-support        Wife   White   Female      0   0  38   United-States   <=50K
    32557  40        Private  154374      HS-grad   9   Married-civ-spouse   Machine-op-inspct     Husband   White     Male      0   0  40   United-States    >50K
    32558  58        Private  151910      HS-grad   9              Widowed        Adm-clerical   Unmarried   White   Female      0   0  40   United-States   <=50K
    32559  22        Private  201490      HS-grad   9        Never-married        Adm-clerical   Own-child   White     Male      0   0  20   United-States   <=50K
    32560  52   Self-emp-inc  287927      HS-grad   9   Married-civ-spouse     Exec-managerial        Wife   White   Female  15024   0  40   United-States    >50K 

    Info of the dataset:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 32561 entries, 0 to 32560
    Data columns (total 15 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   0       32561 non-null  int64 
     1   1       32561 non-null  object
     2   2       32561 non-null  int64 
     3   3       32561 non-null  object
     4   4       32561 non-null  int64 
     5   5       32561 non-null  object
     6   6       32561 non-null  object
     7   7       32561 non-null  object
     8   8       32561 non-null  object
     9   9       32561 non-null  object
     10  10      32561 non-null  int64 
     11  11      32561 non-null  int64 
     12  12      32561 non-null  int64 
     13  13      32561 non-null  object
     14  14      32561 non-null  object
    dtypes: int64(6), object(9)
    memory usage: 3.7+ MB
    ```
    ///

A més, podem utilitzar els següents mètodes
per obtindre més informació:

- `shape`: proporciona el nombre de files i columnes del conjunt de dades.
- `describe()`: proporciona estadístiques descriptives del conjunt de dades com el nombre de valors no nuls,
    la mitjana, la desviació estàndard, el valor mínim, els quartils i el valor màxim.
- `unique()`: proporciona els valors únics d'una columna.
- `value_counts()`: proporciona el nombre de vegades que es repeteix cada valor d'una columna.

??? example "Exemple: `shape`, `describe()` i `unique()`"
    ```python
    print("Shape of the dataset:")
    print(df.shape, "\n")
    print("Description of the dataset:")
    print(df.describe(), "\n")
    print("Unique values of workclass column:")
    print(df['workclass'].unique(), "\n")
    print("Value counts of workclass column:")
    print(df['workclass'].value_counts(dropna=False), "\n")
    ```

    /// html | div.result
    ```
    Shape of the dataset:
    (32561, 15) 

    Description of the dataset:
                     0             2             4             10            11            12
    count  32561.000000  3.256100e+04  32561.000000  32561.000000  32561.000000  32561.000000
    mean      38.581647  1.897784e+05     10.080679   1077.648844     87.303830     40.437456
    std       13.640433  1.055500e+05      2.572720   7385.292085    402.960219     12.347429
    min       17.000000  1.228500e+04      1.000000      0.000000      0.000000      1.000000
    25%       28.000000  1.178270e+05      9.000000      0.000000      0.000000     40.000000
    50%       37.000000  1.783560e+05     10.000000      0.000000      0.000000     40.000000
    75%       48.000000  2.370510e+05     12.000000      0.000000      0.000000     45.000000
    max       90.000000  1.484705e+06     16.000000  99999.000000   4356.000000     99.000000 

    Unique values of workclass column:
    'State-gov' 'Self-emp-not-inc' 'Private' 'Federal-gov' 'Local-gov' '?'
     'Self-emp-inc' 'Without-pay' 'Never-worked']
     
    Value counts of workclass column:
    workclass
    Private             22696
    Self-emp-not-inc     2541
    Local-gov            2093
    NaN                  1836
    State-gov            1298
    Self-emp-inc         1116
    Federal-gov           960
    Without-pay            14
    Never-worked            7
    Name: count, dtype: int64
    ```
    ///


### Valors nuls
Un dels problemes més comuns en les dades són els valors nuls,
ja que la majoria de models no permeten treballar amb valors no numèrics.

Podem identificar els valors nuls amb el mètode `isnull()`.

??? example "Exemple: `isnull()`"
    !!! warning
        Hem modificat el conjunt de dades inicial per afegir un valor nul a la columna `age`.

    ```python
    df.loc[50, 'age'] = None # Assignem un valor nul a la columna 'age' de la fila 50

    print("Number of null values in each column:")
    print(df.isnull().sum(), "\n")
    ```
    /// html | div.result
    ```
    Number of null values in each column:
    age                  1
    workclass         1836
    fnlwgt               0
    education            0
    education-num        0
    marital-status       0
    occupation        1843
    relationship         0
    race                 0
    sex                  0
    capital-gain         0
    capital-loss         0
    hours-per-week       0
    native-country     583
    income               0
    dtype: int64 
    ```
    ///


En aquest cas, podem tractar-los de tres maneres diferents:

- Eliminar les files amb valors nuls.
- Eliminar la columna amb valors nuls.
- Inferir els valors nuls.

Depenent de la tipologia de les dades, una opció serà més adequada que una altra.

#### Eliminar les files amb valors nuls
En el cas que les files amb valors nuls no siguen significatives
dins del conjunt de dades, podem eliminar-les.

??? example "Exemple consulta fila amb `age` nul·la"
    ```python
    print(df[df['age'].isnull()])
    ```
    /// html | div.result
    ```
        age workclass  fnlwgt     education  education-num      marital-status       occupation relationship   race     sex  capital-gain  capital-loss  hours-per-week native-country income
    50  NaN   Private   32275  Some-college             10  Married-civ-spouse  Exec-managerial         Wife  Other  Female             0             0              40  United-States
    ```
    ///

El mètode `dropna()` ens permet eliminar les files amb valors nuls
d'un conjunt de dades.

```python
df = df.dropna(inplace=False, subset=None)
```

- `inplace`: si `True`, el conjunt de dades es modificarà directament.
- `subset`: llista de columnes on buscar valors nuls.

!!! docs
    Documentació de pandas sobre el mètode [`dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html){target=_blank}.

??? example "Exemple: Eliminar files amb `age` nul·la"
    ```python
    rows = df.shape[0]
    df.dropna(subset=['age'], inplace=True)
    print(f"Deleted {rows - df.shape[0]} rows with null values in 'age' column")
    ```
    /// html | div.result
    ```
    Deleted 1 rows with null values in 'age' column
    ```
    ///

#### Eliminar la columna amb valors nuls
En el cas que la columna amb valors nuls no siga significativa
dins del conjunt de dades, podem eliminar-la completament.

El mètode `drop()` ens permet eliminar una columna d'un conjunt de dades.

```python
df = df.drop(labels, inplace=False)
```

!!! docs
    Documentació de pandas sobre el mètode [`drop()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html){target=_blank}.

??? warning "Eliminació de la columna `workclass`"
    En aquest cas, haguérem pogut eliminar la columna `workclass` amb valors nuls.
    ```python
    df.drop(columns='workclass', inplace=True)
    ```

    No obstant això, aquests valors podrien ser significatius per a la predicció,
    i s'ha optat per no fer-ho.


## Dades categòriques
Els models d'aprenentatge automàtic no poden treballar directament
amb dades categòriques o amb text, per tant, és necessari processar-les
per poder-les utilitzar.

Per identificar les columnes amb dades categòriques, podem utilitzar
el mètode `dtypes` i filtrar les columnes amb el tipus `object`.

??? example "Exemple: Identificar columnes categòriques"
    ```python
    print("Categorical columns:")
    print(df.select_dtypes(include='object').columns)
    ```
    /// html | div.result
    ```
    Categorical columns:
    Index(['workclass', 'education', 'marital-status', 'occupation',
           'relationship', 'race', 'sex', 'native-country', 'income'],
          dtype='object')
    ```
    ///

Per transformar les dades categòriques en dades numèriques,
podem utilitzar diferents mètodes com:

- __`OrdinalEncoder` i `LabelEncoder`: transformen les dades categòriques en valors numèrics__.

    La diferència principal és que `OrdinalEncoder` està pensat per transformar les característiques
    de les dades, mentre que `LabelEncoder` està pensat per transformar les etiquetes (`target`).

    Per aquesta raó, `OrdinalEncoder` permet transformar més d'una columna a la vegada i,
    en canvi, `LabelEncoder` només permet transformar una única columna.

    Aquest tipus de transformació és adequada quan les dades categòriques tenen un ordre implícit.

- __`OneHotEncoder`: transforma les dades categòriques en variables binàries.__

    Aquest mètode crea una columna per a cada valor únic de la columna original,
    assignant un valor de `1` si el valor és present i `0` si no ho és.

    Aquest tipus de transformació és adequada quan les dades categòriques no tenen un ordre implícit.


### `OrdinalEncoder`
El `OrdinalEncoder` transforma les dades categòriques en valors ordinals, és a dir,
assigna un valor numèric a cada categoria.

!!! info
    `OrdinalEncoder` no suporta valors nuls, per tant, és necessari tractar-los
    abans de fer la transformació.

??? example "Exemple: Transformació de `workclass` amb `OrdinalEncoder`"
    ```python
    # Assignem un valor '?' als valors nuls
    df.loc[df['workclass'].isnull(), 'workclass'] = '?'

    workclass_oe = OrdinalEncoder()
    df['workclass_oe'] = workclass_oe.fit_transform(df\[['workclass']])

    # print each unique value and its corresponding label
    print("Unique values of workclass column:")
    unique_pairs = df\[['workclass', 'workclass_oe']].drop_duplicates().sort_values('workclass_oe').reset_index(drop=True)
    print(unique_pairs, "\n")
    ```
    /// html | div.result
    ```plaintext
    Unique values of workclass column:
              workclass  workclass_oe
    0                 ?           0.0
    1       Federal-gov           1.0
    2         Local-gov           2.0
    3      Never-worked           3.0
    4           Private           4.0
    5      Self-emp-inc           5.0
    6  Self-emp-not-inc           6.0
    7         State-gov           7.0
    8       Without-pay           8.0 
    ```
    ///

### `OneHotEncoder`
El `OneHotEncoder` transforma les dades categòriques en múltiples columnes binàries,
que s'indica amb un `1` si el valor és d'aquella categoria i `0` si no ho és.

??? example "Exemple: Transformació de `sex` amb `OneHotEncoder`"
    ```python
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(df\[['sex']])
    encoded_columns = encoder.get_feature_names_out(['sex'])
    df_encoded = pd.DataFrame(encoded_data.toarray(), columns=encoded_columns)
    df = pd.concat([df, df_encoded], axis=1)

    print("OneHot encoded columns:")
    print(df\[['sex', 'sex_Male', 'sex_Female']].head(), "\n")
    ```
    /// html | div.result
    ```plaintext
    OneHot encoded columns:
          sex  sex_Male  sex_Female
    0    Male       1.0         0.0
    1    Male       1.0         0.0
    2    Male       1.0         0.0
    3    Male       1.0         0.0
    4  Female       0.0         1.0
    ```
    ///

## Codi font
!load_file ud3/examples/preparacio_adults.py


## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
- [StackExchange Datascience: Difference between OrdinalEncoder and LabelEncoder](https://datascience.stackexchange.com/questions/39317/difference-between-ordinalencoder-and-labelencoder){: .spell-ignore target="_blank"}
