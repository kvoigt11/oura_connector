import pandas as pd
import io
import json

from settings import AZ_KEY1_CONNECTION_STRING, AZ_CONTAINER_NAME
from settings import response_endpoints_list
from azure.storage.blob import BlobServiceClient, ContentSettings



def get_oura_az_blob_data():
    ### Get data from Azure Blob Storage ###
    blob_service_client = BlobServiceClient.from_connection_string(AZ_KEY1_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(AZ_CONTAINER_NAME)

    df_list = []
    # Loop through the blobs in the container
    for blob in container_client.list_blobs():
        blob_name = blob.name
        
        # Extract the folder name from the blob path
        folder_name = blob_name.split('/')[2]

        # Download the blob data
        blob_client = container_client.get_blob_client(blob=blob_name)
        blob_data = blob_client.download_blob().readall()
        
        # Load the data into a pandas DataFrame
        if folder_name == 'personal_info':
            # Decode the byte string to a JSON string
            json_str = blob_data.decode('utf-8')

            # Convert the JSON string to a dictionary
            df = json.loads(json_str)

            # # Convert the dictionary to a DataFrame
            df = pd.DataFrame([df])

        else:
            df = pd.read_json(io.BytesIO(blob_data))
        
        # Create endpoint column for sorting
        df['endpoint'] = folder_name
        
        # Append to list for comprehension
        df_list.append(df)

    # Concatenate list in pandas dataframe
    big_df = pd.concat(df_list)

    # Drop next_token column
    big_df = big_df.drop(columns = ['next_token'], axis = 1)

    # Pull out personal_info endpoint df
    pi_df = big_df[big_df['endpoint'] == 'personal_info']
    pi_df = pi_df.drop(columns = ['data'], axis = 1)

    # Remove personal_info endpoint from big_df
    big_df = big_df[big_df['endpoint'] != 'personal_info']
    big_df = big_df[['data', 'endpoint']]

    return pi_df, big_df


