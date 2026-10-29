---
template: document.html
title: Conjunts de dades
icon: material/book-open-variant
alias: conjunts
comments: true
---

## Conjunts de dades
L'objectiu dels models d'__aprenentatge automàtic__ és trobar patrons
en les dades de manera automàtica per a fer prediccions o prendre
decisions.

Per a aconseguir aquest objectiu, és necessari disposar de dades
per a entrenar els models, que cal dividir en diferents conjunts:
__*train* (entrenament)__, __*validation* (validació)__ i __*test* (prova)__.
Cada conjunt té una finalitat específica durant el procés de
creació i avaluació del model.

La mida de cada conjunt depèn de diversos factors, com ara la quantitat
de dades disponibles, la complexitat del model, etc. No obstant això,
una divisió comuna és:

- __Conjunt d'entrenament__: 70-80 % de les dades.
- __Conjunt de validació__: 10-15 % de les dades.
- __Conjunt de prova__: 10-15 % de les dades.

### Conjunt d'entrenament
El __conjunt d'entrenament__ (_training set_) és el conjunt de dades
que s'utilitza per a __entrenar__ el model i ajustar els seus paràmetres.

L'objectiu d'aquest conjunt és construir un model que siga capaç
de realitzar prediccions correctes sobre dades que no ha vist abans.

### Conjunt de validació
El __conjunt de validació__ (_validation set_) és el conjunt de dades
que s'utilitza per a __avaluar__ el model durant el procés d'entrenament.

L'objectiu d'aquest conjunt és valorar el rendiment del model
en el procés d'entrenament.

Aquest conjunt permet ajustar els hiperparàmetres del model (com ara
la taxa d'aprenentatge, nombre de capes de la xarxa neuronal, etc.)
per a millorar el seu rendiment. També ajuda a detectar
problemes com el __sobreajustament__ (_overfitting_).

![Sobreajustament i infraajustament](img/conjunts/overfitting.png)
/// attribution: Autor desconegut
/// figure-caption: Comparació entre el sobreajustament i l'infraajustament.

### Conjunt de prova
El __conjunt de prova__ (_test set_) és el conjunt de dades
que s'utilitza per a __avaluar__ el model després d'haver finalitzat
el procés d'entrenament.

!!! important "Aquest conjunt de dades __no s'utilitza mai__ durant el procés d'entrenament del model."

L'objectiu d'aquest conjunt és avaluar el rendiment del model
amb dades que no ha vist abans i comprovar si és capaç de generalitzar
correctament el problema.


## Importància dels conjunts de dades
Els conjunts de dades són una part fonamental en el procés
d'__aprenentatge automàtic__ per diversos motius, entre els quals
es poden destacar els següents.

### Prevenció del __sobreajustament__
El __sobreajustament__ (_overfitting_) ocorre quan un model aprén
excessivament les característiques particulars de les __dades d'entrenament__
i no és capaç de generalitzar correctament a noves dades.

Per a evitar el __sobreajustament__, s'utilitza el __conjunt de validació__
per a ajustar el model i detectar el problema abans de provar-lo
amb el __conjunt de prova__.

![Evolució de l'error en els conjunts de dades](img/conjunts/overfitting_validation.png)
/// attribution: Autor desconegut
/// figure-caption: Evolució de l'error en els conjunts de dades durant el procés d'entrenament.

### Evitar el biaix en l'avaluació del model
Si s'utilitza el mateix conjunt de dades per a entrenar i avaluar el model,
aquest pot donar la falsa impressió que el model és millor del que realment
és, ja que el model ja coneix les dades amb les quals s'ha d'avaluar.


## Divisió de les dades en conjunts
La divisió de les dades en conjunts es pot realitzar amb diverses llibreries
de Python, com ara `scikit-learn` o `pandas`.

Una consideració important és assegurar la reproductibilitat de la divisió
de les dades, per la qual cosa és recomanable fixar la __llavor (_seed_)__
del generador de nombres aleatoris.

=== "`scikit-learn`"
    ```python
    --8<-- "docs/files/ud3/examples/conjunt_dades.py:import_pandas"

    --8<-- "docs/files/ud3/examples/conjunt_dades.py:import_sklearn"

    --8<-- "docs/files/ud3/examples/conjunt_dades.py:sklearn"
    ```

=== "`pandas`"
    ```python
    --8<-- "docs/files/ud3/examples/conjunt_dades.py:import_pandas"

    --8<-- "docs/files/ud3/examples/conjunt_dades.py:pandas"
    ```

## Codi font
!load_file "ud3/examples/conjunt_dades.py"

## Bibliografia
/// html | div.spell-ignore
- [:octicons-link-external-16: Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/){:target="_blank"} – César Guijarro Rosaleny
- [:octicons-link-external-16: Wikipedia: Training, validation, and test sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets){:target="_blank"}
///

