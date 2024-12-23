# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy script and requirements
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg2 && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Set environment variables
ENV DISPLAY=:99

# Run the script
CMD ["python", "roblox_afk_script.py"]
