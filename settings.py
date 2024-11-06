import os
import datetime

from dotenv import load_dotenv
from datetime import date


# Returns the current local date
today = date.today()



# Select all data
start_date = today - datetime.timedelta(2000)
end_date = today


# Load environment variables from .env file
load_dotenv()

clientId = os.getenv("oura_clientid")
clientSecret = os.getenv("oura_clientsecret")
personalToken = os.getenv("oura_token")

AZ_KEY1_CONNECTION_STRING = os.getenv("AZ_KEY1_CONNECTION_STRING")
AZ_CONTAINER_NAME = os.getenv("AZ_CONTAINER_NAME")
AZ_FOLDER_PATH = os.getenv("AZ_FOLDER_PATH")

# Big stuff
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(personalToken)}

OURA_URL = 'https://api.ouraring.com'
COLLECTION_URL = "v2/usercollection"

# Set parameters
simple_params = {f'q': 'requests+language:python',
          'start_date': {start_date},
          'end_date': {end_date}}


# List of different response endpoints
response_endpoints_list = ['daily_activity',
                           'daily_readiness',
                           'daily_resilience',
                           'daily_sleep',
                           'daily_spo2',
                           'daily_stress',
                           'heartrate',
                           'personal_info',
                           'sleep',
                           'daily_cardiovascular_age']