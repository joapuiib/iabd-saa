#!/usr/bin/env python

# --8<-- [start:dades]
import pandas as pd
import numpy as np

Y = pd.Series([50, 60, 70, 80])
pred_Y = pd.Series([52, 58, 68, 85])
# --8<-- [end:dades]

# --8<-- [start:mae_pandas]
mae = np.abs(Y - pred_Y).mean()
print(f'MAE with pandas: {mae:.2f}')
# --8<-- [end:mae_pandas]

# --8<-- [start:mae_sklearn]
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(Y, pred_Y)
print(f'MAE with sklearn: {mae:.2f}')
# --8<-- [end:mae_sklearn]

# --8<-- [start:mse_pandas]
mse = ((Y - pred_Y) ** 2).mean()
print(f'MSE with pandas: {mse:.2f}')
# --8<-- [end:mse_pandas]

# --8<-- [start:mse_sklearn]
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y, pred_Y)
print(f'MSE with sklearn: {mse:.2f}')
# --8<-- [end:mse_sklearn]

# --8<-- [start:rmse_pandas]
rmse = np.sqrt(((Y - pred_Y) ** 2).mean())
print(f'RMSE with pandas: {rmse:.2f}')
# --8<-- [end:rmse_pandas]

# --8<-- [start:rmse_sklearn]
from sklearn.metrics import root_mean_squared_error

rmse = root_mean_squared_error(Y, pred_Y)
print(f'RMSE with sklearn: {rmse:.2f}')
# --8<-- [end:rmse_sklearn]

# --8<-- [start:r2_pandas]
r2 = 1 - ((Y - pred_Y) ** 2).sum() / ((Y - Y.mean()) ** 2).sum()
print(f'R^2 with pandas: {r2:.2f}')
# --8<-- [end:r2_pandas]

# --8<-- [start:r2_sklearn]
from sklearn.metrics import r2_score

r2 = r2_score(Y, pred_Y)
print(f'R^2 with sklearn: {r2:.2f}')
# --8<-- [end:r2_sklearn]
