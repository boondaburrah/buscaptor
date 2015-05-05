__author__ = 'boondaburrah'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def sayhello():
    return "Hello, this is not where you're supposed to be."

if __name__ == '__main__':
    app.run()