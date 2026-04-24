FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Debug: Verify API folder and files are copied
RUN ls -la && echo "=== API folder contents ===" && ls -la API/

CMD ["python", "-u", "main.py"]
