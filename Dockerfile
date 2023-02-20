FROM python:3.10-slim-buster
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
