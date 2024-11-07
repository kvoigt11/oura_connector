import pandas as pd

from down_from_blob import get_oura_az_blob_data
from snowflake.snowpark import Session
from settings import connection_parameters



def personal_info_blob_to_snowflake():
    # Select the endpoint we want
    endpoint = "personal_info"

    # Specify the target table name
    target_table = "OURA_PERSONAL_INFO"

    # Create a Snowpark session
    session = Session.builder.configs(connection_parameters).create()

    # Pull data azure blob storage data in pandas dataframes
    pi_df, big_df = get_oura_az_blob_data()

    # Select only data from daily_activity endpoint
    df = pi_df[pi_df['endpoint'] == endpoint]
    df = df.drop(columns = ['endpoint'], axis = 1)

    # Convert Pandas DataFrame to Snowpark DataFrame
    snowpark_df = session.create_dataframe(df)

    # Write the DataFrame to the Snowflake table
    snowpark_df.write.mode("overwrite").save_as_table(target_table)

    print(f"Data from Azure Blob Storage folder {endpoint} has uploaded to Snowflake!")

    session.close()

