from flask import Flask, escape, render_template, request, redirect, url_for

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

# @app.route('/form', methods=['GET'])
# def form():
#     first_name = request.args.get('first_name')
#     last_name = request.args.get('last_name')
#     return f'Fist Name: {first_name}, Last Name: {last_name}'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        return redirect(url_for('registered'))
    return render_template('form.html')

@app.route('/thankyou')
def registered():
    return 'Thank you!'