# Azure subscription vars
subscription_id = "{{env `ARM_SUBSCRIPTION_ID`}}"
client_id = "{{env `ARM_CLIENT_ID`}}"
client_secret = "{{env `ARM_CLIENT_SECRET`}}"
tenant_id = "{{env `ARM_TENANT_ID`}}"

# Resource Group/Location
location = "East US"
resource_group_name = "Azuredevops"
application_type = "myApplication"

# Storage account
storage_account_name = "{{env `ARM_STORAGE_ACCOUNT_NAME`}}"
container_name       = "{{env `ARM_CONTAINER_NAME`}}"
key                  = "test.terraform.tfstate"
access_key           = "{{env `ARM_ACCOUNT_KEY`}}"

# Network
virtual_network_name = ""
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"
