from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

# Чтение данных из CSV-файла в объект DataFrame
df = pd.read_csv('/home/denis/airflow/datasets/data_test.csv', header=None)
df.columns = ['id', 'counts']

# Создание модели и загрузка 
model = LinearRegression()
with open('/home/denis/airflow/models/data.pickle', 'rb') as f:
    model = pickle.load(f)

# Вычисление и вывод оценки
score = model.score(df['id'].values.reshape(-1,1), df['counts'])
print("score=", score)

