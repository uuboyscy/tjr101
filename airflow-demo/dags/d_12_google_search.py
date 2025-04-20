import pendulum
from datetime import datetime, timedelta
from airflow.decorators import dag, task, bash_task


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["your_email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

# Define the DAG
@dag(
    schedule="*/2 * * * *",
    default_args=default_args,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["google_search"],
)
def d_12_google_search():
    @task
    def e_google_search_comment() -> str:
        return "Some HTML"

    e_google_search_comment()

d_12_google_search()
