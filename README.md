Project Title: Subscription Management System with Django & Celery

Explanation:
Setting Up the Django Project:
    1. Create a new Django project and app
    2. Configure the database
    3. Install and configure required packages
    4. Configure Redis as the Celery broker.
Models: 
    1. Create models for Plan, Subscription, and ExchangeRateLog
Celery Task:
    1. Implement a Celery task to fetch USD to BDT exchange rates periodically (every one hour or configurable)
    2. Log the fetched rates into ExchangeRateLog
Admin Panel Permissions:
    1. Staff users can add/edit/delete Plan entries.
    2. Staff can view user Subscription and ExchangeRateLog entries (read-only).
    3. Superusers have full access to all models and actions.
Frontend:
    1. /subscriptions/: A table listing all users and their subscriptions (username, plan, start/end date, status).
    2. Use conditional styling for subscription status: Active = green, Cancelled = red, Others = yellow
    3. This page should be publicly accessible (no login required).
How to Run: 
    1. Clone the repo
    2. Create and activate a virtual environment
    3. Install dependencies (pip install -r requirements.txt)
    4. Run migrations (python manage.py migrate)
    5. Celery task Configuration: 
       i. Go to the Django Admin Panel
       ii. Log in with a superuser account.
       iii. In Periodic Tasks : 
               Create an Interval Schedule (Every:1, Period: hours), 
               Create the Periodic Task (Name: Fetch Exchange Rate USD to BDT, Task: myapp.tasks.fetch_exchange_rate , 
               Interval: Select the 1 hour interval you just created)
    6. Start Redis server (redis-server)
    7. Run Celery worker (celery -A flarezen_task worker --beat --loglevel=info)
    8. Start Django development server (python manage.py runserver)
    9. Visit http://localhost:8000/subscriptions to see the frontend subscription list.

The .env File: 
    SECRET_KEY='django-insecure-1))l17xv+q%92-7yru=kuyl4timwg6smfspf4c!l=_9^n!w+5x'

    For MySQL Setup 
    MYSQL_DATABASE = 'mydatabase' # Your database name
    MYSQL_USER = 'falrezen'  #Your db username
    MYSQL_PASSWORD = 'falrezenadmin' #Your db password
    If want djnago default Database use this:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
