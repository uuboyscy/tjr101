"""
Utilities to deal with Google Sheets
https://github.com/uuboyscy/ubPython/blob/master/gcp/sample_07_gsheets_utils.py
"""
import pandas as pd
import pygsheets
from pygsheets.client import Client

BIGQUERY_CREDENTIALS_FILE_PATH = "bigquery-user.json"


def get_google_sheet_client() -> Client:
    """Get Google Sheets client."""
    with open(BIGQUERY_CREDENTIALS_FILE_PATH, "r") as f:
        service_account_json_str = f.read()
    return pygsheets.authorize(
        service_account_json=service_account_json_str,
    )

def get_gsheet_as_df(gsheet_url: str, worksheet_title: str | None = None) -> pd.DataFrame:
    """Return DataFrame from a specified Google Sheets worksheet."""
    gc = get_google_sheet_client()
    sheet = gc.open_by_url(gsheet_url)
    if worksheet_title:
        return sheet.worksheet_by_title(worksheet_title).get_as_df(numerize=False)
    return sheet.sheet1.get_as_df(numerize=False)


gsheets_url = "https://docs.google.com/spreadsheets/d/1IwUX-U2MQ1w3y7_C7hCCPZiTHQ4hXVWBhwT0ZvM_v0I"

df = get_gsheet_as_df(
    gsheet_url=gsheets_url,
    worksheet_title="Sheet1",
)

print(df)
