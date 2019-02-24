FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir src/
COPY requirements.txt src/
WORKDIR /src/
RUN pip install -r requirements.txt
ADD . /src/
