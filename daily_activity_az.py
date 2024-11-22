import pandas as pd

from down_from_blob import get_oura_az_blob_data
from settings import AZURE_SERVER_NAME, AZURE_DATABASE_NAME, AZURE_DATABASE_USERNAME, AZURE_DATABASE_PASSWORD
from upload_to_az_db import upload_to_azure_sql



def daily_activity_blob_to_azure():
    # Select the endpoint we want
    endpoint = "daily_activity"

    # Specify the target table name
    target_table = "OURA_DAILY_ACTIVITY"

    # Pull data azure blob storage data in pandas dataframes
    pi_df, big_df = get_oura_az_blob_data()

    # Select only data from daily_activity endpoint
    df = big_df[big_df['endpoint'] == endpoint]
    df = df.drop(columns = ['endpoint'], axis = 1)

    # Loop through each row and create dataframes
    big_list = []
    for i in range(len(df)):
        indi_df = df['data'][i]
        indi_df = pd.DataFrame(indi_df)
        indi_df = indi_df.reset_index(drop = True)

        big_list.append(indi_df)

    # Concatenate all of these individual rows together into one dataframe
    next_df = pd.concat(big_list)

    next_df = next_df.reset_index(drop = True)
    final_df = next_df.drop(columns = ['met'], axis = 1)

    # Works
    upload_to_azure_sql(
        df = final_df,
        table_name = target_table,
        server = AZURE_SERVER_NAME,
        database = AZURE_DATABASE_NAME,
        username = AZURE_DATABASE_USERNAME,
        password = AZURE_DATABASE_PASSWORD)
    

    print(f"Data from Azure Blob Storage folder {endpoint} has uploaded to Azure SQL Database!")


daily_activity_blob_to_azure()