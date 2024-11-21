# Use the official Prefect 3.1.2 image as the base
FROM prefecthq/prefect:3.1.2.dev1-python3.11

# Set the working directory to /app
WORKDIR /opt/prefect/flows

# Install ODBC Driver
RUN apt-get update && apt-get install -y \
    gnupg2 \
    curl \
    unixodbc \
    unixodbc-dev

# Add Microsoft repository and install SQL Server ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copy the requirements file into the container
COPY requirements.txt .

# Rest of the Dockerfile
RUN if [ "$OS" = "Windows_NT" ]; then \
    pip install pywin32==308; \
    fi

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Bring in environmental variables
COPY .env .

RUN apt-get clean
RUN apt-get update

# Install gdal and its development headers
RUN apt-get update && apt-get install -y gdal-bin libgdal-dev

# Copy the rest of the application code into the container at /app
COPY . /opt/prefect/flows



CMD ["streamlit", "run", "app_contents/app.py", "--server.port=80", "--server.enableCORS=false"]