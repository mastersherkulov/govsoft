FROM python:3.13.5-bullseye

RUN apt-get update && apt-get install -y python3-pip && apt-get install -y libpq-dev 

RUN pip install --upgrade pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /project
COPY . /project