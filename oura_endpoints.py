import requests
import pandas as pd
import json

from settings import headers, OURA_URL, COLLECTION_URL
from settings import simple_params, AZ_FOLDER_PATH
from settings import response_endpoints_list
from upload_to_blob import upload_to_blob_storage



def pull_oura_endpoints(response_endpoints_list):

    for response_needs in response_endpoints_list:
        print(f"Running {response_needs}")

        response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers, params = simple_params)

        json_response = response.json()

        upload_to_blob_storage(response_needs = response_needs,
                            json_data = json_response,
                            folder_path = AZ_FOLDER_PATH)
        
        
    
    print("All endpoints listed have been successfully uploaded to Azure Blob Storage!")