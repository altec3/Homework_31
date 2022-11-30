# Урок 31. Домашнее задание


### Создание и запуск образа с PostgreSQL

```python
docker run --name hw_31_psql -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

### Миграция таблиц в базу данных

```python
python manage.py migrate
```


### Загрузка фикстур в базу данных

```python
python manage.py loaddata location.json
python manage.py loaddata user.json
python manage.py loaddata category.json
python manage.py loaddata ad.json
```
