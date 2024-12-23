# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Clear the webdriver-manager cache to avoid issues with corrupt files
RUN rm -rf /root/.wdm

# Optionally, if you want to manually copy ChromeDriver (in case of consistent issues with webdriver-manager):
# COPY chromedriver /usr/local/bin/chromedriver

# Run your Python script
COPY roblox_afk_script.py .

CMD ["python", "roblox_afk_script.py"]
