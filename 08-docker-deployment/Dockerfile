FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
