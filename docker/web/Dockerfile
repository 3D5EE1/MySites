FROM python:latest

ENV PYTHONBUFFERED 1
ENV MY_DIR MySites

RUN mkdir -p /var/log/gunicorn

ADD ./$MY_DIR $MY_DIR
ADD gunicorn.conf $MY_DIR
ADD requirements.txt $MY_DIR

WORKDIR $MY_DIR
RUN pip install -r requirements.txt

CMD gunicorn -c gunicorn.conf $MY_DIR.wsgi