import requests

# api-endpoint
URL = "http://opensasa.info/SASAplandata/"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'type': 'REC_ORT'}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# It represents a list of the bus stops and their information.
print(data)
