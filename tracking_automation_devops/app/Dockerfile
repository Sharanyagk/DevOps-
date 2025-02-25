# Use a lightweight Python image
FROM python:3.9-slim  

# Set the working directory inside the container
WORKDIR /app  

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the entire application code
COPY . .  

# Expose the application port
EXPOSE 8000  

# Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]  
