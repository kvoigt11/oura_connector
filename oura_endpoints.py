import requests
import pandas as pd
import json

from settings import headers, OURA_URL, COLLECTION_URL
from settings import response_endpoints_list
from upload_to_blob import upload_to_blob_storage
from settings import set_simple_params


def pull_oura_endpoints(start_date, end_date):
    # Set simple parameters with the date range we want
    simple_params = set_simple_params(start_date, end_date)

    # Run each response type through this API endpoint structure
    for response_needs in response_endpoints_list:
        print(f"Running {response_needs}")

        response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers, params = simple_params)

        json_response = response.json()

        upload_to_blob_storage(response_needs = response_needs,
                            json_data = json_response,
                            start_date = start_date,
                            end_date = end_date)
    
    print("All endpoints listed have been successfully uploaded to Azure Blob Storage!")
