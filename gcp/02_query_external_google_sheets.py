from google.cloud import bigquery
from google.oauth2.service_account import Credentials

# Credential scope
GCP_CREDENTIAL_SCOPE = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/bigquery",
]

# Using credentials file
BIGQUERY_CREDENTIALS_FILE_PATH = "bigquery-user.json"
CREDENTIALS = Credentials.from_service_account_file(
    BIGQUERY_CREDENTIALS_FILE_PATH,
    scopes=GCP_CREDENTIAL_SCOPE,
)

def query_gsheets():
    client = bigquery.Client(
        credentials=CREDENTIALS,
    )
    query_job = client.query(
        """
        SELECT *
        FROM `tjr101_demo.external_gsheets`
        """
    )

    return query_job.to_dataframe()

df = query_gsheets()

print(df)
