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
| [google_service_account.service_accounts](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/service_account) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_project"></a> [project](#input\_project) | ID del progetto GCP in cui creare i service account | `string` | n/a | yes |
| <a name="input_service_accounts"></a> [service\_accounts](#input\_service\_accounts) | Mappa dei service account da creare, con i dettagli del display\_name e della descrizione | <pre>map(object({<br/>    display_name = string<br/>    description  = string<br/>  }))</pre> | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_service_account_emails"></a> [service\_account\_emails](#output\_service\_account\_emails) | Email dei service account creati |
| <a name="output_service_account_names"></a> [service\_account\_names](#output\_service\_account\_names) | Nomi completi delle risorse dei service account creati |
<!-- END_TF_DOCS -->