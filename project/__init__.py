# project/__init__.py

from flask import Flask, jsonify
from flask import render_template

# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/hello/<name>')
def hello(name):
    return "Hello %s" % name

# entry
if __name__ == '__main__':
    app.run(debug=True)
