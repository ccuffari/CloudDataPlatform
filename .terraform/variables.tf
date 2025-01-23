# variables.tf
variable "project" {
  description = "GCP project ID"
  type        = string
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
}

variable "table_id" {
  description = "BigQuery table ID"
  type        = string
}

variable "location" {
  description = "BigQuery dataset location"
  type        = string
  default     = "europe-north1"
}


variable "project" {
  description = "GCP project ID"
  type        = string
}

variable "location" {
  description = "GCP resource location"
  type        = string
  default     = "us-central1"
}

variable "service_accounts" {
  description = "Mappa dei service account da creare, con i dettagli del display_name e della descrizione"
  type = map(object({
    display_name = string
    description  = string
  }))
}
