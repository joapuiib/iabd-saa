---
template: document.html
title: Altres models de regressió
icon: material/book-open-variant
comments: true
alias: regressio-altres
---

*[GPR]: Gaussian Process Regression
*[SVR]: Support Vector Regression
*[SVM]: Support Vector Machine

## Altres models de regressió
A part dels models de regressió vistos fins ara, hi ha molts altres models
que es poden utilitzar per resoldre problemes de regressió.

Aquesta pàgina recull alguns d'aquests models i com es poden utilitzar
amb la biblioteca `scikit-learn`.

### Gaussian Process Regression (GPR)
La classe `GaussianProcessRegressor` de `scikit-learn` implementa
el model de regressió de processos gaussians (_Gaussian Process Regression_ o _GPR_).

#### Recursos
/// html | div.spell-ignore
- [Gaussian Process Regression - scikit-learn](https://scikit-learn.org/stable/modules/gaussian_process.html)
- [Gaussian Processes regression: basic introductory example - scikit-learn](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html#sphx-glr-auto-examples-gaussian-process-plot-gpr-noisy-targets-py)
///

### Support Vector Regression (SVR)
La classe `SVR` de `scikit-learn` implementa el model de regressió (_Support Vector Regression_ o _SVR_)
de __màquina de suport vectorial__ (_Support Vector Machine_ o _SVM_).

#### Recursos
/// html | div.spell-ignore
- [Support Vector Regression Tutorial for Machine Learning - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2020/03/support-vector-regression-tutorial-for-machine-learning/)
- [Support Vector Machine (SVM) - scikit-learn](https://scikit-learn.org/stable/modules/svm.html#regression)
- [Support Vector Regression (SVR) using linear and non-linear kernels - scikit-learn](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#sphx-glr-auto-examples-svm-plot-svm-regression-py)
///