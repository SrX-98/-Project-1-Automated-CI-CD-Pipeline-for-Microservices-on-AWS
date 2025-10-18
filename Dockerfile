# Use official lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the app port
EXPOSE 5000

# Run app using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
