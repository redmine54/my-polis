# docker/api.Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY ./backend/app /app/app
COPY ./backend/requirements.txt /app/requirements.txt
COPY ./sample_data /sample_data

RUN echo "=== /appの内容 ===" && ls -R /app

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install uv

EXPOSE 8000

# CMD ["uv", "run", "-m","app.main"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
