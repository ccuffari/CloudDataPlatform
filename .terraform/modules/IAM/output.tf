output "service_account_emails" {
  description = "Email dei service account creati"
  value       = { for key, account in google_service_account.service_accounts : key => account.email }
}

output "service_account_names" {
  description = "Nomi completi delle risorse dei service account creati"
  value       = { for key, account in google_service_account.service_accounts : key => account.name }
}
