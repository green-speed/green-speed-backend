# importing the requests library
import requests

# api-endpoint
URL = "https://ipchannels.integreen-life.bz.it/ninja/api/v2/flat/BikesharingStation"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'limit': -1, 'offset': 0, 'shownull': False, 'distinct': True}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

for el in data['data']:
    print(el)
