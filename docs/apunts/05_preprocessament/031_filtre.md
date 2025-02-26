---
template: document.html
title: "Selecció de característiques: Mètodes de filtre"
icon: material/file-check-outline
comments: true
alias: seleccio-filtre
---

## Selecció de característiques: Mètodes de filtre
Els __mètodes de filtre__ són una tècnica de reducció de dimensionalitat
basada en la selecció de característiques que analitzen la relevància de
les característiques a partir d'una funció sobre les dades.

### Umbral de variància
L'__umbral de variància__ és una tècnica de filtre __univariada__ que es
basa en eliminar les característiques amb baixa variància,
ja que aquestes no aporten informació rellevant al model.

La classe `VarianceThreshold` de `scikit-learn` permet eliminar les característiques
amb baixa variància.

```python
constant_filter = VarianceThreshold(threshold=0)
constant_filter.fit_transform(X_train)
constant_filter.transform(X_test)
```

El paràmetre `threshold` indica el valor de la variància per sobre del qual
les característiques seran considerades.

- Si `threshold=0`, es eliminaran les característiques amb variància zero.
- Si `threshold` és un valor diferent de zero, es eliminaran les característiques amb variància inferior a aquest valor.
   
   En aquest cas, és important normalitzar les dades mitjançant `MinMaxScaler`
   per evitar que l'escala afecte al càlcul de la variància.


### Basada en correlació
La selecció de característiques basada en correlació és una tècnica de filtre
__multivariada__ que elimina les característiques amb alta correlació,
ja que aquestes aporten la mateixa informació al model.

Per eliminar les característiques amb alta correlació, cal seguir els següents passos:

1. Obtindre la matriu de correlació de les característiques.

```python
corr_matrix = X_train.corr().abs()
```

2. Seleccionar la part superior de la matriu de correlació,
   ja que la matriu és simètrica i la diagonal principal conté
   la correlació de cada característica amb ella mateixa.

```python
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
```

3. Trobar les característiques amb una correlació superior a un determinat umbral,
   que seran les que eliminarem.

```python
corr_threshold = 0.7
to_drop = [column for column in upper.columns if any(upper[column] > corr_threshold)]
```

4. Eliminar les característiques amb alta correlació.

```python
# Drop features
X_train = X_train.drop(columns=to_drop, axis=1)
X_test = X_test.drop(columns=to_drop, axis=1)
```

## Codi font
!load_file ud5/examples/reduccio_filtres.py

/// html | div.spell-ignore
## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic" de César Guijarro](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
///
