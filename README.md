Simple Flask App with FromZeroToFlask

## Run the Flask App

```
export FLASK_APP=hello
flask run
```

## Run Debug Mode
* Notes: Do NOT run Debug mode in production
```
export FLASK_DEBUG=1
```

## Flask follow the MVC design pattern
- Model: File or set of files dedicated to read from and write to a database
- View: File or set of files dealing with the presentation layer (HTML, CSS, JS)
- Controller: File or set of files that coordinate request and load and save the data using the model and present it back to the user using the views

### MVC: Templates
In Flask the views are handled by Templates. (views = templates)
they take as input a set of variables call context and return HTML
create a template folder. Flask always look for a set of folder and templates is one of them.

#### render template
- Create an index.html file under the newly created templates directory
- update you app to "render_template('<the_index_html_file>')"

#### passing context to template
- Create an hello.html file under the templates directory
- create a Jinja variable in the HTML content of hello.html
- update you app to "render_template('<the_index_html_file>', '<the_variable_name>')" (in my case it is the post.html)

### Adding link for other pages: url_for

- add an HTML anchor (<a>) to index
- URL_for provided by flask to tie your URL to a function name instead of a route, as route can change a lot

### The static folder
- files dont need to be change by our controller- Presentation centric files : like CSS, JavaScript
- Create a static directory, then update the index file

### Extending templates (DRY: Don't Repeat Yourself)

(parent template, extended template)
- for create a base template under the template folder.
- 2 more steps to make your your styles available to all other templates
1. in the template that extends the base, in the 1st line, extend the base
```{% extends "base.html" %}```
2.  - in the base template insert a directive to tell base where to render the content from any child template
```{% block content %}{% end block %}```
    - in the child template, surround the content with
    ```{% block content %}<content_here>{% endblock %}```

### Forms and HTTP Verb (the Get and Post Methods):
- the GET verb reads the URL.
- You can pass variable in the URL. They are called field-value pairs of query parameters and they all starts after the "?" in the URL

in the view, you could use ```first_name = request.args.['first_name']``` for the function but if a parameter in not pass you will get an http bad request. use the get ```first_name = request.args.get('first_name')```

#### Key difference between Get and Post

-------------------------
| GET       |       POST|
-------------------------
| Data passed in URL| Data in request body|
| Data limit| No data limit|
|requests cached by browser|Requests not cached by browser|
-------------------------

request.values.get reads both GET and POST, really convenient

it is good practice to redirect a user to another route after he fills out the form, because the browser cache the values, and the recored can be recreated over an over again. 

### Cookies and Sessions
HTTP is a stateless protocol, the server sees each HTTP page as a standalone operation. No history. 

that's why cookies are used.

- cookies: it is a piece of data that the server save on your compute to reuse information about you.vthis is how it works: cookies are set in one page and are available either when you reload the page or go to another page. when you 1st set your cookie, you won't be able to see it in the 1st page. Cookies are unsecure and sessions come to the rescue
- sessions: randomliy generated string saved on your compute and points back to the data on the server. the data on the website is also encrypted, hard to decode

you have to have randomly generate secret to encrypt the cookie
you can generate one : python -c "import os; print(os.urandom(16))"

### Databases
big siloes that can store millions of records
deveided into small logical sileos call table
Tables have a specific structure called Schema describimg name, type, lenght of column
Id is added by the db
once data is save in the DB you can run queries against it
queries are data operations to retrieve one or more data macthing a criteria.
if the email is unique, we can make the email column a unique key 
Database create index to help speed up record search 

### CRUD

C: Create - R: Read - U: Update - D: Delete

In MySQL this is the equivalent query for CRUD
Create: Insert
Read: Select 
Update: Update
Delete: Delete

Install mysql
```brew install mysql```
Secure MySQL
```mysql_secure_installation```
No to Validate Password Plugin
Remove the Anonymous user login
and remote root user login
remove the test database
reload the priviledge

with MariaDB
```mysqladmin --user=root password 'password'```


### ORM: Object Relational Mapper

MVC, if templates are for Views, Models are files that deal with anything related to connecting/talking to the Database. That model file leverage ORM which converts data rows into objects. so when accessing user in that route, we would request a list of object from the model, not issueing SQL command, if anything change DB structue or go to another DB, we only change the Models files not the application:

```users = User.query.filter_by(live=1)```


## Application Factory

Application factory design pattern.

Usually  we have modules in the application that do different things and we seperates them this way to create order.

A file like `app.py` that creates an instance of the application. 


## Blueprints

Building pives of app focus on specific areas:

ex. if we were building twitter: user - feed - relationship (would be different modules responsible for different part of the applations). Each would have theor own model, controller and views

in flask views.py for controller, template for the views and model for model, they have their test and all is grouped under one app (user for ex.)


### Migrations

After creating models that have classes that represent schemas in your database, need to apply the changes to the DB

for the 1st time run ```flask db init```

output
```shell
/Users/klouis/projects/flask-visitor-counter/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
  Creating directory /Users/klouis/projects/flask-visitor-counter/migrations ...  done
  Creating directory /Users/klouis/projects/flask-visitor-counter/migrations/versions ...  done
  Generating /Users/klouis/projects/flask-visitor-counter/migrations/script.py.mako ...  done
  Generating /Users/klouis/projects/flask-visitor-counter/migrations/env.py ...  done
  Generating /Users/klouis/projects/flask-visitor-counter/migrations/README ...  done
  Generating /Users/klouis/projects/flask-visitor-counter/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/klouis/projects/flask-visitor-counter/migrations/alembic.ini' before proceeding.
```

then run ```flask db migrate```

output
```shell
/Users/klouis/projects/flask-visitor-counter/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'counter'
  Generating /Users/klouis/projects/flask-visitor-counter/migrations/versions/e3cfac093eb3_.py ...  done
  ```

  then run ```flask db upgrade```

output
```shell
  /Users/klouis/projects/flask-visitor-counter/venv/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e3cfac093eb3, empty message
```
