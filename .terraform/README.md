<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_bigquery"></a> [bigquery](#module\_bigquery) | ./modules/bigquery | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_dataset_id"></a> [dataset\_id](#input\_dataset\_id) | BigQuery dataset ID | `string` | n/a | yes |
| <a name="input_location"></a> [location](#input\_location) | BigQuery dataset location | `string` | `"europe-north1"` | no |
| <a name="input_project"></a> [project](#input\_project) | GCP project ID | `string` | n/a | yes |
| <a name="input_table_id"></a> [table\_id](#input\_table\_id) | BigQuery table ID | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_dataset_id"></a> [dataset\_id](#output\_dataset\_id) | ID of the created dataset |
| <a name="output_table_id"></a> [table\_id](#output\_table\_id) | ID of the created table |
<!-- END_TF_DOCS -->