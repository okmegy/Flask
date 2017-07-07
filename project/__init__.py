# project/__init__.py

from flask import Flask, jsonify
from flask import render_template
from project import view

# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/', methods=['GET'])
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/hello/<name>')
def hello(name):
    return "Hello %s" % name

# entry
if __name__ == '__main__':
    app.run(debug=True)
