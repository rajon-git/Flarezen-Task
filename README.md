Project Title: Subscription Management System with Django & Celery

How to Run: 
    Local Setup: 
        1. Clone the repo
        2. Create and activate a virtual environment
        3. Install dependencies (pip install -r requirements.txt)
        4. In the root directory, create a .env file and edit it as shown below. In the MySQL setup,        
            specify your database name, username, and password. If you prefer to use Django's default SQLite database, you can skip the MySQL configuration

        5. Run migrations (python manage.py migrate)
        6. Celery task Configuration: 
            i. Go to the Django Admin Panel
            ii. Log in with a superuser account.
            iii. In Periodic Tasks : 
                Create an Interval Schedule (Every:1, Period: hours), 
                Create the Periodic Task ( Name: Fetch Exchange Rate USD to BDT, Task: myapp.tasks.fetch_usd_to_bdt, Interval: Select the 1 hour interval you just created )

        7. Start Redis server (redis-server)
        8. Run Celery worker (celery -A flarezen_task worker --beat --loglevel=info)
        9. Start Django development server (python manage.py runserver)
        10. Visit http://localhost:8000/subscriptions to see the frontend subscription list.
        11. Done

    Docker usage Setup:
        1. Create .env File
        2. sudo docker ps -a (from there get flarezen-task-web container ID)
        3. sudo docker start ... (there give flarezen-task-web container ID)
        4. sudo docker ps (Check there redis:alpine this container running 
            or not, if running then next command else start this with container ID or name)
        5. sudo docker-compose run web bash / sudo docker exec -it (there give flarezen-task-web        container ID) bash
        6. Create an superuser and configure (6. Celery task Configuration)
        7. Run celery with this command :  celery -A flarezen_task worker --beat --loglevel=info
        8. Done

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
