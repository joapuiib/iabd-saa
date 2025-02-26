---
template: document.html
title: "Selecció de característiques: Mètodes d'envoltura"
icon: material/file-check-outline
comments: true
alias: seleccio-envoltura
---

## Selecció de característiques: Mètodes d'envoltura
Els mètodes d'envoltura són una tècnica de reducció de dimensionalitat
basada en la selecció de característiques que seleccionen les característiques
basant-se en el rendiment d'un model d'aprenentatge automàtic.

### Selecció cap endavant
La __selecció cap endavant (_forward selection_)__ és un mètode d'envoltura
que es basa en seleccionar les característiques d'una a una,
afegint la característica que millora més el rendiment del model
en cada pas.

La classe `SequentialFeatureSelector` de `mlxtend` implementa aquest mètode,
utilitzant el paràmetre `forward=True`.

```python
--8<-- "docs/files/ud5/examples/reduccio_envoltura.py:lib"

--8<-- "docs/files/ud5/examples/reduccio_envoltura.py:forward"
```

### Selecció cap enrere
La __selecció cap enrere (_backward elimination_)__ és un mètode d'envoltura
que parteix de totes les característiques i va eliminant-ne una
a una, eliminant la característica que més empitjora el rendiment
del model en cada pas.

Aquest mètode també es pot implementar amb la classe `SequentialFeatureSelector`
de `mlxtend`, utilitzant el paràmetre `forward=False`.

```python
--8<-- "docs/files/ud5/examples/reduccio_envoltura.py:backward"
```


### Selecció bidireccional
La __selecció bidireccional (_bidirectional selection_)__ és un mètode
d'envoltura que combina els dos mètodes anteriors, afegint i eliminant
característiques en cada pas.


Aquest mètode també es pot implementar amb la classe `SequentialFeatureSelector`
de `mlxtend`, utilitzant el paràmetre floating=True`.

- `forward=True` i `floating=True`: Selecció cap endavant amb possibilitat
    d'eliminar característiques seleccionades.

```python
--8<-- "docs/files/ud5/examples/reduccio_envoltura.py:bidirectional_forward"
```

- `forward=False` i `floating=True`: Selecció cap enrere amb possibilitat
    de tornar a afegir característiques eliminades.

```python
--8<-- "docs/files/ud5/examples/reduccio_envoltura.py:bidirectional_backward"
```

## Codi font
!load_file ud5/examples/reduccio_envoltura.py

/// html | div.spell-ignore
## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic" de César Guijarro](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
- [w3schools - Data Science - Regression Table: P-Value](https://www.w3schools.com/datascience/ds_linear_regression_pvalue.asp){:target="_blank"}
- [`mlxtemd` - `SequentialFeatureSelector`: The popular forward and backward feature selection approaches](https://rasbt.github.io/mlxtend/user_guide/feature_selection/SequentialFeatureSelector/){:target="_blank"}
///
