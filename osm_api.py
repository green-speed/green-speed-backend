import requests
from typing import Tuple


def get_coordinates_by_name(name: str) -> Tuple[str, str]:
    '''
        method from string to coordinates
    '''
    params = {'q': name, 'format': 'json'}
    a = requests.get("https://nominatim.openstreetmap.org/search", params=params)
    res = a.json()
    return res[0]['lon'], res[0]['lat']


coords = get_coordinates_by_name('lago di caldaro')
print(coords)