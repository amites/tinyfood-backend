# Tiny Food Django Backend

Provides a simple wrapper around some data models to provide support for the tinyfood.org project.

requires `python3`

to get started



if using `pyenv`
```
pyenv install 3.7.3
pyenv virtualenv 3.6.6 tinyfood
pyenv activate tinyfood
```

```
git clone https://github.com/amites/tinyfood-backend.git
cd tinyfood-backend
pip isntall -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
# follow prompts
python manage.py runserver 0.0.0.0:8000
```


visit

http://localhost:8000/admin

sign-in with your created credentials


supported uris

- /tinyfood/json_index


