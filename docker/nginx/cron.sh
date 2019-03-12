#!/bin/bash

echo 'запуск nginx...'

nginx

echo 'получение сертификата...'

letsencrypt certonly --webroot -w /var/www/rypy -d rypy.ru -d www.rypy.ru -m rypylook@outlook.com --agree-tos

echo 'перенос конфига для порта 443...'

mv /nginx_next.conf /etc/nginx/nginx.conf

mv /cron_next.sh /cron.sh