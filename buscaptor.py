__author__ = 'boondaburrah'
from alexa import Intent
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def say_hello():
    return "Hello, this is not where you're supposed to be."


@app.route('/alexa', methods=['POST'])
def handle_echo():
    try:
        alexa = Intent(request.get_json(force=True))
    except RuntimeError:
        return "Not an intent"
    return alexa.get_type()

if __name__ == '__main__':
    app.run()