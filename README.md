Project Title: Subscription Management System with Django & Celery
All API endpoints Postman documentation below: https://documenter.getpostman.com/view/24667147/2sB3BANCvH

This project was initially configured for local development. If you intend to run it using Docker, some changes in settings.py (such as database host configuration) are required. Please refer to the Docker setup instructions.

How to Run: 
    Local Setup: 
        1. Clone the repo.
        2. Create and activate a virtual environment.
        3. Install dependencies (pip install -r requirements.txt).
        4. In the root directory, create a .env file and edit it as shown below. 
           In the MySQL setup, specify your database name, username, and password. 
           If you prefer to use Django's default SQLite database, you can skip the MySQL configuration
        6. When use localhost in settings.py there use : 
            CELERY_TIMEZONE = "Asia/Dhaka"
            CELERY_BROKER_URL = 'redis://localhost:6379/0'
            CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
            CELERY_ACCEPT_CONTENT = ['json']
            CELERY_TASK_SERIALIZER = 'json'

            and in Databases: 'HOST': 'localhost',

        7. Run migrations (python manage.py migrate)
        8. Celery task Configuration: 
            i. Go to the Django Admin Panel.
            ii. Log in with a superuser account.
            iii. In Periodic Tasks : 
                Create an Interval Schedule (Every:1, Period: hours), 
                Create the Periodic Task ( Name: Fetch Exchange Rate USD to BDT, Task: myapp.tasks.fetch_usd_to_bdt, Interval: Select the 1 hour interval you just created )

        9. Start Redis server (redis-server).
        10. Run Celery worker another terminal (celery -A flarezen_task worker --beat --loglevel=info).
        11. Start Django development server (python manage.py runserver).
        12. Visit http://localhost:8000/subscriptions to see the frontend subscription list.
        13. Done

    Docker usage Setup:
        1. Create .env File.
        2. When use Docker in settings.py there use : 
            CELERY_TIMEZONE = "Asia/Dhaka"
            CELERY_BROKER_URL = 'redis://redis:6379/0'  
            CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
            CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
            CELERY_ACCEPT_CONTENT = ['json']
            CELERY_TASK_SERIALIZER = 'json'

            and in Databases: 'HOST': 'db',

        3. sudo docker ps -a (from there get flarezen-task-web container ID).
        4. sudo docker start ... (there give flarezen-task-web container ID).
        5. sudo docker ps (Check there redis:alpine this container running. 
            or not, if running then next command else start this with container ID or name).
        6. sudo docker-compose run web bash / sudo docker exec -it (there give flarezen-task-web        container ID) bash.
        7. Create an superuser and configure (6. Celery task Configuration).
        8. Run celery with this command :  celery -A flarezen_task worker --beat --loglevel=info.
        9. Done

    The .env File: 
        SECRET_KEY='django-insecure-1))l17xv+q%92-7yru=kuyl4timwg6smfspf4c!l=_9^n!w+5x'
        MYSQL_DATABASE = 'mydatabase' 
        MYSQL_USER = 'falrezen' 
        MYSQL_PASSWORD = 'falrezenadmin' 
        If want djnago default Database use this:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
