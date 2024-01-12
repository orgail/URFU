# Импорт библиотек
import pandas as pd
import numpy as np

# Чтение данных из CSV-файла в объект DataFrame 
df = pd.read_csv('/home/denis/airflow/datasets/data_processed.csv', header=None)

# Работа с индексами
idxs = np.array(df.index.values)
np.random.shuffle(idxs)
l = int(len(df)*0.7)
train_idxs = idxs[:l]
test_idxs = idxs[l+1:]

# Запись обучающей выборки в CSV-файл
df.loc[train_idxs, :].to_csv('/home/denis/airflow/datasets/data_train.csv',
                        header=None,
                        index=None)

# Запись тестовой выборки в CSV-файл
df.loc[test_idxs, :].to_csv('/home/denis/airflow/datasets/data_test.csv',
                        header=None,
                        index=None)

