#!/bin/bash

nginx

letsencrypt certonly --webroot -w /var/www/rypy -d rypy.ru -d www.rypy.ru -m rypylook@outlook.com --agree-tos

service rsyslog start && service cron start && tail -f /var/log/syslog

mv /nginx2.conf /etc/nginx/nginx.conf

nginx -s reload

