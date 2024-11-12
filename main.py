import datetime

from oura_endpoints import pull_oura_endpoints
from datetime import date
from daily_activity_snow import daily_activity_blob_to_snowflake
from daily_cardio_age_snow import daily_cardio_age_blob_to_snowflake
from daily_readiness_snow import daily_readiness_blob_to_snowflake
from daily_sleep_snow import daily_sleep_blob_to_snowflake
from daily_spo2_snow import daily_spo2_blob_to_snowflake
from daily_stress_snow import daily_stress_blob_to_snowflake
from personal_info_snow import personal_info_blob_to_snowflake
from sleep_snow import sleep_blob_to_snowflake


# Returns the current local date
today = date.today()

# Select all data
start_date = today - datetime.timedelta(1200)
end_date = today


# Runs main
def main():
    pull_oura_endpoints(start_date, end_date)
    personal_info_blob_to_snowflake()
    daily_activity_blob_to_snowflake()
    daily_cardio_age_blob_to_snowflake()
    daily_readiness_blob_to_snowflake()
    daily_sleep_blob_to_snowflake()
    daily_spo2_blob_to_snowflake()
    daily_stress_blob_to_snowflake()
    sleep_blob_to_snowflake()



if __name__ == "__main__":
    main()