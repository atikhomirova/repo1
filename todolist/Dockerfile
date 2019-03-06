FROM python:3.7
ENV PYTHONUNBUFFERED 1


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN mkdir /code
COPY requirements.txt code/
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
