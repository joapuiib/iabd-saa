---
template: document.html
title: "Solució: Anàlisi visual de house prices"
icon: material/file-check-outline
alias: analisi-visual-houses
---

## Anàlisi visual de House Prices
```python
import matplotlib.pyplot as plt
import seaborn as sns

df_numerics = house_data.select_dtypes(include = ['float64', 'int64'])
df_objects = house_data.select_dtypes(include=['object'])

# Densitat per columna
figure=plt.figure(figsize = (30, 40))

columns = 3
rows = df_numerics.shape[1] // columns + 1

for i, column in enumerate(df_numerics.columns, 1):
        axes = figure.add_subplot(rows,columns,i)
        sns.kdeplot(x = df_numerics[column], hue = house_data['SalePriceQ'], fill = True, ax = axes)
        figure.tight_layout()
plt.show()


# Histograma
figure=plt.figure(figsize = (30, 40))

columns = 4
rows = df_objects.shape[1] // columns + 1

for i, column in enumerate(df_objects.columns, 1):
    axes = figure.add_subplot(rows,columns,i)
    sns.histplot(x = df_objects[column], ax = axes, hue=house_data["SalePriceQ"],  multiple='dodge')
    axes.tick_params(axis='x', rotation=45)
    for label in axes.get_xticklabels():
        label.set_ha('right')  # Align labels to the right
    figure.tight_layout()
plt.show()


# Scatter-plot entre parell de columnes
columns = ['OverallQual', 'OverallCond', 'GarageArea', 'GrLivArea', 'YearBuilt']
_ = sns.pairplot(data=house_data, vars=columns,
                 hue="SalePriceQ", plot_kws={'alpha': 0.2},
                 height=3, diag_kind='kde')
plt.show()


# Single scatter-plot
ax = sns.scatterplot(
        x="GrLivArea", y="YearBuilt", data=house_data,
        hue="SalePriceQ", alpha=0.5,
    )
plt.show()


# Correlation matrix
columns = ['OverallQual', 'OverallCond', 'GarageArea', 'GrLivArea', 'YearBuilt']
corr_df = house_data[columns].corr(method='pearson', numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True)
plt.show()
```
