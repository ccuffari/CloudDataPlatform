# Main Directory Files

# main.tf
provider "google" {
  project = var.project
  region  = var.location
}

module "bigquery" {
  source      = "./modules/bigquery"
  project     = var.project
  dataset_id  = var.dataset_id
  table_id    = var.table_id
  location    = var.location
  schema_path = "modules/bigquery/schema/schema.json"
}

module "service_accounts" {
  source      = "./modules/IAM"
  project  = var.project
  service_accounts = var.service_accounts
}
