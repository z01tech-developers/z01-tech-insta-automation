# Use a slim Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8080 to match Cloud Run expectations
EXPOSE 8080

# Run the Flask app
CMD ["python", "main.py"]
