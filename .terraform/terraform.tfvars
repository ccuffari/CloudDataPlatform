# terraform.tfvars
project    = "clouddataplatform"
dataset_id = "FinancialDataset"
table_id   = "sales_data"
location   = "europe-north1"
service_accounts = {
  "data-catalog-sa-1" = {
    display_name = "Service Account for Data Catalog"
    description  = "SA utilizzato per le operazioni di Data Catalog"
  },
  "bigquery-sa-1" = {
    display_name = "Service Account for BigQuery"
    description  = "SA utilizzato per BigQuery operations"
  }
}
apis       = ["datacatalog.googleapis.com"]
