---
template: document.html
title: Estadística bàsica
icon: material/book-open-variant
comments: true
tags:
---

@TODO: Revisar exemples amb Pandas


## Estadística bàsica
L'__aprenentatge automàtic__ està basat en models matemàtics i estàditics.
Per això, és important tindre una base sòlida en estadística per entendre el funcionament dels algoritmes d'aprenentatge automàtic
i analitzar els resultats obtinguts.

L'__estadística__ és una disciplina que estudia la recopilació, anàlisi i interpretació de dades.

En aquests apunts veurem operacions bàsiques com la __mitjana__, la __mediana__, la __moda__, la __desviació estàndard__ i la __variança__.

## Mitjana aritmètica ($\bar{X}$)

La __mitjana aritmètica__ és el valor obtingut en sumar tots els valors d'una mostra i dividir-los pel nombre total de valors.

$$
\bar{X} = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

!!! example
    Donades les edats d'un grup de persones $X = \{ 20, 20, 50, 60, 80 \}$, la mitjana aritmètica és:

    $$
    \bar{X} = \frac{1}{5} (20 + 20 + 50 + 60 + 80) = 46
    $$
    

!!! example "Exemple amb Pandas"
    ```python
    import pandas as pd
     
    df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                       "B":[5, 2, 54, 3, 2], 
                       "C":[20, 16, 7, 3, 8],
                       "D":[14, 3, 17, 2, 6]})

    print("DataFrame:")
    print(df)
     
    # axis = 0 calculará la mitjana de cada columna (A, B, C, D)
    column_mean = df.mean(axis = 0)
    print("Mitjana de cada columna:")
    print(column_mean)
     
    # axis = 1 calculará la mitjana de cada fila (0, 1, 2, 3, 4)
    row_mean = df.mean(axis = 1)
    print("Mitjana de cada fila:")
    print(row_mean)
    ```
    /// html | div.result
    ```text
    DataFrame:
        A   B   C   D
    0  12   5  20  14
    1   4   2  16   3
    2   5  54   7  17
    3  44   3   3   2
    4   1   2   8   6
    Mitjana de cada columna:
    A    13.2
    B    13.2
    C    10.8
    D     8.4
    dtype: float64
    Mitjana de cada fila:
    0    12.75
    1     7.75
    2    20.75
    3    12.75
    4     4.25
    dtype: float64
    ```
    ///

!!! example "Exemple mitjana d'una fila"
    Amb l'anterior `DataFrame`, podem utilitzar la funció [`iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html){:target="_blank"}
    per seleccionar una fila i calcular la mitjana dels seus valors.

    ```python
    mean = df.iloc[0].mean()
    print(mean)
    ```
    /// html | div.result
    ```text
    12.75
    ```

!!! example "Exemple mitjana d'una columna"
    De la mateixa manera, podem calcular la mitjana d'una columna.

    ```python
    mean = df.loc[:,"A"].mean()
    print(mean)
    ```
    /// html | div.result
    ```text
    13.2
    ```
    ///

## Mediana ($\tilde{X}$)
La __mediana__ és el valor que divideix la mostra en dues parts iguals,
és a dir, la meitat dels valors són més grans que la mediana i l'altra meitat són més xicotets.

Per a calcular la mediana, primer s'ordenen els valors de la mostra de menor a major i es tria el valor central.

- Si la mostra té un nombre imparell de valors, la mediana és el valor central.
- Si la mostra té un nombre parell de valors, la mediana és la mitjana aritmètica dels dos valors centrals.

!!! example
    Donades les edats d'un grup de persones $X = \{ 20, 20, 50, 60, 80 \}$, la mediana és:

    $$
    \tilde{X} = 50
    $$

!!! example "Exemple amb Pandas"
    ```python
    median = df.median()
    print("Mediana de cada columna:")
    print(median)
    ```
    /// html | div.result
    ```text
    Mediana de cada columna:
    A    5.0
    B    3.0
    C    8.0
    D    6.0
    dtype: float64
    ```
    ///

## Moda
La __moda__ és el valor que més vegades apareix en una mostra.

