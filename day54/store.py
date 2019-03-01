from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'item1',
        'items': [
            {
                'name': 'Some item',
                'price': 15.32
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    return jsonify(_get_store(name))


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    store = _get_store(name)

    if store:
        store['items'].append({
            'name': request_data['name'],
            'price': request_data['price']
        })
        return jsonify(store)

    return jsonify({'message:' 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    store = _get_store(name)
    return jsonify({'items': store['items']})


def _get_store(name):
    for store in stores:
        if store['name'] == name:
            return store

    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
