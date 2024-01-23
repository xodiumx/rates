# Info about currency rates

## Установка через `Docker`

1. Cклонируйте репозиторий
```
git clone git@github.com:xodiumx/rates.git
```
3. Перейдите в директорию
```
cd src
```
2. В директории `src` создайте `.env` file
```
SECRET_KEY='django-insecure-y&2fj&1trnl)n4j5b&s*3r*bn4_#z*y11o$#^qw6j)=5@y(-k2'

DB_NAME=rates
DB_HOST=db
# DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=admin
DB_ENGINE=django.db.backends.postgresql

POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin

PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_TASK_TRACK_STARTED=True
CELERY_TASK_TIME_LIMIT=60

FLOWER_USER=admin
FLOWER_PASSWORD=admin

DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin

API_KEY=SzR3TJROpiCTDb5K9dKSwehNGsdus5Uy
```
3. Выполните команду
```
docker-compose up -d
```

## Доступные эндпоинты

- `localhost/admin` - данные для входа - admin:admin
- `localhost:5050/` - `pgadmin` эндпоинт
- `localhost:5555/flower/` - `flower` эндпоинт
- `localhost/api/v1/get-current-usd/` - список последних 10 курсов доллара
