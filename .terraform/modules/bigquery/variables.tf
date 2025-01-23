# modules/bigquery/variables.tf
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
}

variable "schema_path" {
  description = "Path to the JSON schema file"
  type        = string
}