# BlogApp

Setup

The first thing to do is to clone the repository:

$ git clone https://github.com/afsal1/BlogApp.git

$ cd BlogApp

Create a virtual environment to install dependencies in and activate it:

$virtualenv venv

$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

Then migrate tables through the command:

(env)$ python manage.py makemigrations

(env)$ python manage.py migrate

Now you can run the server:

(env)$ python manage.py runserver



Walkthrough

Once your app running with python manage.py runserver , home page shows the login page. First time you need to create an account to login.
Signup with proper credentials then redirect to login page then you can login
