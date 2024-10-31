import requests
import pandas as pd
from settings import headers, OURA_URL, COLLECTION_URL


### Don't use this much! ###

start_date = '2020-01-01'
end_date = '2024-10-31'

params = {f'q': 'requests+language:python',
          'start_date': {start_date},
          'end_date': {end_date}}

response_needs = "enhanced_tag"

response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers, params=params)

json_response = response.json()
df = pd.DataFrame(json_response)
df = df.drop(columns = ['next_token'], axis = 1)

df = pd.DataFrame(df['data'])

main_metrics_list = []
for i in range(0, len(df)):
    data_df = pd.DataFrame(df['data'][i], index = [i])
    
    main_metrics_list.append(data_df)

main_metrics_df = pd.concat(main_metrics_list)

# main_metrics_df = main_metrics_df.rename(columns = {'id': 'stress_id',
#                                                     'day': 'activity_date'})

print(main_metrics_df)

# for col in main_metrics_df.columns:
#     print(col)

# print(main_metrics_df)