# modules/bigquery/outputs.tf
output "dataset_id" {
  description = "ID of the created dataset"
  value       = google_bigquery_dataset.dataset.dataset_id
}

output "table_id" {
  description = "ID of the created table"
  value       = google_bigquery_table.table.table_id
}