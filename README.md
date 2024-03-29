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

| GET       |       POST|
------------|-------------
| Data passed in URL| Data in request body|
| Data limit| No data limit|
|requests cached by browser|Requests not cached by browser|
------------|-------------

request.values.get reads both GET and POST, really convenient

it is good practice to redirect a user to another route after he fills out the form, because the browser cache the values, and the recored can be recreated over an over again. 

### Cookies and Sessions
HTTP is a stateless protocol, the server sees each HTTP page as a standalone operation. No history. 

that's why cookies are used.

- cookies: it is a piece of data that the server save on your compute to reuse information about you.vthis is how it works: cookies are set in one page and are available either when you reload the page or go to another page. when you 1st set your cookie, you won't be able to see it in the 1st page. Cookies are unsecure and sessions come to the rescue
- sessions: randomliy generated string saved on your compute and points back to the data on the server. the data on the website is also encrypted, hard to decode

you have to have randomly generate secret to encrypt the cookie
you can generate one : python -c "import os; print(os.urandom(16))"
