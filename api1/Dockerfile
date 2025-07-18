FROM python:3.13-slim

WORKDIR /app

COPY app1.py .

RUN pip install --no-cache-dir flask requests

EXPOSE 8888

CMD ["python", "app1.py"]
