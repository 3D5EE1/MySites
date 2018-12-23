### Изменен принцип входа в учетную запись 
#### теперь для входя необходимо указать адрес электронной почты и пароль

![login](https://github.com/3d5ee1/MySites/raw/develop/static/readme/img/login.JPG "login")

***

## Project MySites in docker

`примеры того как выглядит проект`

моя [визитка](https://rypy.ru "визитка").

посмотреть все [проекты](https://rypy.ru/menu "страница выбора сайтов").

***

## инструкция:

1. создать любую директорию в системе на ваш выбор, зайти в нее и склонировать сам проект:
**git clone https://github.com/3D5EE1/MySites.git**.

2. выполнить команду **docker-compose up** из корня проекта, где лежит файл docker-compose.yml; 
команда **docker-compose up -d** запустит проект в виде демона



## Migrate databases

> **обновление модели:** docker-compose exec **web** python manage.py **makemigrations**

> **миграция в базу:** docker-compose exec **web** python manage.py **migrate**

***

## Django collectstatic

> **перенос статических файлов в проект:** docker-compose exec **web** python manage.py **collectstatic**

***
