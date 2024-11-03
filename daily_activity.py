import requests
import pandas as pd
import json

from settings import headers, OURA_URL, COLLECTION_URL
from settings import simple_params, AZ_FOLDER_PATH
from upload_to_blob import upload_to_blob_storage



response_needs = "daily_activity"

response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers, params = simple_params)

json_response = response.json()

upload_to_blob_storage(response_needs = response_needs,
                       json_data = json_response,
                       folder_path = AZ_FOLDER_PATH)

# # Write JSON data to a file
# with open(f"kv_oura_{response_needs}_data_{today}.json", "w") as outfile:
#     json.dump(json_response, outfile)


# df = pd.DataFrame(json_response)
# df = df.drop(columns = ['next_token'], axis = 1)

# df = pd.DataFrame(df['data'])

# main_metrics_list = []
# for i in range(0, len(df)):
#     data_df = pd.DataFrame(df['data'][i], index = [i])

#     # Drop these columns for now:
#     drop_one_df = data_df.drop(columns = ['class_5_min',
#                                           'contributors',
#                                           'met'], axis = 1)
    
#     main_metrics_list.append(drop_one_df)

# main_metrics_df = pd.concat(main_metrics_list)

# main_metrics_df = main_metrics_df.rename(columns = {'id': 'activity_id',
#                                                     'score': 'activity_score',
#                                                     'steps': 'total_steps',
#                                                     'day': 'activity_date',
#                                                     'timestamp': 'activity_timestamp'})

# for col in main_metrics_df.columns:
#     print(col)

# print(main_metrics_df)