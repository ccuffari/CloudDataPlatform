# terraform.tfvars
project    = "clouddataplatform"
dataset_id = "FinancialDataset"
table_id   = "sales_data"
location   = "europe-north1"
service_accounts = {
  "bigquery-sa" = {
    display_name = "Service Account for BigQuery"
    description  = "SA utilizzato per BigQuery operations"
  }
}
apis       = ["datacatalog.googleapis.com"]
