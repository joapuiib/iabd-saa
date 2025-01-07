#!/usr/bin/env python

# --8<-- [start:dades]
import numpy as np
from sklearn.model_selection import train_test_split

def f(x):
    return -100 - 5*x + 5*np.power(x, 2) + 0.1*np.power(x, 3)

np.random.seed(42)
n_samples = 100

X = np.random.uniform(-50, 50, n_samples)
Y = f(X) + np.random.randn(n_samples)*1000
X = X.reshape(-1, 1) # Convertim X en una matriu de 1 columna

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_test, Y_test = zip(*sorted(zip(X_test, Y_test))) # Ordenem les dades de test per visualitzar-les correctament
# --8<-- [end:dades]

# --8<-- [start:plot_lineal]
import matplotlib.pyplot as plt

plt.scatter(X_train, Y_train, color='blue')
plt.scatter(X_test, Y_test, color='orange')
plt.show()
# --8<-- [end:plot_lineal]

# --8<-- [start:regressio_lineal]
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

model = LinearRegression()
model.fit(X_train, Y_train)

pred_Y = model.predict(X_test)

rmse = mean_squared_error(Y_test, pred_Y)
r2 = r2_score(Y_test, pred_Y)
print(f'RMSE linear: {rmse:.2f}')
print(f'R^2 linear: {r2:.2f}')
# --8<-- [end:regressio_lineal]

# --8<-- [start:plot_lineal]
plt.scatter(X_train, Y_train, color='blue')
plt.scatter(X_test, Y_test, color='orange')
plt.plot(X_test, pred_Y, color='red')
plt.show()
# --8<-- [end:plot_lineal]

# --8<-- [start:model]
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

degree = 3
polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
model = make_pipeline(polynomial_features, LinearRegression())
# --8<-- [end:model]

# --8<-- [start:fit]
model.fit(X_train, Y_train)
# --8<-- [end:fit]


# --8<-- [start:params]
print(f'Coeficients: {model.named_steps["linearregression"].coef_}')
print(f'Intercept: {model.named_steps["linearregression"].intercept_}')
# --8<-- [end:params]

# --8<-- [start:predict]
pred_Y = model.predict(X_test)

rmse = mean_squared_error(Y_test, pred_Y)
r2 = r2_score(Y_test, pred_Y)
print(f'RMSE polinòmica: {rmse:.2f}')
print(f'R^2 polinòmica: {r2:.2f}')
# --8<-- [end:predict]

# --8<-- [start:plot_polinomica], pred_Y)
plt.scatter(X_train, Y_train, color='blue')
plt.scatter(X_test, Y_test, color='orange')
plt.plot(X_test, pred_Y, color='red')
plt.show()
# --8<-- [end:plot_polinomica]