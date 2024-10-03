---
template: document.html
title: Introducció a Pandas
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
- [Llibre "pandas: powerful Python data analysis toolkit"](https://pandas.pydata.org/pandas-docs/version/1.4.4/pandas.pdf){:target="_blank"}
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
Una `Series` es pot crear a partir d'una llista de valors:

```python
@TODO
```
