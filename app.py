import logging
import os

import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin
from flask import request

from datamodel import get_sample_transportation_options

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

current_script_location = os.path.realpath(__file__)
root_package_dir = os.path.dirname(current_script_location)

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True



@app.route('/route')
def find_bus():
    from_x = request.args.get('from_x') #if key doesn't exist, returns None
    from_y = request.args.get('from_y')
    to_x = request.args.get('to_x')
    to_y = request.args.get('to_y')
    print('from_x: ', from_x)
    print('from_y: ', from_y)
    print('to_x: ', to_x)
    print('to_y: ', to_y)
    return '''<h1>from_x: {}</h1>'''.format(from_x)


@app.route('/api/v1/directions')
@cross_origin()
def get_directions():
    from_location = request.args.get('from') #if key doesn't exist, returns None
    to_location = request.args.get('to')
    if from_location or to_location:
        sample_transportation_options = get_sample_transportation_options()
        return jsonify(sample_transportation_options)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)


