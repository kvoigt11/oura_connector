import pandas as pd

from down_from_blob import get_oura_az_blob_data
from settings import AZURE_SERVER_NAME, AZURE_DATABASE_NAME, AZURE_DATABASE_USERNAME, AZURE_DATABASE_PASSWORD
from upload_to_az_db import upload_to_azure_sql



def personal_info_blob_to_azure():
    # Select the endpoint we want
    endpoint = "personal_info"

    # Specify the target table name
    target_table = "OURA_PERSONAL_INFO"

    # Pull data azure blob storage data in pandas dataframes
    pi_df, big_df = get_oura_az_blob_data()

    # Select only data from daily_activity endpoint
    df = pi_df[pi_df['endpoint'] == endpoint]
    df = df.drop(columns = ['endpoint'], axis = 1)

    upload_to_azure_sql(
        df = df,
        table_name = target_table,
        server = AZURE_SERVER_NAME,
        database = AZURE_DATABASE_NAME,
        username = AZURE_DATABASE_USERNAME,
        password = AZURE_DATABASE_PASSWORD)


    print(f"Data from Azure Blob Storage folder {endpoint} has uploaded to Azure SQL Database!!")


