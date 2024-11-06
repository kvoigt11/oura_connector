import os

from dotenv import load_dotenv


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
def set_simple_params(start_date, end_date):
    simple_params = {f'q': 'requests+language:python',
            'start_date': {start_date},
            'end_date': {end_date}}
    
    return simple_params


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


SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")