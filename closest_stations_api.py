import logging

import requests


def calc_diff_between_coords():
    pass


def get_closest_bikes():
    logging.info("Getting closest bike sharing stations...")
    URL = "https://ipchannels.integreen-life.bz.it/ninja/api/v2/flat/BikesharingStation"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'limit': -1, 'offset': 0, 'shownull': False, 'distinct': True}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()['data']
    locations = list(map(lambda e: (e['scoordinate']['x'], e['scoordinate']['y']), data))
    #TODO add sorting by closest location
    return locations


def get_closest_carsharing():
    logging.info("Getting closest carsharing sharing stations...")
    URL = "https://ipchannels.integreen-life.bz.it/ninja/api/v2/flat/CarsharingCar"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'limit': -1, 'offset': 0, 'shownull': False, 'distinct': True}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()['data']
    all = set()
    for elm in data:
        if 'pcoordinate' in elm:
            all.add((elm['pcoordinate']['x'], elm['pcoordinate']['y']))
    #TODO add sorting by closest location
    return all