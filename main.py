import datetime

from prefect import flow
from prefect.logging import get_run_logger
from prefect.docker import DockerImage

from oura_endpoints import pull_oura_endpoints
from datetime import date
from daily_activity_az import daily_activity_blob_to_azure
from daily_cardio_age_az import daily_cardio_age_blob_to_azure
from daily_readiness_az import daily_readiness_blob_to_azure
from daily_sleep_az import daily_sleep_blob_to_azure
from daily_spo2_az import daily_spo2_blob_to_azure
from daily_stress_az import daily_stress_blob_to_azure
from personal_info_az import personal_info_blob_to_azure
from sleep_az import sleep_blob_to_azure


# Returns the current local date
today = date.today()

# Select all data
start_date = today - datetime.timedelta(1200)
end_date = today


# Runs main
@flow(log_prints=True)
def main():
    pull_oura_endpoints(start_date, end_date)
    personal_info_blob_to_azure()
    daily_activity_blob_to_azure()
    daily_cardio_age_blob_to_azure()
    daily_readiness_blob_to_azure()
    daily_sleep_blob_to_azure()
    daily_spo2_blob_to_azure()
    daily_stress_blob_to_azure()
    sleep_blob_to_azure()


if __name__ == "__main__":
    main.deploy(
        name="oura-runner",
        image=DockerImage(
            name="containerregistrykylevoigt.azurecr.io/kv-portfolio-app:latest",
            platform="linux/amd64",
            dockerfile="Dockerfile"
        ),
        work_pool_name="aci-work-pool",
        push = False
    )