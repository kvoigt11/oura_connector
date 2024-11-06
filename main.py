import datetime

from oura_endpoints import pull_oura_endpoints
from datetime import date

# Returns the current local date
today = date.today()

# Select all data
start_date = today - datetime.timedelta(1)
end_date = today


# Runs main
def main():
    pull_oura_endpoints(start_date, end_date)


if __name__ == "__main__":
    main()