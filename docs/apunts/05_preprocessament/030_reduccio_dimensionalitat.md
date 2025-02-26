---
template: document.html
title: Reduccio de la dimensionalitat
icon: material/book-open-variant
comments: true
alias: reduccio-dimensionalitat
---

## Reducció de la dimensionalitat
S'entén com __reducció de dimensionalitat__ les diferents tècniques que permeten reduir el
nombre de característiques o variables d'un conjunt de dades, però tractant de mantindre
la major part de la informació.

Reduir la dimensionalitat pot ser útil per millorar el rendiment dels algoritmes d'aprenentatge
automàtic, ja que permet:

- Simplificar el model, que a més serà més fàcil d'interpretar.
- Reduir els requeriments computacionals i temps de càlcul.
- Evitar que les dades siguen excessivament disperses.

## Tècniques de reducció de dimensionalitat
Les tècniques de reducció de dimensionalitat es poden dividir en dos grans grups:

- __Selecció de característiques (_feature selection_)__: Consisteix en seleccionar un subconjunt de les característiques originals.

    La principal premisa és que no totes les característiques són rellevants per a la tasca de predicció,
    ja que les dades poden contindre característiques que són __irrelevants__ o __redundants__.
    Aquestes característiques poden ser eliminades sense afectar la informació del conjunt de dades.

- __Extracció de característiques (_feature extraction_)__: Consisteix en transformar les característiques originals en un nou conjunt
    de característiques, que són una combinació de les característiques originals. Aquestes noves característiques
    són anomenades __components__ i emmagatzemen la major part de la informació de les característiques originals.

### Selecció de característiques
Dins de les tècniques de selecció de característiques, podem classificar-les en diferents categories:

- __Métodes de filtre__: Són mètodes que analitzen la relevància de les característiques a partir d'una funció sobre les dades.
    Aquesta funció pot ser una mesura estadística com la variança o la correlació, i és independent de l'algoritme d'aprenentatge
    automàtic que s'utilitzarà.

    Aquests mètodes poden ser:
    
    - __Univariats__, que analitzen les característiques de manera individual.

        _Exemple [__VarianceThreshold__][exemple-variance-threshold]: Elimina les característiques amb baixa variància._

    - __Multivariats__, que analitzen les característiques de manera conjunta.

        _Exemple [__Correlation-based Feature Selection__][exemple-correlation-selection]: Elimina les característiques amb alta correlació._

    [exemple-variance-threshold]: 031_filtre.md#umbral-de-variancia
    [exemple-correlation-selection]: 031_filtre.md#basada-en-correlacio

- __Mètodes d'envoltura__: Són mètodes que seleccionen les característiques basant-se
    en el rendiment d'un model d'aprenentatge automàtic.

    Aquests mètodes poden ser:
    
    - [__Forward selection__][forward]: Comença amb un conjunt buit de característiques i va afegint-ne una a una.
    - [__Backward elimination__][backward]: Comença amb totes les característiques i va eliminant-ne una a una.
    - [__Bidirectional selection__][bidirectional]: Combina els dos mètodes anteriors.

    [forward]: 032_envoltura.md#seleccio-cap-endavant
    [backward]: 032_envoltura.md#seleccio-cap-enrere
    [bidirectional]: 032_envoltura.md#seleccio-bidireccional


### Extracció de característiques
Alguns dels mètodes més comuns d'extracció de característiques numèriques són:

- [__PCA (Principal Component Analysis)__][pca]: És una tècnica de reducció de dimensionalitat que transforma les característiques originals
    en un nou conjunt de característiques no correlacionades anomenades components principals.

- [__LDA (Linear Discriminant Analysis)__][lda]: És una tècnica de reducció de dimensionalitat que transforma les característiques originals
    en un nou conjunt de característiques que maximitzen la separació entre les classes.

[pca]: 033_extraccio.md#pca-principal-component-analysis
[lda]: 033_extraccio.md#lda-linear-discriminant-analysis

## Bibliografia
- [Viquipèdia - Reducció de dimensionalitat](https://ca.wikipedia.org/wiki/Reducci%C3%B3_de_dimensionalitat)
- [Stats StackExchange - Should we normalize before using VarianceThreshold in sklearn?](https://stats.stackexchange.com/questions/253920/should-we-normalize-before-using-variancethreshold-in-sklearn)