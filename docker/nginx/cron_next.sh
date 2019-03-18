#!/bin/bash

echo 'запуск nginx...'

nginx

echo 'запуск rsyslog и cron...'

service rsyslog start && service cron start && tail -f /var/log/syslog