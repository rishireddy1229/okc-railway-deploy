# Use an official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app/backend

# Copy the project files into the image
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r backend/requirements.txt

# Make script executable
RUN chmod +x start.sh

# Expose port
EXPOSE 8000

# Run the script
CMD ["./start.sh"]
