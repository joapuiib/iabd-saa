---
template: document.html
title: Normalització
icon: material/book-open-variant
comments: true
alias: normalitzacio
---

## Normalització
No totes les dades tenen __la mateixa escala__, és a dir, no tenen el mateix rang de valors.
Això pot suposar un problema per als algoritmes d'aprenentatge automàtic, ja que poden donar més pes
a les característiques amb valors més grans.

Per això, és important __normalitzar__ les dades abans d'aplicar un algoritme d'aprenentatge automàtic.

La llibraría `scikit-learn` proporciona diverses tècniques de normalització
a través del mòdul `sklearn.preprocessing`.

### `MinMaxScaler`
Una tècnica comuna de normalització és `MinMaxScaler`,
que __redimensiona les dades entre 0 i 1__ utilitzant el valor mínim i màxim de cada característica.

$$
X_{\text{norm}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}}
$$

??? example
    Donades les dades d'entrada $X = [1, 2, 3, 4, 5]$,

    La normalització queda com:

    $$
    X_{\text{norm}} = \frac{X - 1}{5 - 1} = \left[0, 0.25, 0.5, 0.75, 1\right]
    $$


La classe `MinMaxScaler` de `scikit-learn` permet normalitzar les dades
amb aquesta tècnica.

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)
```

- La funció `fit_transform` ajusta el `scaler` als valors mínim i màxim de les dades d'entrenament
    i normalitza les dades d'entrenament.
- La funció `transform` normalitza les dades de prova sense modificar el `scaler`.


### `StandardScaler`
Una altra tècnica comuna de normalització és `StandardScaler`,
que redimensiona les dades perquè el conjunt de cada característica tinga __mitjana igual a 0 ($\mu = 0$)
i desviació estàndard igual a 1 ($\sigma = 1$)__.

$$
X_{\text{norm}} = \frac{X - \mu}{\sigma}
$$

??? example
    Donades les dades d'entrada $X = [1, 2, 3, 4, 5]$, on $\mu = 3$ i $\sigma = 1.41$,

    La normalització queda com:

    $$
    X_{\text{norm}} = \frac{X - 3}{1.41} = \left[-1.41, -0.71, 0, 0.71, 1.41\right]
    $$

La classe `StandardScaler` de `scikit-learn` permet normalitzar les dades
amb aquesta tècnica.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)
```



/// html | div.spell-ignore
## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic" de César Guijarro](https://cesguiro.es/){:target="_blank"} de César Guijarro Rosaleny
///
