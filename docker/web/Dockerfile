FROM python:latest

ENV PYTHONBUFFERED 1
ENV MY_DIR MySites

RUN mkdir -p /var/log/gunicorn

ADD . $MY_DIR

WORKDIR $MY_DIR
RUN pip install -r requirements.txt