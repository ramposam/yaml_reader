# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the app files
COPY . .
# Copy the requirements file and install dependencies
#COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# Create output directory
RUN mkdir -p output

## Run the main script when the container starts
CMD ["python", "main.py"]
