# project/__init__.py
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

app.config.from_envvar('APP_CONFIG_FILE')
