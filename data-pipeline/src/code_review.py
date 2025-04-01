df.to_sql(
    name="Staff",
    con=conn,
    schema="TESTDB",
    if_exists="append",
    index=False,
    test=123,
)
