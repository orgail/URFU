import pandas as pd


df = pd.read_csv('/home/denis/airflow/datasets/data.csv', header=None)

# Нормализация данных 
df[0] = (df[0]-df[0].min())/(df[0].max()-df[0].min())
 
# Запись обработанных данных и перебор значений
with open('/home/denis/airflow/datasets/data_processed.csv', 'w') as f:
    for i, item in enumerate(df[0].values):
        f.write("{},{}\n".format(i, item))

