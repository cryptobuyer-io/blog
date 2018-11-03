# Blog Cryptobuyer

### Instalation
Install the dependencies
```sh
$ sudo aptitude update
$ sudo aptitude safe-upgrade
```

Install the dependencies:
```sh
$ sudo apt-get install git-core  libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev libxml2-dev libxslt-dev python-dev libssl-dev python3-pip postgresql libwv2-dev wv libpq-dev gettext python3.4-venv
```

Clone the Project:
```sh
$ git clone <repo-url>
$ cd blog/
```

Create a new virtual env:
```sh
python3 -m venv .env
```

Activate the virtualenv:
```sh
source .env/bin/activate
```

Install the Project dependencies:
```sh
pip3.4 install -r requirements.txt
```

Create the Database:
```sh
$ sudo su - postgres
$ psql
$ postgres@wagtail-sandbox:~$ psql
psql (9.3.13)
Type "help" for help.
postgres=# CREATE DATABASE blog;
postgres=# CREATE USER bloguser WITH PASSWORD 'blogpass';
postgres=# ALTER ROLE bloguser SET client_encoding TO 'utf8';
postgres=# ALTER ROLE bloguser  SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE bloguser  SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE blog TO bloguser;
postgres=# \q
```

Run the Migrations:
```sh
$ python manage.py migrate
```

Create a Superuser:
```sh
$ python manage.py createsuperuser
```

Runs the development server:
```sh
$ python manage.py runserver 0.0.0.0:8000
```
