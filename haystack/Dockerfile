# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Haystack code to the container
COPY . .

# Expose the port the Haystack service will run on
EXPOSE 8000

# Command to run the Haystack API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
