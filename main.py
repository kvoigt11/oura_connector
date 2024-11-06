
from oura_endpoints import pull_oura_endpoints
from settings import response_endpoints_list



def main():
    pull_oura_endpoints(response_endpoints_list)


if __name__ == "__main__":
    main()