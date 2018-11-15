# How to Cache Using Redis in Django Applications
This application demonstrates how to use Redis in caching of Django Applications using the following [tutorial](https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178)

## Setting up:

```shell
git clone https://github.com/isaacomondi/django_caching.git
cd django_cache
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

To seed data into your db, I have created a script called `load_data.py`. To use it just run your server and on another terminal write: 

```shell
python load_data.py
```