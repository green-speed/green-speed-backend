import datetime
from dataclasses import dataclass
from enum import Enum

from typing import List


class TransportationType(str, Enum):
    BIKE = 'bicycle'
    BUS = 'bus'
    TRAIN = 'train'
    WALKING = 'walk'
    CAR_POOLING = 'car_pooling'
    CAR_SHARING = 'car_sharing'


@dataclass
class Leg(object):
    transportation_type: TransportationType


@dataclass
class TransportationOption(object):
    legs: List[Leg]
    total_time: int
    green_score: int
    departure_time: str
    arrival_time: str


@dataclass
class DirectionsResponse(object):
    location_from: str
    location_to: str
    transportation_options: List[TransportationOption]


def format_time(hour: int, minute: int):
    return f'{hour:02d}:{minute:02d}'


def get_sample_transportation_options():
    current_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    departure_time1 = current_time + datetime.timedelta(minutes=2)
    departure_time2 = current_time + datetime.timedelta(minutes=4)
    duration1 = 58
    duration2 = 32
    arrival1 = departure_time1 + datetime.timedelta(minutes=duration1)
    arrival2 = departure_time2 + datetime.timedelta(minutes=duration2)

    return DirectionsResponse(location_from="Hotel Figl", location_to="Lago di Caldaro",
                              transportation_options=[
                                  TransportationOption(green_score=3, total_time=duration1,
                                                       departure_time=format_time(departure_time1.hour, departure_time1.minute),
                                                       arrival_time=format_time(arrival1.hour, arrival1.minute),
                                                       legs=[
                                      Leg(transportation_type=TransportationType.WALKING),
                                      Leg(transportation_type=TransportationType.BIKE),
                                      Leg(transportation_type=TransportationType.WALKING)
                                  ]),
                                  TransportationOption(green_score=2, total_time=duration2,
                                                       departure_time=format_time(departure_time2.hour, departure_time2.minute),
                                                       arrival_time=format_time(arrival2.hour, arrival2.minute),
                                                       legs=[
                                                           Leg(transportation_type=TransportationType.WALKING),
                                                           Leg(transportation_type=TransportationType.BUS)
                                                       ]),
                              ])