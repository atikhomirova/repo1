FROM python:3.7.2-alpine3.9  # Ant: Use python 3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir src/
COPY requirements.txt src/
WORKDIR /src/
RUN pip install -r requirements.txt
ADD . /src/
