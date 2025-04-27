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
