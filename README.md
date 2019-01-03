## Добавлено поле адреса электронной почты

![login](https://github.com/3d5ee1/MySites/raw/develop/static/readme/img/authentication.JPG "login")

***

## Изменен шаблон добавления пользователя в админке

![login](https://github.com/3d5ee1/MySites/raw/develop/static/readme/img/creation.JPG "login")

***

## Добавлены дополнительные поля информации о пользователе

![login](https://github.com/3d5ee1/MySites/raw/develop/static/readme/img/user_info.JPG "login")

***

## Изменен принцип входа в учетную запись 
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

2. выполнить команду **docker-compose up** из корня проекта, где лежит файл docker-compose.yml. 

3. после завершения установки необходимо перезагрузить все docker контейнеры, для этого нажать комбинацию клавиш CTRL + C дважды, затем выполнить команду **docker-compose up -d** это запустит проект со всеми примененными настройками в виде демона

## Migrate databases

> **обновление модели:** docker-compose exec **web** python manage.py **makemigrations**

> **миграция в базу:** docker-compose exec **web** python manage.py **migrate**

***

## Django collectstatic

> **перенос статических файлов в проект:** docker-compose exec **web** python manage.py **collectstatic**

***
