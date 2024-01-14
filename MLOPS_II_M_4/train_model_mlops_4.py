# Импорт модулей
from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime as dt

# Определение базовых аргументов для DAG
args = {
    "owner": "admin",
    "start_date": dt.datetime(2024, 1, 14),
    "retries": 1,
    "retry_delays": dt.timedelta(minutes=1),
    "depends_on_past": False
}


# Создание DAG 
with DAG(
    dag_id='Twitter_AMZN',
    default_args=args,
    schedule='*/5 * * * *',
    tags=['Twitter', 'AMZN'],
) as dag:
    tfs_data = BashOperator(task_id='tfs_data',
                            bash_command="cp /home/denis/airflow/tfs_data/Twitter_volume_AMZN.csv /home/denis/airflow/datasets/Twitter_volume_AMZN.csv -f",
                            dag=dag)
    get_data = BashOperator(task_id='get_data',
                            bash_command="python3 /home/denis/airflow/scripts/get_data.py",
                            dag=dag)
    train_test_split_data = BashOperator(task_id='train_test_split_data',
                            bash_command="python3 /home/denis/airflow/scripts/train_test_split.py",
                            dag=dag)
    tfs_reserch = BashOperator(task_id='tfs_reserch',
                            bash_command="cp /home/denis/airflow/datasets/train.h5 /home/denis/airflow/tfs_reserch/train.h5 -f && cp /home/denis/airflow/datasets/test.h5 /home/denis/airflow/tfs_reserch/test.h5 -f",
                            dag=dag)
    train_model = BashOperator(task_id='train_model',
                            bash_command="python3 /home/denis/airflow/scripts/model_save.py",
                            dag=dag)
    tfs_pred = BashOperator(task_id='tfs_pred',
                            bash_command="cp /home/denis/airflow/models/model.pkl /home/denis/airflow/tfs_pred/model.pkl",
                            dag=dag) 

    tfs_data >> get_data >> train_test_split_data >> tfs_reserch >> train_model >> tfs_pred

