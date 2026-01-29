FROM python:3.12-slim

RUN pip install --no-cache-dir requests

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
