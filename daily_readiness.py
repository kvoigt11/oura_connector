import requests
import pandas as pd
from settings import headers, OURA_URL, COLLECTION_URL

start_date = '2020-01-01'
end_date = '2024-10-31'

params = {f'q': 'requests+language:python',
          'start_date': {start_date},
          'end_date': {end_date}}

response_needs = "daily_readiness"

response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers, params=params)

json_response = response.json()
df = pd.DataFrame(json_response)
df = df.drop(columns = ['next_token'], axis = 1)

df = pd.DataFrame(df['data'])

main_metrics_list = []
for i in range(0, len(df)):
    data_df = pd.DataFrame(df['data'][i], index = [i])

    # Drop these columns for now:
    drop_one_df = data_df.drop(columns = ['contributors'], axis = 1)
    
    main_metrics_list.append(drop_one_df)

main_metrics_df = pd.concat(main_metrics_list)

main_metrics_df = main_metrics_df.rename(columns = {'id': 'readiness_id',
                                                    'score': 'readiness_score',
                                                    'day': 'activity_date',
                                                    'timestamp': 'activity_timestamp'})

print(main_metrics_df)

for col in main_metrics_df.columns:
    print(col)

# print(main_metrics_df)