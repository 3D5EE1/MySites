#!/bin/bash

nginx

letsencrypt certonly --webroot -w /var/www/rypy -d rypy.ru -d www.rypy.ru -m rypylook@outlook.com --agree-tos

mv /nginx2.conf /etc/nginx/nginx.conf

service rsyslog start && service cron start && tail -f /var/log/syslog

nginx -s reload

