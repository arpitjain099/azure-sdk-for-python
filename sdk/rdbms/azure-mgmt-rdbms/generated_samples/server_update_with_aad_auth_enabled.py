# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.rdbms import PostgreSQLManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-rdbms
# USAGE
    python server_update_with_aad_auth_enabled.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PostgreSQLManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="ffffffff-ffff-ffff-ffff-ffffffffffff",
    )

    response = client.servers.begin_update(
        resource_group_name="TestGroup",
        server_name="pgtestsvc4",
        parameters={
            "properties": {
                "administratorLoginPassword": "newpassword",
                "authConfig": {"activeDirectoryAuthEnabled": True, "tenantId": "tttttt-tttt-tttt-tttt-tttttttttttt"},
                "backup": {"backupRetentionDays": 20},
                "createMode": "Update",
                "storage": {"storageSizeGB": 1024},
            },
            "sku": {"name": "Standard_D8s_v3", "tier": "GeneralPurpose"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/preview/2022-03-08-preview/examples/ServerUpdateWithAadAuthEnabled.json
if __name__ == "__main__":
    main()
