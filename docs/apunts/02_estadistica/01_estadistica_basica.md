---
template: document.html
title: Estadística bàsica
icon: material/book-open-variant
comments: true
tags:
---


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
    Donades les edats d'un grup de persones $X = \{ 20, 21, 50, 60, 80 \}$, la mitjana aritmètica és:

    $$
    \bar{X} = \frac{1}{5} (20 + 21 + 50 + 60 + 80) = 46.2
    $$
    

!!! example "Exemple amb Pandas"
    ```python
    import pandas as pd
     
    df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                       "B":[5, 2, 54, 3, 2], 
                       "C":[20, 16, 7, 3, 8],
                       "D":[14, 3, 17, 2, 6]})
     
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
