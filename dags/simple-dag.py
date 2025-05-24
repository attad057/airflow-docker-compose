from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time


def wait_function():
    print("Waiting for 60 seconds...")
    time.sleep(60)
    print("Done waiting!")

# Define default_args for the DAG (e.g., retry settings, start date, etc.)
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 3, 27),
}

# Define the DAG
dag = DAG(
    'simple_dag',  # DAG name
    default_args=default_args,
    description='A simple DAG that prints a message and waits',
    schedule_interval=timedelta(days=1),  # Run once a day
    catchup=False,  # Prevents backfilling (e.g., no tasks will be run for past dates)
)

# Define tasks
task_1 = PythonOperator(
    task_id='print_hello_task',
    python_callable=lambda: print("Hello, Airflow!"),
    dag=dag,
)

task_2 = PythonOperator(
    task_id='wait_task',
    python_callable=wait_function,
    dag=dag,
    provide_context=True,  # Optionally provide context for accessing DAG parameters
)

task_3 = PythonOperator(
    task_id='print_wait_complete_task',
    python_callable=lambda: print("Wait complete!"),
    dag=dag,
)
# Set task dependencies (task_2 will run after task_1, task_3 will run after task_2)
task_1 >> task_2 >> task_3