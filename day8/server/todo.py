from flask_restful import reqparse, abort, Api, Resource

TODOLIST = {"item1": "100 days of coding"}


class Todo(Resource):
    def __init__(self):
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('item')

    def get(self, id):
        if id not in TODOLIST.keys():
            abort(404, message="Item not found")

        return TODOLIST[id]

    def delete(self, id):
        if id not in TODOLIST.keys():
            abort(404, message="Item not found")

        del TODOLIST[id]

    def put(self, id):
        args = self._parser.parse_args()
        item = args['item']
        TODOLIST[id] = item
        return item, 201
