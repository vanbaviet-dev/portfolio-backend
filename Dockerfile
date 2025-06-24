# Use official Python image
FROM python:3.13.4-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh","gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]
