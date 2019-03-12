#!/bin/bash

echo 'запуск rsyslog и cron...'

service rsyslog start && service cron start && tail -f /var/log/syslog