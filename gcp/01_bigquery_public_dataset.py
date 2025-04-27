from google.cloud import bigquery
from google.oauth2.service_account import Credentials

# Using credentials file
BIGQUERY_CREDENTIALS_FILE_PATH = "bigquery-user.json"
CREDENTIALS = Credentials.from_service_account_file(BIGQUERY_CREDENTIALS_FILE_PATH)

def query_stackoverflow():
    client = bigquery.Client(
        credentials=CREDENTIALS,
    )
    query_job = client.query(
        """
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10"""
    )

    # results = query_job.result()  # Waits for job to complete.

    # for row in results:
    #     # print("{} : {} views".format(row.url, row.view_count))
    #     print(row)

    result_df = query_job.to_dataframe()

    print(result_df)


if __name__ == "__main__":
    query_stackoverflow()
