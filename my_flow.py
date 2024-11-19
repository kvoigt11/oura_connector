from prefect import flow
from prefect.logging import get_run_logger
from prefect.docker import DockerImage

@flow
def my_flow():
    logger = get_run_logger()
    logger.info("Hello from ACI!")

if __name__ == "__main__":
    my_flow.deploy(
        name="my-third-deployment",
        image=DockerImage(
            name="containerregistrykylevoigt.azurecr.io/kv-portfolio-app:latest",
            platform="linux/amd64",
            dockerfile="Dockerfile"
        ),
        work_pool_name="aci-work-pool",
        push = False
    )