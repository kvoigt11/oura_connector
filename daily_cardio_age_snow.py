import pandas as pd

from down_from_blob import get_oura_az_blob_data
from snowflake.snowpark import Session
from settings import connection_parameters



def daily_cardio_age_blob_to_snowflake():
    # Select the endpoint we want
    endpoint = "daily_cardiovascular_age"

    # Specify the target table name
    target_table = "OURA_DAILY_CARDIOVASCULAR_AGE"

    # Create a Snowpark session
    session = Session.builder.configs(connection_parameters).create()

    # Pull data azure blob storage data in pandas dataframes
    pi_df, big_df = get_oura_az_blob_data()

    # Select only data from daily_activity endpoint
    df = big_df[big_df['endpoint'] == endpoint]
    df = df.drop(columns = ['endpoint'], axis = 1)

    # Loop through each row and create dataframes
    big_list = []
    for i in range(len(df)):
        indi_df = df['data'][i]
        indi_df = pd.DataFrame(indi_df, index = [i])
        indi_df = indi_df.reset_index(drop = True)

        big_list.append(indi_df)

    # Concatenate all of these individual rows together into one dataframe
    next_df = pd.concat(big_list)
    final_df = next_df.reset_index(drop = True)

    # Convert Pandas DataFrame to Snowpark DataFrame
    snowpark_df = session.create_dataframe(final_df)

    # Write the DataFrame to the Snowflake table
    snowpark_df.write.mode("overwrite").save_as_table(target_table)

    print(f"Data from Azure Blob Storage folder {endpoint} has uploaded to Snowflake!")

    session.close()

