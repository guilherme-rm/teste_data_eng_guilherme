# Python image
FROM python:3.10-slim

# Work directory
WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code to container
COPY . .

# Copy setup scripts to container
COPY setup/ /setup

# Execute setup scripts
RUN python /setup/create_fonte.py
RUN python /setup/gen_data_fonte.py
RUN python /setup/create_alvo.py

# Expose server port
EXPOSE 8000

# commands to run app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]