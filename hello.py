from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return "Hello, World" 

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', t_name=name)

## https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('post.html', t_post=post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)