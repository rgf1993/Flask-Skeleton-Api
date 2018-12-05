# Flask-Skeleton

# Virtual Environment - Windows (Python 3+)
- To create the virtual environment: "python -m venv venv"

- To activate: "source venv/Scripts/activate


# To set the flask app variable run: 
-   export FLASK_APP=app.py



# To run locally:
- python manage.py runserver --threaded

-   "flask run"


# To add dependancies to requirements.txt:
-   pip freeze > requirements.txt

# To install dependancies from requirements.txt:
-   pip install -r requirements.txt


# Installed packages:

pip install flask
cors
autoenv
gunicorn==19.7.1


# db:

in venv:
-   python manage.py init

-   python manage.py db migrate (To pick up models changes)

- python manage.py db upgrade (to upgrade the database to a new alembic version)

# test:
py.test

#sql:
app.logger.info(cur.query)