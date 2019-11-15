import requests
import numpy as np


def get_closest_stations(current_lat,
                         current_long,
                         list_ort_nr,
                         list_lat,
                         list_long,
                         list_ort_name,
                         list_ort_gemeinde,
                         amount_to_get=2):
    list_distances = []
    for i in range(len(list_ort_nr)):
        list_distances.append(abs(list_lat[i] - current_lat) + abs(list_long[i] - current_long))
    result_list = []
    result_names_list = []
    result_gemeinde_list = []
    for i in range(amount_to_get):
        num_min = np.argmin(list_distances)
        result_list.append(list_ort_nr[num_min])
        result_names_list.append(list_ort_name[num_min])
        result_gemeinde_list.append(list_ort_gemeinde[num_min])
        list_ort_nr = np.delete(list_ort_nr, num_min)
        list_lat = np.delete(list_lat, num_min)
        list_long = np.delete(list_long, num_min)
        list_distances = np.delete(list_distances, num_min)
        list_ort_name = np.delete(list_ort_name, num_min)
        list_ort_gemeinde = np.delete(list_ort_gemeinde, num_min)
    return result_list, result_names_list, result_gemeinde_list


# api-endpoint
URL = "http://opensasa.info/SASAplandata/"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'type': 'REC_ORT'}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# It represents a list of the bus stops and their information.
list_ort_nr = []
list_lat = []
list_long = []
list_ort_name = []
list_ort_gemeinde = []

for el in data:
    for busstop in el['busstops']:
        list_ort_nr.append(busstop['ORT_NR'])
        list_lat.append(busstop['ORT_POS_BREITE'])
        list_long.append(busstop['ORT_POS_LAENGE'])
        list_ort_name.append(el['ORT_NAME'])
        list_ort_gemeinde.append(el['ORT_GEMEINDE'])


stations, station_names, station_gemeinde = get_closest_stations(
    current_lat=56,
    current_long=45,
    list_ort_nr=list_ort_nr,
    list_lat=list_lat,
    list_long=list_long,
    list_ort_name=list_ort_name,
    list_ort_gemeinde=list_ort_gemeinde
)

print('2 closest stations to curretn location is')
print('station number: ', stations[0], 'ort name: ', station_names[0], 'ort gemeinde: ', station_gemeinde[0])
print('station number: ', stations[1], 'ort name: ', station_names[1], 'ort gemeinde: ', station_gemeinde[1])

