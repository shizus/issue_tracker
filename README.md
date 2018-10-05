# issue_tracker

## Pre-requisites

- Python 3.5
- Pip
- Virtualenv (optional)

## Installation

`git clone https://github.com/shizus/issue_tracker.git`


In the project directory, create a virtual environment with (if you are using virtualenv)

`virtualenv venv`

Activate the virtual environment

`source venv/bin/activate`

Install the project's requirements

`pip install -r requirements.txt`

Create the database

`python manage.py migrate`

Create a super user

`python manage.py createsuperuser`

Populate database with initial data

`python manage.py loaddata fixtures/groups.json`

Run the app

`python manage.py runserver`

## About the functionality

With the last section you have everything working with a group
called superuser that can do everything and a group called
staff that can view issues only.

**This must not be confused** with the staff and superuser attributes
for Django. In this app all users that need to see the
issues must be have the staff user attribute enabled.

A Django super user can do anything without needing a group
or any permission.

If you need to test how this works you can run

`python manage.py loaddata fixtures/users.json`



