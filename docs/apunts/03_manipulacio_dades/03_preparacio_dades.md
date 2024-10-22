---
template: document.html
title: Preparació de les dades
icon: material/book-open-variant
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

!!! info
    En aquests apunts treballarem en el següent conjunt de dades
    [adult-dataset](https://www.kaggle.com/datasets/mlbysoham/adult-dataset){target=_blank}.

### Informació sobre les dades
El primer pas és conèixer les dades amb les quals treballarem.

Podem obtindre informació sobre les dades utilitzant diferents mètodes.

Els mètodes `head()`, `tail()`, `info()` vists a
[[pandas#informacio-de-les-dades]]{target=_blank})
ens permeten obtenir una visió general de les dades.

??? example "Exemple: `head()`, `tail()` i `info()` adults-dataset"
    @TODO

A més, podem utilitzar els següents mètodes
per obtindre més informació:

- `describe()`: proporciona estadístiques descriptives del conjunt de dades.
    - `count`: nombre de valors no nuls.
    - `mean`: mitjana dels valors.
    - `std`: desviació estàndard dels valors.
    - `min`: valor mínim.
    - `25%`: primer quartil.
    - `50%`: mediana.
    - `75%`: tercer quartil.
    - `max`: valor màxim.
- `shape`: proporciona el nombre de files i columnes del conjunt de dades.

??? example "Exemple: `describe()` i `shape` adults-dataset"
    @TODO

### Anàlisi visual de les dades

### Valors nuls
Un dels problemes més comuns en les dades són els valors nuls,
ja que la majoria de models no permeten treballar amb valors no numèrics.

Podem identificar els valors nuls amb el mètode `isnull()`.

??? example "Exemple: `isnull()` adults-dataset"
    @TODO `isnull().sum()`

En aquest cas, podem tractar-los de tres maneres diferents:

- Eliminar les files amb valors nuls.
- Eliminar la columna amb valors nuls.
- Inferir els valors nuls.

Depenent de la tipologia de les dades, una opció serà més adequada que una altra.

@TODO Exemples de com tractar els valors nuls


## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
