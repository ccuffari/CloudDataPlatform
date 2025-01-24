variable "project" {
  description = "ID del progetto GCP"
  type        = string
}

variable "apis" {
  description = "Elenco delle API da abilitare"
  type        = set(string)
  default     = ["datacatalog.googleapis.com"]
}
