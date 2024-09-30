#!/usr/bin/env python3

import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_bar, labs, theme_minimal, geom_point
from sklearn.mixture import GaussianMixture

df = pd.read_csv('edats.csv', header=None, names=['age', 'persons'])
df['proportion'] = df['persons'] / df['persons'].sum()
df['downsampled'] = (df['proportion'] * 100000).round().astype(int)

# print(df)


plot = (
    ggplot(df, aes(x='age', y='persons')) +
    geom_bar(stat='identity', fill='steelblue', color='black') +
    labs(title="Age Distribution", x="Age", y="Number of Persons") +
    theme_minimal()
)

downsampled_plot = (
    # plot +
    ggplot(df, aes(x='age', y='downsampled')) +
    geom_bar(stat='identity', fill='steelblue', color='black') +
    labs(title="Age Distribution", x="Age", y="Number of Persons") +
    theme_minimal()
)

# plot.show()
# downsampled_plot.show()

n_components = 3
downsampled_ages = df.loc[df.index.repeat(df['downsampled'])]['age'].values.reshape(-1, 1)

gmm = GaussianMixture(n_components=n_components, random_state=42)
gmm.fit(downsampled_ages)

# print(gmm.means_)
# print(gmm.weights_)
# print(gmm.covariances_)

# Generate 100 random samples from the model
samples, _ = gmm.sample(10000)


# Histogram of the samples
samples_df = pd.DataFrame(samples)
samples_df = samples_df[samples_df[0] >= 0]
samples_df = samples_df.round().astype(int)

generated_df = samples_df.value_counts().sort_index().reset_index()
generated_df.columns = ['age', 'count']

# print(generated_df)

generated_plot = (
    ggplot(generated_df, aes(x='age', y='count')) +
    geom_bar(stat='identity', fill='steelblue', color='black') +
    labs(title="Generated Age Distribution", x="Age", y="Number of Persons") +
    theme_minimal()
)

# generated_plot.show()

# print all generated samples separated by commas
samples_str = ',\n'.join([str(x[0]) for x in samples_df.values])
print(samples_str)
