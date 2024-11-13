#!/usr/bin/env python

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import os
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, OneHotEncoder
from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns


def download(url, filepath):
    http_response = urlopen(url)
    content = http_response.read()
    with open(filepath, 'wb') as f:
        f.write(content)


files_folder = '../../files/ud3'
if not os.path.exists(files_folder):
    os.makedirs(files_folder)

file_path = os.path.join(files_folder, 'adult.data.csv')
if not os.path.exists(file_path):
    adult_dataset_url = 'https://raw.githubusercontent.com/joapuiib/saa-datasets/refs/heads/main/adult.data.csv'
    print('Downloading dataset...')
    download(adult_dataset_url, file_path)
else:
    print(f'Dataset found at {file_path}')


df = pd.read_csv(file_path)
df_numerics = df.select_dtypes(include = ['float64', 'int64'])

def densitat_etiquetes():

    figure=plt.figure(figsize = (15, 6))

    for i, column in enumerate(df_numerics.columns, 1):
            axes = figure.add_subplot(3,2,i)
            sns.kdeplot(x = df_numerics[column], hue = df['income'], fill = True, ax = axes)
            figure.tight_layout()


def histograma():
    figure=plt.figure(figsize = (15, 20))

    for i, column in enumerate(df.columns, 1):
        axes = figure.add_subplot(5,3,i)
        sns.histplot(x = df[column], ax = axes)
        axes.tick_params(axis='x', rotation=45)
        for label in axes.get_xticklabels():
            label.set_ha('right')  # Align labels to the right
        figure.tight_layout()


def relacions_variable():
    n_samples_to_plot = 5000
    columns = ['age', 'education-num', 'hours-per-week']
    _ = sns.pairplot(data=df[:n_samples_to_plot], vars=columns,
                     hue="income", plot_kws={'alpha': 0.2},
                     height=3, diag_kind='hist', diag_kws={'bins': 30})

def scatterplot():
    ax = sns.scatterplot(
        x="age", y="hours-per-week", data=df,
        hue="income", alpha=0.5,
    )


def matriu_correlacio():
    corr_df = df_numerics.corr(method='pearson')

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df, annot=True)


def boxplot():
    sns.boxplot(x='income', y ='age', hue='income', data = df)


# histograma()
# relacions_variable()
# scatterplot()
# matriu_correlacio()
boxplot()
plt.show()
