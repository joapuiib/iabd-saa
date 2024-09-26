import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_bar, labs, theme_minimal

df = pd.read_csv('edats.csv', header=None, names=['age', 'persons'])
df['acumulat'] = df['persons'].cumsum()

print(df)


# Quartils
# q = df['acumulat'].quantile([0.25, 0.5, 0.75])
q = np.interp([0.25, 0.50, 0.75], df['acumulat'], df['age'])


print("Quartils:")
print("Q1 (25%):", q[0])
print("Q2 (50%):", q[1])
print("Q3 (75%):", q[2])

plot = (
    ggplot(df, aes(x='age', y='persons')) +
    geom_bar(stat='identity', fill='steelblue', color='black') +
    labs(title="Age Distribution", x="Age", y="Number of Persons") +
    theme_minimal()
)

plot.show()
