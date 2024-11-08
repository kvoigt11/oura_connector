# Use the official Python 3.11 image as the base
FROM python:3.11.4-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python scripts into the container
COPY *.py .

# Set the command to run the Python script
CMD ["python", "main.py"]