# Appetizer
`Restaurant site with catering service`

Build by using Django 3 and Python 3

# deployed on Heroku Service (w/o images)

- Try to Register new user and Sign in for creation order and viewing orders history.
Please notice, that your email in order should be the same as in registration form.

https://appetizer-catering-service.herokuapp.com/

# deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Connect your PostgreSQL db in file appetizer/settings.py

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

3 - Create superuser by using command (for blog_post db model need to be default author with id=1):

`python3 manage.py createsuperuser`

4 - Load all data from JSON files to db by using next commands:

`python3 manage.py loaddata about_us.json`
`python3 manage.py loaddata meals.json`
`python3 manage.py loaddata catering.json`
`python3 manage.py loaddata blog.json`

5 - Run app:

`python3 manage.py runserver`
