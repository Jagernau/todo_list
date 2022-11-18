FROM python:3.10-slim
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY todolist/ .
# COPY todolist/core/ core/
# COPY todolist/todolist/ todolist/
# COPY todolist/manage.py manage.py
RUN ./manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
