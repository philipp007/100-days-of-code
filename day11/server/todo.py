from flask_restful import abort
from flask import Blueprint, request, jsonify


TODOLIST = {"item1": "100 days of coding"}
todo_api = Blueprint('todo', 'todo', url_prefix='/todos')


@todo_api.route('/', methods=['GET'])
def api_list():
    return jsonify(list(TODOLIST.items()))


@todo_api.route('/<item_id>', methods=['GET', 'DELETE', 'PUT'])
def api_item(item_id):
    if request.method == 'GET':
        return get_item(item_id)
    elif request.method == 'PUT':
        return put_item(item_id)
    else:
        delete_item(item_id)


def get_item(item_id):
    if item_id not in TODOLIST.keys():
        abort(404, message="Item not found")

    return TODOLIST[item_id]


def put_item(item_id):
    item = request.values['item']
    TODOLIST[item_id] = item
    return item, 201


def delete_item(item_id):
    if item_id not in TODOLIST.keys():
        abort(404, message="Item not found")

    del TODOLIST[item_id]