# outputs.tf
output "dataset_id" {
  description = "ID of the created dataset"
  value       = module.bigquery.dataset_id
}

output "table_id" {
  description = "ID of the created table"
  value       = module.bigquery.table_id
}

output "service_account_emails" {
  description = "Email dei service account creati"
  value       = module.service_accounts.service_account_emails
}

output "service_account_names" {
  description = "Nomi completi delle risorse dei service account creati"
  value       = module.service_accounts.service_account_names
}
