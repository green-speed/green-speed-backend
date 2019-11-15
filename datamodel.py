from dataclasses import dataclass
from enum import Enum

from typing import List


class TransportationType(str, Enum):
    BIKE = 'bike'
    BUS = 'bus'
    TRAIN = 'train'
    WALKING = 'walking'
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
