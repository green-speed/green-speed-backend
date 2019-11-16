import logging
import os

import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin
from flask import request

from datamodel import get_sample_transportation_options
from osm_api import get_coordinates_by_name
from get_closest_bus_station_example import get_closest_stations
from closest_stations_api import get_closest_bikes, get_closest_carsharing

app = Flask(__name__)
CORS(app)

current_script_location = os.path.realpath(__file__)
root_package_dir = os.path.dirname(current_script_location)

logging.basicConfig()
#logging.basicConfig(filename='information.log', level=logging.DEBUG)

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
def get_directions():
    from_location = request.args.get('from') #if key doesn't exist, returns None
    to_location = request.args.get('to')
    logging.info(f'post request received from: {from_location}; to: {to_location}')
    from_coords = get_coordinates_by_name(from_location)
    logging.info(f'name of location: {from_location}; coordinates on street map: {from_coords}')
    to_coords = get_coordinates_by_name(to_location)
    logging.info(f'name of location: {to_location}; coordinates on street map: {to_coords}')
    if from_location or to_location:
        logging.info(f'Getting closest bus stations..')
        buses_from = get_closest_stations(current_long=float(from_coords[0]), current_lat=float(from_coords[1]))
        logging.info(f'closest bus stations to <from> point: {buses_from}')
        buses_to = get_closest_stations(current_long=float(to_coords[0]), current_lat=float(to_coords[1]))
        logging.info(f'closest bus stations to the <to> point: {buses_to}')
        bikes = get_closest_bikes()
        logging.info(f'closest bikes to the <to> point: {bikes}')
        carsharing = get_closest_carsharing()
        logging.info(f'closest carsharings to the <to> point: {carsharing}')
        sample_transportation_options = get_sample_transportation_options()
        logging.info(f'transportation options are calculated as follows: {sample_transportation_options}')
        return jsonify({"data": [sample_transportation_options]})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
