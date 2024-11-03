# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
# WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY app.py /app.py

# Install dependencies
RUN apt-get update && apt-get install -y wget unzip gnupg \
    && apt-get install -y firefox-esr \
    && wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && chmod +x /usr/local/bin/geckodriver \
    && rm /tmp/geckodriver.tar.gz

# Install Selenium
RUN pip install selenium

# Run the script
CMD ["python", "/app.py"]
