FROM python:latest

ENV PYTHONBUFFERED 1
ENV MY_DIR MySites

RUN mkdir -p /var/log/gunicorn

ADD ./MySites $MY_DIR
ADD gunicorn.conf $MY_DIR
ADD requirements.txt $MY_DIR

WORKDIR $MY_DIR
RUN pip install -r requirements.txt