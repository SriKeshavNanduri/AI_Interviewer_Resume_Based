import os
from dotenv import load_dotenv 
from azure.storage.blob import BlobServiceClient

load_dotenv()

def connect_blob(blob_name,container_name , connection_string):

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_container_client(container_name).get_blob_client(blob_name)
    
    return blob_client