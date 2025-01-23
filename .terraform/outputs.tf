# outputs.tf
output "dataset_id" {
  description = "ID of the created dataset"
  value       = module.bigquery.dataset_id
}

output "table_id" {
  description = "ID of the created table"
  value       = module.bigquery.table_id
}