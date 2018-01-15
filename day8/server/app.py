#!flask/bin/python
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, '/todos/<id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')