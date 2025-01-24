terraform {
  backend "gcs" {
    bucket  = " terraform-state-cfc"
    prefix  = "terraform/state"
    project = "clouddataplatform"
  }
}
