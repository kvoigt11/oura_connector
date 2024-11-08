import json

from settings import AZ_KEY1_CONNECTION_STRING, AZ_CONTAINER_NAME
from azure.storage.blob import BlobServiceClient, ContentSettings
from datetime import date


def upload_to_blob_storage(response_needs, json_data, folder_path, start_date, end_date):
    # Create blob service client
    blob_service_client = BlobServiceClient.from_connection_string(AZ_KEY1_CONNECTION_STRING)

    # Get container client
    container_client = blob_service_client.get_container_client(AZ_CONTAINER_NAME)

    # Generate blob name (file path in container)
    blob_name = f"{folder_path}/{response_needs}/kv_oura_{response_needs}_data.json"

    # Get blob client
    blob_client = container_client.get_blob_client(blob_name)

    # Convert JSON to string
    json_string = json.dumps(json_data)

    # Upload the JSON data
    blob_client.upload_blob(
        json_string,
        overwrite = True,
        content_settings = ContentSettings(content_type='application/json')
    )

    print("Upload successful!")

