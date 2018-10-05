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

`manage.py loaddata fixtures/groups.json`

Run the app

`python manage.py runserver`