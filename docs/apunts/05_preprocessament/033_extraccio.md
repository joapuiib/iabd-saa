---
template: document.html
title: "Extracció de característiques: PCA i LDA"
icon: material/file-check-outline
comments: true
alias: pca-lda
---

*[PCA]: Principal Component Analysis
*[LDA]: Linear Discriminant Analysis

## Extracció de característiques
El procés __d'extracció de característiques__ en la __reducció de dimensionalitat__
consisteix en transformar les característiques originals en un nou conjunt
de característiques més reduït, que emmagatzemen la major part de la informació
de les característiques originals.

### PCA - Principal Component Analysis
El __PCA__ (_Principal Component Analysis_) és una tècnica d'extracció de característiques
que permet reduir la dimensionalitat d'un conjunt de dades,
transformant les característiques originals en un nou conjunt de característiques
no correlacionades anomenades __components principals__.

```python
--8<-- "docs/files/ud5/examples/reduccio_extraccio.py:import_pca"

--8<-- "docs/files/ud5/examples/reduccio_extraccio.py:pca"
```

### LDA - Linear Discriminant Analysis
El __LDA__ (_Linear Discriminant Analysis_) és una tècnica d'extracció de
característiques que permet reduir la dimensionalitat d'un conjunt de dades,
transformant les característiques originals en un nou conjunt de característiques
que maximitzen la separació entre les classes.

```python
--8<-- "docs/files/ud5/examples/reduccio_extraccio.py:import_lda"

--8<-- "docs/files/ud5/examples/reduccio_extraccio.py:lda"
```

## Codi font
!load_file "ud5/examples/reduccio_extraccio.py"


/// html | div.spell-ignore
## Bibliografia
///
