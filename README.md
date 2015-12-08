Bugtrax
=======

A simple bug-tracking system.

How to setup locally
--------------------

This project was built using Python 3.4. This will probably not work under Python 2.7.
My development environment is Ubuntu 14.04. All commands below assume you're running the same
OS or something similar.

Create a new virtual environment and activate it.

```bash
python3 -m venv bugtrax
cd bugtrax
source bin/activate
```

Clone the repository.

```bash
hg clone ssh://hg@bitbucket.org/pvergil/bugtrax
```

Run migrations.

```bash
python3 manage.py migrate
```

Create a super user.

```bash
python3 manage.py createsuperuser
```

Run the development server.

```bash
python3 manage.py runserver
```