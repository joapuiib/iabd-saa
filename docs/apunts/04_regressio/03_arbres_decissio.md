---
template: document.html
title: Regressió amb arbres de decissió
icon: material/book-open-variant
comments: true
alias: regressio-arbres-decissio
---

*[DT]: Decision Tree

## Regressió amb arbres de decissió
Els __arbres de decissió__ (_decision trees_ o _DT_) són models d'aprenentatge automàtic
supervisat que poden resoldre problemes de classificació i regressió.

Aquests models es basen l'aprenentatge de decisions simples a partir de les dades
en forma d'estructura d'arbre.

=== "Classificació"
    ![Exemple d'arbre de decissió](img/arbres_decissio/iris_decision_tree.svg){: style="max-width: 800px;"}
    /// attribution
    [Scikit-learn: Decision Trees](https://scikit-learn.org/stable/modules/tree.html#classification){:target="_blank"}
    ///
    /// figure-caption
    Exemple d'arbre de decissió de classificació del [conjunt de dades Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set){:target="_blank"}.
    ///

=== "Regressió"
    ![Exemple d'arbre de regresió](img/arbres_decissio/sin_decision_tree.png){: style="max-width: 800px;"}
    /// attribution
    [Scikit-learn: Decision Trees](https://scikit-learn.org/stable/modules/tree.html#classification){:target="_blank"}
    ///
    /// figure-caption
    Exemple d'arbre de decissió de regressió de la funció $\sin(x)$.
    ///


## Model de regressió amb arbres de decissió
Els arbres de decissió poden ser utilitzats per resoldre problemes de regressió.

Podem crear un model de regressió amb arbres de decissió amb Scikit-learn
mitjançant la classe `DecisionTreeRegressor`.

!!! docs
    Documentació oficial de [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html){:target="_blank"}

???+ prep "Preparació de les dades"
    Anem a generar un conjunt de dades que s'ajusten la funció $\sin(x)$ amb una lleugera desviació.

    ```python
    --8<-- "docs/files/ud4/examples/arbres_decissio.py:dades"
    ```

    ![Dades generades a partir del la funció sinus](img/arbres_decissio/dades.png)
    /// figure-caption
    Dades generades a partir de la funció $\sin(x)$.
    ///


### Creació del model
El model `DecisionTreeRegressor` té el hiparàmetre `max_depth` que determina la profunditat màxima de l'arbre de decissió.

Un valor massa alt d'aquest paràmetre pot provocar __sobreajustament (_overfitting_)__.

```python
--8<-- "docs/files/ud4/examples/arbres_decissio.py:model"
```


### Entrenament del model
Per entrenar el model amb les dades, utilitzem el mètode `fit` de la classe `DecisionTreeRegressor`.

```python
--8<-- "docs/files/ud4/examples/arbres_decissio.py:fit"
```

### Predicció i avaluació del model
Una vegada entrenat, podem fer prediccions amb el model i avaluar-lo.

```python
--8<-- "docs/files/ud4/examples/arbres_decissio.py:predict"
```
/// html | div.result
```
RMSE arbre decissió: 0.11
R2 arbre decissió: 0.81
```
///


## Visualització de l'arbre de decissió
Podem visualitzar l'arbre de decissió de les dades de prova
amb una gràfica.

```python
--8<-- "docs/files/ud4/examples/arbres_decissio.py:plot"
```
/// html | div.result

![Model de regressió mitjançant arbre de decissió](img/arbres_decissio/plot.png)
//// figure-caption
Model de regressió mitjançant arbre de decissió.
////

///

## Codi font
!load_file "ud4/examples/arbres_decissio.py"

/// html | div.spell-ignore
## Recursos addicionals
- [¿Qué es Decision Tree y Random Forest? | MindMachineTV](https://www.youtube.com/watch?v=tYPi6qcCQbg)

## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic" de César Guijarro](https://cesguiro.es/) de César Guijarro Rosaleny	
- [Decision Trees - Scikit-learn](https://scikit-learn.org/stable/modules/tree.html)
- [Decision Tree - Wikipedia](https://en.wikipedia.org/wiki/Decision_tree)
///