import pandas as pd
from sktime.forecasting.model_selection import temporal_train_test_split


df_h = pd.read_hdf('/home/denis/airflow/datasets/data.h5', key='data')

y = df_h.value

TEST_SIZE = int(0.45*y.size)

y_train, y_test = temporal_train_test_split(y, test_size=TEST_SIZE)

# Сохраняем обработанные данные
y_train.to_hdf('/home/denis/airflow/datasets/train.h5', key='data', mode='w', format='table', data_columns=True)
y_test.to_hdf('/home/denis/airflow/datasets/test.h5', key='data', mode='w', format='table', data_columns=True)

