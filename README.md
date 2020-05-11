# Youtube Data API

There is a periodic function which is running every minute, to fetch data from YouTube Data API, and there is redis cache storing results for a short time limit, which get refreshed every minute, or in cache miss is there.

Celery is a task queue, used to asynchronously execute work outside the HTTP request-response cycle. And the message broker used here is again redis.

Major Dependencies to be installed are:
1. Celery
2. Redis server
3. Google-api-client

Steps to run the project:
1. We need to create a virtual environment, using `python3 -m venv my_env`.
2. After creating virtual environment, we need to activate the virtual environment, using `source my_env/bin/activate`.
3. Changing the directory to fampay, we can now install the required dependecies using the command,  `pip install requirements.txt`
4. And the server can be run by `python manage.py runserver`
5. We need to run the redis local server using `redis-server`, if it's already trying stopping it and running it again.
6. We got to run the celery as well using command `celery -A <project_name> beat` and in other terminal `celery worker -A <project_name> --loglevel=info --concurrency=4`
7. We can check the API response on the localhost server with port 8000, with the link `localhost:8000/link/<int>` that int would be the page number, you would want.
