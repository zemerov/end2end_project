FROM python:3.9-slim

WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src ./src
COPY data ./data

CMD ["python3", "/app/src/main.py"]