!!! example
    Donades les edats d'un grup de persones $X = \{ 20, 20, 50, 60, 80 \}$, la moda és:

    $$
    \text{moda}(X) = 20
    $$

!!! note
    El mètode [`mode()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html){:target="_blank"}
    de Pandas retorna la moda de cada columna.

    Si hi ha més d'una moda, el mètode retorna totes les modes.

!!! example "Exemple amb Pandas"
    ```python
    mode = df.mode()
    print("Moda de cada columna:")
    print(mode)
    ```
    /// html | div.result
    ```text
    Moda de cada columna:
       A  B  C  D
    0  1  2  3  2
    1  4  3  7  3
    2  5  5  8  6
    3 12 54 16 14
    4 44 NaN 20 17
    ```
    ///

## Variança ($\sigma^2$)
La __variança__ és una mesura de la dispersió dels valors d'una mostra respecte a la mitjana.

Es calcula com la mitjana dels quadrats de les diferències entre cada valor i la mitjana.

$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{X})^2
$$

!!! note
    Les diferències són elevades al quadrat per a que siguen sempre positives.

!!! example
    Donades les edats d'un grup de persones $X = \{ 20, 20, 50, 60, 80 \}$, la variança és:

    $$
    \sigma^2 = \frac{1}{5} ((20-46)^2 + (20-46)^2 + (50-46)^2 + (60-46)^2 + (80-46)^2) \\
    \sigma^2 = \frac{1}{5} (676 + 676 + 16 + 196 + 1296) \\
    \sigma^2 = \frac{2856}{5} = 571.2
    $$

!!! example "Exemple amb Pandas"
    ```python
    variance = df.var()
    print("Variança de cada columna:")
    print(variance)
    ```
    /// html | div.result
    ```text
    Variança de cada columna:
    A    340.8
    B    281.2
    C    116.0
    D     46.0
    dtype: float64
    ```
    ///

## Desviació estàndard ($\sigma$)
La __desviació estàndard__ és la arrel quadrada de la variança.
Mesura la dispersió dels valors respecte a la mitjana,
però indica la dispersió en les mateixes unitats que els valors.

$$
\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{X})^2}
$$

!!! example
    Donades les edats d'un grup de persones $X = \{ 20, 20, 50, 60, 80 \}$, la desviació estàndard és:

    $$
    \sigma = \sqrt{571.2} = 23.9
    $$

!!! example "Exemple amb Pandas"
    ```python
    std = df.std()
    print("Desviació estàndard de cada columna:")
    print(std)
    ```
    /// html | div.result
    ```text
    Desviació estàndard de cada columna:
    A    18.457537
    B    16.778211
    C    10.770330
    D     6.782330
    dtype: float64
    ```
    ///


## Quantils
Els __quantils__ són mesures de posició que divideixen una mostra de manera
que una proporció determinada de valors queda a cada costat del quantil.

Els quantils més importants són els __quartils__, __decils__ i __percentils__.

### Quartils
Els __quartils__ divideixen la mostra en quatre parts iguals.

Per tant, obtenim tres punts de tall: $Q_1$, $Q_2$ i $Q_3$, corresponents al 25%, 50% i 75% de la mostra.

<figure id=figure-1>
    <img src="../img/quartils.png" alt="Quartils">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 1: Quartils</figcaption>
</figure>

!!! example "Quartils en Pandas"
    @TODO: Exemple amb Pandas

### Decils
Els __decils__ divideixen la mostra en deu parts iguals, cadascuna amb el 10% dels valors.

<figure id=figure-2>
    <img src="../img/decils.png" alt="Decils">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 2: Decils</figcaption>
</figure>

### Percentils
Els __percentils__ divideixen la mostra en cent parts iguals, cadascuna amb el 1% dels valors.

És una de les mesures més utilitzades en estadística per a comparar valors.

!!! example
    @TODO: Exemple

!!! example "Percentils en Pandas"
    @TODO: Exemple amb Pandas

## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/) de César Guijarro Rosaleny
- [Quantil, Viquipèdia](https://ca.wikipedia.org/wiki/Quantil)
