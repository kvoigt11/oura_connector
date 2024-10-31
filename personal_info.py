import requests
import pandas as pd
from settings import headers, OURA_URL, COLLECTION_URL



response_needs = "personal_info"

response = requests.get(f"{OURA_URL}/{COLLECTION_URL}/{response_needs}", headers = headers)

json_response = response.json()
df = pd.DataFrame(json_response, index = [0])

df = df.add_prefix('client_')

print(df)