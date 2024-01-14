import pandas as pd
from sktime.forecasting.model_selection import temporal_train_test_split


data = pd.read_csv('/home/denis/airflow/datasets/Twitter_volume_AMZN.csv', index_col='timestamp', parse_dates=True)
# Для удобства работы добавим колонки дата и час
data['date'] = pd.to_datetime(data.index).date
data['h'] = pd.to_datetime(data.index).hour

# формируем датасет с почасовой группировкой
numeric_df = data.select_dtypes(include=['number'])
df_h = numeric_df.groupby(pd.Grouper(freq='1h')).sum()
df_h.drop(df_h.tail(1).index, inplace=True)
df_h.drop(df_h.head(1).index, inplace=True)

df_h.value = df_h.value.astype('float')

df_h.to_hdf('/home/denis/airflow/datasets/data.h5', key='data', mode='w', format='table', data_columns=True)
