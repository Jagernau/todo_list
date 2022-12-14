## Приложение: Планировщик задач.



стек (python3.9, Django, Postgres)


### Скачать:

1. Скачать проэкт: `git clone https://github.com/Jagernau/todo_list`
2. Зайти в папку `cd todo_list`


## Запуск проэкта через docker-compose:
Очень быстро! Всё собранно!
1. В директории `todolist` создать файл `.env`:

    - `SECRET_KEY=`
    - `DEBUG=`
    - `POSTGRES_DB=` Имя db
    - `POSTGRES_USER=` Имя Пользователя
    - `POSTGRES_PASSWORD=` Пароль Пользователя
    - `VK_OAUTH2_KEY=` Это в ВК надо создать приложение, сайт для API, это id приложения!!!
    - `VK_OAUTH2_SECRET=` Это ключ от этого API, что бы посетитель мог зарегистрироваться через соцсеть.
    - `BOT_TOKEN=` Это токен бота для Телеграм, которого Вам надо создать!

2. И всё запустить командой `sudo docker-compose up --build`

# Вариант вручную (это на случай если нет docker-compose).
### Установка виртуальной среды для проэкта:

1. Создать песочницу: `python3 -m virtualenv env`
2. Войти в виртуальную среду: `source env/bin/activate`
3. Обновить "pip" виртуальной среды: `pip install --upgrade pip`
4. Установить библиотеки проэкта: `pip install -r requirements.txt`

### Запуск Postgres и передача констант в setings.py:

1. Создать файл `.env` в директории `/todo_list/todolist` и записать в него:
    - `SECRET_KEY=`
    - `DEBUG=`
    - `POSTGRES_DB=` Имя db
    - `POSTGRES_USER=` Имя Пользователя
    - `POSTGRES_PASSWORD=` Пароль Пользователя
    - `POSTGRES_HOST=` Хост постгрес, по умолчанию "localhost"
    - `POSTGRES_PORT=` Порт по умолчанию "5432"
    - Вписать переменные для Вк и Тг как было описанно выше.

2. Запустить Postgres через докер и передать в него секретные константы: 
```
sudo docker run --name django_db -e POSTGRES_PASSWORD= -e POSTGRES_DB= -e POSTGRES_USER= -p 5432:5432 -d postgres
```

* Простой способ запуска Postgres и записи констант:

    - Разрешить выполнять скрипт `sudo chmod +x ./easy_env` 
    - Запустить скрипт `./easy_env`- этот скрипт спросит константы описанние выше, запишет их в `todolist/.env` и запустит докер postgres с переданными константами

    - Выполнить миграции  `./manage.py migrate`.
    - Запустить Бэкэнд `./manage.py runserver`.
    - С Фронтом запустить на 8000 порту, фронт доекр: sermalenk/skypro-front:lesson-38 на 80 порт.
    - Запустить бота Тг `./manage.py runbot`
