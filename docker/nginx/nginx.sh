#!/bin/bash

echo 'запуск nginx...'

nginx

echo 'получение сертификата...'

letsencrypt certonly --webroot -w /var/www/rypy -d rypy.ru -d www.rypy.ru -m rypylook@outlook.com --agree-tos

echo 'перенос конфига для порта 443...'

mv /nginx2.conf /etc/nginx/nginx.conf

echo 'запуск rsyslog и cron, применение настроек nginx...'

service rsyslog start && service cron start && nginx -s reload && tail -f /var/log/syslog