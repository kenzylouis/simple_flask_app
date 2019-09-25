from flask import Flask, escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello_world():
    return "Hello, World" 

@app.route('/hello/<name>')
def hello(name):
    return "Hello, " + name

## https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post  {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)