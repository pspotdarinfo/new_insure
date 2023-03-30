
import pandas as pd

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)


# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.
connect_str = "DefaultEndpointsProtocol=https;AccountName=mlopspjj1amlsa;AccountKey=GVD+fwn1UV0H77torlkpiVpwUcrg358pYfh7aITYHSwZ6ul5GEV9Rpzt7XgbSbU6QB3FXdPIM+2w+AStxT/oNQ==;EndpointSuffix=core.windows.net"


# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)


# Create a unique name for the container
container_name = "azureml-blobstore-86385659-9fa2-4c25-a47c-fc76e1e53174"

# Create the container
#container_client = blob_service_client.create_container(container_name)

#download csv file from Azure Storage
from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str= connect_str, container_name= container_name, blob_name="insurance/insurance.csv")

with open("./insurance.csv", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)


df = pd.read_csv("./insurance.csv")



# Add Preprocessing Code



# End of Preprocessing Code

df.to_csv('preproc_insurance.csv',index=False)

#Upload preprocessed csv file

from azure.storage.blob import BlobClient

blob = BlobClient.from_connection_string(conn_str= connect_str, container_name= container_name, blob_name="insurance/preproc_insurance.csv")

with open("./preproc_insurance.csv", "rb") as data:
    blob.upload_blob(data, overwrite=True)


