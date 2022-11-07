## Приложение: Планировщик задач.

стек (python3.9, Django, Postgres)


### Скачать:

1. Скачать проэкт: `git clone https://github.com/Jagernau/todo_list`
2. Зайти в папку `cd todo_list`


### Установка виртуальной среды для проэкта:

1. Создать песочницу: `python3 -m virtualenv env`
2. Войти в виртуальную среду: `source env/bin/activate`
3. Обновить "pip" виртуальной среды: `pip install --upgrade pip`
4. Установить библиотеки проэкта: `pip install -r requirements.txt`


### Запуск Postgres и передача констант в setings.py:

1. Создать файл `.env` и заисать в него:
    - `SECRET_KEY=`
    - `DEBUG=`
    - `POSTGRES_DB=` Имя db
    - `POSTGRES_USER=` Имя Пользователя
    - `POSTGRES_PASSWORD=` Пароль Пользователя
    - `POSTGRES_HOST=` Хост постгрес, по умолчанию "localhost"
    - `POSTGRES_PORT=` Порт по умолчанию "5432"

2. Запустить Postgres через докер и передать в него секретные константы: 
```
sudo docker run --name django_db -e POSTGRES_PASSWORD= -e POSTGRES_DB= -e POSTGRES_USER= -p 5432:5432 -d postgres
```

* Простой 



