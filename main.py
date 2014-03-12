from flask import abort, Flask, request

from sharded_counter import (GeneralCounterShardConfig as Counter, get_count,
                             increment)

app = Flask(__name__)


@app.route('/counters/', methods=['POST'])
def create_counter():
    """Create a new counter and return its id and URL."""
    counter_id = str(Counter().put().integer_id())
    return str({'id': counter_id}), 201


@app.route('/counters/<int:counter_id>', methods=['GET', 'PUT'])
def get_counter(counter_id):
    if Counter.get_by_id(counter_id) is None:
        abort(404)
    counter_id = str(counter_id)

    if request.method == 'PUT':
        increment(counter_id)

    return str({'count': get_count(counter_id)})
