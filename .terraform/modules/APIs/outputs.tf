output "enabled_services" {
  description = "Elenco delle API abilitate"
  value       = [for service in google_project_service.enabled_apis : service.service]
}
