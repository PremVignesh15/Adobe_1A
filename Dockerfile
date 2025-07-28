# Use official Python slim image
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy your code and requirements
COPY app/ /app/
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Tell the app it's running inside Docker
ENV IN_DOCKER=1

# Start the app
CMD ["python", "main.py"]
