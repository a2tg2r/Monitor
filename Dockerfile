# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY roblox_afk_script.py .

# Run the script when the container starts
CMD ["python", "roblox_afk_script.py"]
