#!/usr/bin/env python3

import pandas as pd

data = [[5, 6, 7],
        [2, 6, 9]]

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()

cov = df.cov()
print("Matriu de covariància:")
print(cov)
print()

pearson = df.corr(method='pearson')
print("Correlació de Pearson:")
print(pearson)
print()

spearman = df.corr(method='spearman')
print("Correlació de Spearman:")
print(spearman)
print()
