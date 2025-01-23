<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_google"></a> [google](#provider\_google) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [google_bigquery_dataset.dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset) | resource |
| [google_bigquery_table.table](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_dataset_id"></a> [dataset\_id](#input\_dataset\_id) | BigQuery dataset ID | `string` | n/a | yes |
| <a name="input_location"></a> [location](#input\_location) | BigQuery dataset location | `string` | n/a | yes |
| <a name="input_project"></a> [project](#input\_project) | GCP project ID | `string` | n/a | yes |
| <a name="input_schema_path"></a> [schema\_path](#input\_schema\_path) | Path to the JSON schema file | `string` | n/a | yes |
| <a name="input_table_id"></a> [table\_id](#input\_table\_id) | BigQuery table ID | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_dataset_id"></a> [dataset\_id](#output\_dataset\_id) | ID of the created dataset |
| <a name="output_table_id"></a> [table\_id](#output\_table\_id) | ID of the created table |
<!-- END_TF_DOCS -->