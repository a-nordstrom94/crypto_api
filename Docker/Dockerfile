# Use official Python 3.11 image from Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
# NOTE: this Dockerfile lives in the Docker/ folder while the build context
# will be the repository root. The requirements file is kept at Docker/requirements.txt
COPY Docker/requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and data from the repository root (build context)
COPY Src/ ./Src/

# Set environment variables for Python unbuffered output
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "-m", "Src.main"]
