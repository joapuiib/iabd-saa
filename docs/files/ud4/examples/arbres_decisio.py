#!/usr/bin/env python

# --8<-- [start:dades]
import numpy as np
from sklearn.model_selection import train_test_split


def f(x):
    return np.sin(x / 5)

np.random.seed(42)
n_samples = 200

X = np.random.uniform(-50, 50, n_samples)
Y = f(X) + np.random.randn(n_samples) * 0.25
X = X.reshape(-1, 1) # Convertim X en una matriu de 1 columna

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_test, Y_test = zip(*sorted(zip(X_test, Y_test))) # Ordenem les dades de test per visualitzar-les correctament
# --8<-- [end:dades]

import matplotlib.pyplot as plt

plt.scatter(X_train, Y_train, color='blue')
plt.scatter(X_test, Y_test, color='orange')
plt.show()

# --8<-- [start:model]
from sklearn.tree import DecisionTreeRegressor

max_depth = 5
model = DecisionTreeRegressor(max_depth=max_depth)
# --8<-- [end:model]

# --8<-- [start:fit]
model.fit(X_train, Y_train)
# --8<-- [end:fit]

# --8<-- [start:predict]
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

pred_Y = model.predict(X_test)

rmse = mean_squared_error(Y_test, pred_Y)
r2 = r2_score(Y_test, pred_Y)
print(f'RMSE arbre decissió: {rmse:.2f}')
print(f'R2 arbre decissió: {r2:.2f}')
# --8<-- [end:predict]

# --8<-- [start:plot]
import matplotlib.pyplot as plt

plt.scatter(X_train, Y_train, color='blue')
plt.scatter(X_test, Y_test, color='orange')
plt.plot(X_test, pred_Y, color='red', lw=2)
plt.show()
# --8<-- [end:plot]

# --8<-- [start:plot_tree]
from sklearn.tree import export_graphviz
from graphviz import Source

# Export the tree to a DOT format
dot_data = export_graphviz(
    model,
    out_file=None,  # Leave as None to return the DOT data as a string
    filled=True,  # Color the nodes based on their values
    rounded=True,  # Round the corners of the boxes
    special_characters=True  # Allow for special characters in labels
)

# Render the DOT data to a graph
graph = Source(dot_data)
graph.format = "png"
graph.render("decision_tree")
graph.view()  # Open the PNG file
# --8<-- [end:plot_tree]
