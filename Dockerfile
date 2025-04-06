FROM python:3.11-slim

# Install system-level dependencies if needed (but slim has most things already)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .
COPY app/ app/
COPY gmailtogravatar.py .
COPY .env .

# Install dependencies globally (inside container)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]