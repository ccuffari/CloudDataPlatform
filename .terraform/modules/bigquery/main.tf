# modules/bigquery/main.tf
resource "google_bigquery_dataset" "dataset" {
  project   = var.project
  dataset_id = var.dataset_id
  location  = var.location
}

resource "google_bigquery_table" "table" {
  project      = var.project
  dataset_id   = google_bigquery_dataset.dataset.dataset_id
  table_id     = var.table_id
  schema       = file(var.schema_path)
}