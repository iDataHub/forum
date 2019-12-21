# DataHub Forum
Forum based on `django-spirit`.

## Installation
```
git clone --depth 1 https://github.com/iDataHub/forum

cd forum
mv environ.example environ
source environ
pipenv shell
pipenv install

cd datahub
python manage.py collectstatic
# if not 'db.sqlite3' exists
#     python manage.py spiritinstall
#     python manage.py createsuperuser
python manage.py runserver idatahub.tech:8000
```

## TODO
- Using `datahub.settings.prod`.
