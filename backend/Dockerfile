# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy entire backend app
COPY ./app /app/app

# Run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
