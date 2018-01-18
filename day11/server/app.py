#!flask/bin/python
from flask import Flask
from todo import todo_api

app = Flask(__name__)
app.register_blueprint(todo_api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')