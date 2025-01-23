variable "project" {
  description = "ID del progetto GCP in cui creare i service account"
  type        = string
}

variable "service_accounts" {
  description = "Mappa dei service account da creare, con i dettagli del display_name e della descrizione"
  type = map(object({
    display_name = string
    description  = string
  }))
}
