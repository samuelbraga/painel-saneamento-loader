FROM python:3.10.8

RUN apt update && apt upgrade -y

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install --system --skip-lock