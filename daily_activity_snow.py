import pandas as pd

from down_from_blob import get_oura_az_blob_data
from snow_conn import create_snow_conn


endpoint = "daily_activity"


# Bring in snowflake connector
snow_engine = create_snow_conn()

# Create connection to snowflake database
connection = snow_engine.connect()

# Pull data azure blob storage data in pandas dataframes
pi_df, big_df = get_oura_az_blob_data()

# Select only data from daily_activity endpoint
df = big_df[big_df['endpoint'] == endpoint]

print(df)

connection.close()

# # Get unique endpoints
# endpoint_list = big_df['endpoint'].unique().tolist()

# # Loop through each unique endpoint to create a unique dataframe for each
# for endpoint in endpoint_list:
#     endpoint_df = big_df[big_df['endpoint'] == endpoint]

#     if endpoint != 'personal_info':
#         endpoint_df = endpoint_df[['data', 'endpoint']]

#     else:
#         endpoint_df = endpoint_df.drop(columns = ['data'], axis = 1)

#     print(endpoint_df)