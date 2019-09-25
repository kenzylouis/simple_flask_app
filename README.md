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



