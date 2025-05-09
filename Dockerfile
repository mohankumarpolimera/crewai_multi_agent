# Base image with Python
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your script (change if needed)
CMD ["python", "run.py"]
