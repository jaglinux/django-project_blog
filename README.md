# django-project_blog

### to run server
```python manage.py runserver```
### access API at http://127.0.0.1:8000/ 
### access django admin dashboard at http://127.0.0.1:8000/admin/ 

## Steps after cloning this project.
Before cloning, have virtual env ready (python3 -m venv . ; source bin/activate) <br>
```pip install -r requirements.txt``` <br>
Copy the master db.sqlite3 to project folder. (Or create fresh DB as explained later) <br>
TBD : migrations <br>
```python manage.py runserver```

## To create new django project, below commands are useful
### to create new django project
```django-admin startproject project_blog```
### to create fresh DB
```python manage.py migrate```
### apply migrations
```python manage.py makemigrations``` <br>
```python manage.py migrate```
### create superuser
```python manage.py createsuperuser```
### to create new django app , example to create app by name base
```django-admin startapp base```

## Celery and Redis setup
### Install Redis
```brew install redis``` <br>
```brew services start redis``` <br>
To check if redis is up <br>
```redis-cli``` <br>
```redis-server``` <br>
### Install Celery
pip install celery and redis client (already present in requirements.txt) <br>
### Start Celery
```export PYTHONPATH=<your project path>/project_blog``` <br>
```celery -A project_blog worker``` <br>
``` celery is  <Celery project_blog at 0x1022fe910>
 
 -------------- celery@jagadishs-MBP.attlocal.net v5.3.4 (emerald-rush)
--- ***** ----- 
-- ******* ---- macOS-12.2.1-arm64-arm-64bit 2023-10-15 07:00:34
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         project_blog:0x1022fe910
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     redis://localhost:6379/
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[2023-10-15 07:00:34,910: WARNING/MainProcess] /Users/jag/django/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2023-10-15 07:00:34,916: WARNING/MainProcess] /Users/jag/django/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(```
