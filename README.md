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
### create superuser
```python manage.py createsuperuser```
### to create new django app , example to create app by name base
```django-admin startapp base```
