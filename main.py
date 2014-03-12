from flask import abort, Flask, jsonify, request, url_for

from sharded_counter import (GeneralCounterShardConfig as Counter, get_count,
                             increment)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    """Return a link to the counters collection."""
    return jsonify(counters=url_for('create_counter', _external=True))


@app.route('/counters/', methods=['POST'])
def create_counter():
    """Create a new counter and return its id and URL."""
    counter_id = str(Counter().put().integer_id())
    url = url_for('get_counter', counter_id=counter_id, _external=True)
    response = jsonify(id=counter_id, url=url)
    response.status_code = 201
    response.headers.add('Location', url)
    return response


@app.route('/counters/<int:counter_id>', methods=['GET', 'PUT'])
def get_counter(counter_id):
    """Get or increment the current value of a counter."""
    if Counter.get_by_id(counter_id) is None:
        abort(404)
    counter_id = str(counter_id)

    if request.method == 'PUT':
        increment(counter_id)

    return jsonify(id=counter_id, url=request.url, count=get_count(counter_id))
