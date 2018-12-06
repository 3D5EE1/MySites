FROM nginx:latest

RUN apt update && apt install -y cron rsyslog letsencrypt

ADD nginx1.sh /
ADD nginx2.sh /
ADD nginx1.conf /etc/nginx/nginx.conf
ADD nginx2.conf /

RUN echo "0 0 * * 1    root    /usr/bin/letsencrypt renew >> /var/log/letsencrypt-renew.log" >> /etc/crontab

RUN mkdir -p /var/www/rypy
RUN mkdir -p /var/www/media
RUN mkdir -p /var/www/static

RUN chown -R nginx:nginx /var/www/media
RUN chown -R nginx:nginx /var/www/static
RUN chmod 777 nginx1.sh
RUN chmod 777 nginx2.sh

ENTRYPOINT ["sh", "/nginx1.sh"]

ENTRYPOINT ["sh", "/nginx2.sh"]
