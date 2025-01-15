---
template: document.html
title: Mètriques de regressió
icon: material/book-open-variant
comments: true
alias: regressio-metriques
---

*[MAE]: Mean Absolute Error
*[MSE]: Mean Squared Error
*[RMSE]: Root Mean Squared Error


## Mètriques de regressió
Les mètriques són mesures que ens permeten avaluar la qualitat d'un model de regressió,
que determinen com de bé s'ajusta el model a les dades i com de precises són les prediccions.

!!! prep "Dades d'exemple"
    /// html | div.columns

    | Real ($Y$) | Predicció ($\hat{Y}$) |
    |------------|-----------------------|
    | 50         | 52                    |
    | 60         | 58                    |
    | 70         | 68                    |
    | 80         | 85                    |

    ```python
    import pandas as pd

    Y = pd.Series([50, 60, 70, 80])
    pred_Y = pd.Series([52, 58, 68, 85])
    ```
    ///


### MAE – Error absolut mitjà
L'__error absolut mitjà (Mean Absolute Error o MAE)__ és la mitjana de les diferències
absolutes entre les prediccions ($\hat{y}$) i els valors reals ($y$).

La fórmula per calcular l'error absolut mitjà és:

```math
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
```

!!! example "Càlcul de l'error absolut mitjà"
    === "`pandas`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:mae_pandas"
        ```
    === "`scikit-learn`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:mae_sklearn"
        ```

    ```
    MAE: 2.75
    ```

Quan més xicotet siga el MAE, millor serà el model.
És fàcil d'interpretar ja que està expressat en les mateixes
que la variable dependent.

### MSE – Error quadràtic mitjà
L'__error quadràtic mitjà (Mean Squared Error o MSE)__ és la mitjana de les diferències
elevades al quadrat entre les prediccions ($\hat{y}$) i els valors reals ($y$).

La fórmula per calcular l'error quadràtic mitjà és:

```math
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```

El MSE és més sensible als errors grans que el MAE, ja que eleva al quadrat
les diferències. Això fa que els errors més grans tinguin un pes més gran
en la mesura.

!!! example "Càlcul de l'error quadràtic mitjà"
    === "`pandas`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:mse_pandas"
        ```
    === "`scikit-learn`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:mse_sklearn"
        ```

    ```
    MSE: 9.25
    ```

### RMSE – Arrel de l'error quadràtic mitjà
L'__arrel de l'error quadràtic mitjà (Root Mean Squared Error o RMSE)__ és la
arrel quadrada del MSE.

```math
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
```

Aquesta mètrica és equivalent al MSE però més fàcil d'interpretar,
ja que expressada en les mateixes unitats que la variable dependent.

!!! example "Càlcul de l'arrel de l'error quadràtic mitjà"
    === "`pandas`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:rmse_pandas"
        ```
    === "`scikit-learn`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:rmse_sklearn"
        ```

    ```
    RMSE: 3.04
    ```

### R² – Coeficient de determinació
El __coeficient de determinació ($R^2$)__ és una mesura que indica com de bé
s'ajusta el model als valors reals.

El coeficient de determinació pot prendre valors entre 0 i 1, sent 1 el millor valor
possible. Un valor de 0 indica que el model no s'ajusta als valors reals.

El coeficient de determinació es pot calcular com:

```math
R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
```

On:

- $y_i$ són els valors reals.
- $\hat{y}_i$ són les prediccions del model.
- $\bar{y}$ és la mitjana dels valors reals.


!!! example "Càlcul del coeficient de determinació $R^2$"
    === "`pandas`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:r2_pandas"
        ```
    === "`scikit-learn`"
        ```python
        --8<-- "docs/files/ud4/examples/metriques_regressio.py:r2_sklearn"
        ```

    ```
    R^2: 0.93
    ```