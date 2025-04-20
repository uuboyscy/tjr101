from airflow.decorators import task


@task
def do_something(some_str: str) -> list[str]:
    # ["H", "E", "L", "L", "O"]
    return list(some_str)
