import pandas as pd
import pickle
from sktime.forecasting.compose import TransformedTargetForecaster
from sktime.transformations.series.detrend import Deseasonalizer
from sktime.forecasting.exp_smoothing import ExponentialSmoothing


df_h = pd.read_hdf('/home/denis/airflow/datasets/data.h5', key='data')

# уберём нулевые и резкие максимальные значения
df_h.loc[df_h['value'] > 1400, 'value'] = 1400
df_h.loc[df_h['value'] < 250, 'value'] = 250

y = df_h.value

ses = ExponentialSmoothing()

# пайплайн
forecaster = TransformedTargetForecaster(
                steps=[
                ("deseasonalize1", Deseasonalizer(model="multiplicative", sp=24)),
                ("deseasonalize2", Deseasonalizer(model="multiplicative", sp=24*7)),
                ("forecaster", ses),
                ])
forecaster.fit(y)

with open("/home/denis/airflow/models/model.pkl", "wb") as f:
    pickle.dump(forecaster, f)
