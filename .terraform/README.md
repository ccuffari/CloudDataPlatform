<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_bigquery"></a> [bigquery](#module\_bigquery) | ./modules/bigquery | n/a |
| <a name="module_enable_apis"></a> [enable\_apis](#module\_enable\_apis) | ./modules/apis | n/a |
| <a name="module_service_accounts"></a> [service\_accounts](#module\_service\_accounts) | ./modules/IAM | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_apis"></a> [apis](#input\_apis) | Elenco delle API da abilitare | `set(string)` | <pre>[<br/>  "datacatalog.googleapis.com"<br/>]</pre> | no |
| <a name="input_dataset_id"></a> [dataset\_id](#input\_dataset\_id) | BigQuery dataset ID | `string` | n/a | yes |
| <a name="input_location"></a> [location](#input\_location) | BigQuery dataset location | `string` | `"europe-north1"` | no |
| <a name="input_project"></a> [project](#input\_project) | GCP project ID | `string` | n/a | yes |
| <a name="input_service_accounts"></a> [service\_accounts](#input\_service\_accounts) | Mappa dei service account da creare, con i dettagli del display\_name e della descrizione | <pre>map(object({<br/>    display_name = string<br/>    description  = string<br/>  }))</pre> | n/a | yes |
| <a name="input_table_id"></a> [table\_id](#input\_table\_id) | BigQuery table ID | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_bigquery_dataset_ids"></a> [bigquery\_dataset\_ids](#output\_bigquery\_dataset\_ids) | n/a |
| <a name="output_dataset_id"></a> [dataset\_id](#output\_dataset\_id) | ID of the created dataset |
| <a name="output_enabled_apis"></a> [enabled\_apis](#output\_enabled\_apis) | Elenco delle API abilitate nel progetto |
| <a name="output_service_account_emails"></a> [service\_account\_emails](#output\_service\_account\_emails) | Email dei service account creati |
| <a name="output_service_account_names"></a> [service\_account\_names](#output\_service\_account\_names) | Nomi completi delle risorse dei service account creati |
| <a name="output_table_id"></a> [table\_id](#output\_table\_id) | ID of the created table |
<!-- END_TF_DOCS -->