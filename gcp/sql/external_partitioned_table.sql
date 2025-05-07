-- Create partitioned external table from files in GCS
CREATE OR REPLACE EXTERNAL TABLE `<your_dataset>.SalePartitionExternal`
(
  TransactionID STRING,
  ProductID STRING,
  Quantity INT64,
  SaleDate DATE,
)
WITH PARTITION COLUMNS
OPTIONS (
  format = 'CSV',
  uris = ['gs://<your_bucket>/<external_partitioned_folder>/*'],
  hive_partition_uri_prefix = 'gs://<your_bucket>/<external_partitioned_folder>',
  skip_leading_rows = 1,
  max_bad_records = 1
);

-- Create external table from Google Sheets
CREATE OR REPLACE EXTERNAL TABLE `<your_dataset>.<your_table_name>`
OPTIONS (
  format = 'GOOGLE_SHEETS',
  skip_leading_rows = 1,
  uris = ['<your_googlesheets_url>'],
  sheet_range = '<sheet_name>!A:D'
);
