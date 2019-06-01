# TechOTD
A Tech blog site: HTML, CSS, Javascript and Django 2.0.

##Installation steps:
1. Clone Repository and navigate into directory with manage.py.
2. Activate virtual environment. Run 'source absolute-path/blog/bin/activate'.
3. Run 'pip install -r requirements.txt' This will install the dependencies of the project.
4. Run 'python3 manage.py makemigrations' to make make migrations.
5. Run 'python3 manage.py migrate' to migrate the model to database (sqlite3).
6. Run 'python3 manage.py runserver' to start the server.
7. Navigate to 127.0.0.1/index on your browser to arrive at the home page.

##If you get an error at 'python3 manage.py makemigrations' or 'python3 manage.py migrate':
-Run the following: 
-echo ">> Deleting old migrations" 
-find . -path "*/migrations/*.py" -not -name "__init__.py" -delete 
-find . -path "*/migrations/*.pyc"  -delete

##If error still exists:
-Run the following to check django version and reinstall: 
-python -m django --version
-pip install --upgrade --force-reinstall  Django==2.0.5
