# import subprocess
from airflow.models import dag
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from gen_daily import mockCurrentDates
from append_to_sql import append

# import pendulum
# import pytz

# tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
# timezone = pendulum.timezone(tz)
# timezone = pendulum.timezone(offset=4)


default_arg = {
    'owner' : 'OM',
    'depends_on_past' : False,
    'start_date' : datetime(2024,3,14),
    'retries' : 3,
    'retry_delay' : timedelta(minutes=1)
}


dag = DAG(
    'retail_dag',
    default_args = default_arg,
    description = 'my retail pipe',
    schedule_interval=timedelta(days=1)
)

run1 = PythonOperator(
    task_id = 'creating todays data',
    python_callable = mockCurrentDates,
    dag = dag
)

run2 = PythonOperator(
    task_id = 'inserting data into sql',
    python_callable = append,
    dag = dag
)
run1 >> run2

