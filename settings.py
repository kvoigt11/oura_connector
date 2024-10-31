import os
from dotenv import load_dotenv

start_date = '2020-01-01'
end_date = '2024-10-29'

# Load environment variables from .env file
load_dotenv()

clientId = os.getenv("oura_clientid")
clientSecret = os.getenv("oura_clientsecret")
personalToken = os.getenv("oura_token")

# Big stuff
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(personalToken)}


OURA_URL = 'https://api.ouraring.com'
COLLECTION_URL = "v2/usercollection"
