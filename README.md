## Trendy words

A platform to collect text documents of a corpus to observe word trending variations over time.

## Local dev

Create a .env file contaning dev configurations (empty database ready to use) and RabbitMQ server:

```
# $ openssl rand -hex 32
SECRET_KEY="bca651bc236a794a12daf545c35530552763b78c05d144930ec4cd69153c02be"
ENVIRONMENT=dev
# postgresql
PG_DATABASE=trendy_words
PG_USER=postgres
PG_PASSWORD=postgres
PG_HOST=localhost
PG_PORT=5432
# celery
CELERY_BROKER_URL=amqp://guest@localhost//
```

Create a python venv:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Init database:

```shell
$ ./manage.py migrate
```

Launch services:

```shell
# celery worker to execute tasks
$ celery -A TrendyWords worker --loglevel=INFO

# celery beat to schedule tasks
$ celery -A TrendyWords beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# django backend/frontend
$ ./manage.py createsuperuser --username admin --email admin@nowhere.org --skip-checks
$ ./manage.py runserver
```

Web app : http://localhost:8000/
