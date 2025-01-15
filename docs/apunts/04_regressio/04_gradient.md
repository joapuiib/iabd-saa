---
template: document.html
title: Descens del gradient
icon: material/book-open-variant
comments: true
alias: descens-gradient
---

*[SGD]: Stochastic Gradient Descent

## Descens del gradient
L'__algorisme del gradient descendent__ és un mètode iteratiu
d'optimització que permet trobar el mínim d'una funció.

Aquest algorisme es basa en utilitzar la derivada de la funció
de cost per trobar la direcció en la qual la funció de cost
descendeix més ràpidament.

Aquest algorisme és molt útil ja que permet la utilització de diferents
funcions de cost i diferents mètodes de regularització.

## Funció de cost
La __funció de cost__ és una funció que mesura la diferència entre
els valors predits pel model i els valors reals de les dades.

Aquesta funció és la que l'algorisme del gradient descendent
tracta d'optimitzar i minimitzar.

En el cas de problemes de regressió, trobem les següents funcions de cost:

- `squared_loss`: [[regressio-metriques#mse-error-quadratic-mitja]].
- `huber`: funció de cost robusta a outliers.
- `epsilon_insensitive`: funció de cost de [màquina de suport vectorial](https://ca.wikipedia.org/wiki/M%C3%A0quina_de_vector_de_suport).

## Regulització
La __regularització__ és un mètode que permet evitar el sobreajustament
dels models de regressió.

Aquest mètode consisteix en afegir un terme a la funció de cost
que penalitza els pesos del model, evitant que aprenguen massa
els valors de les dades d'entrenament.

Els dos mètodes de regularització més comuns són:

- `l1`: regularització L1 o _Lasso_.
- `l2`: regularització L2 o _Ridge_.


## `SGDRegressor`
La classe `SGDRegressor` de `scikit-learn` implementa l'algorisme
del gradient descendent estocàstic (_Stochastic Gradient Descent_ o _SGD_).

```python
from sklearn.linear_model import SGDRegressor

model = SGDRegressor(loss='squared_loss', penalty='l2')
```

Aquest model té els següents hiperparàmetres:

- `loss`: funció de cost a optimitzar (_per defecte_: `squared_loss`).
- `penalty`: mètode de regularització (_per defecte_: `l2`).
- `alpha`: terme de regularització (_per defecte_: `0.0001`).
- `max_iter`: nombre màxim d'iteracions (_per defecte_: `1000`).
- `shuffle`: barreja les dades a cada iteració (_per defecte_: `True`).

!!! docs
    Documentació oficial de [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html)

## Codi font
Aquest exemple utilitza el procés de [[normalitzacio|Normalització]] de les dades
mitjançant la classe `StandardScaler`, que encara no hem estudiat.

!load_file ud4/examples/descens_gradient.py

/// html | div.spell-ignore
## Recursos addicionals
- [¿Qué es el Descenso del Gradiente? Algoritmo de Inteligencia Artificial | DotCSV
](https://www.youtube.com/watch?v=A6FiCDoz8_4)
- [IA NOTEBOOK #3 | Descenso del Gradiente (Gradient Descent) | Programando IA
](https://www.youtube.com/watch?v=-_A_AAxqzCg)


## Bibliografia
- [Algorisme del gradient descendent – Viquipèdia](https://ca.wikipedia.org/wiki/Algorisme_del_gradient_descendent)
- [1.5. Stochastic Gradient Descent – scikit-learn](https://scikit-learn.org/stable/modules/sgd.html)
- [Huber loss - Wikipedia](https://en.wikipedia.org/wiki/Huber_loss)
///