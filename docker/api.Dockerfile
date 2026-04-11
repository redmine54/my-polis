# docker/api.Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY ../backend /app
COPY ../sample_data /sample_data

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uv", "run", "app/main.py"]
