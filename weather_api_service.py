from datetime import datetime
from typing import NamedTuple

from enum import Enum

from .gps_coordinates import Coordinates

Celsius = int


class WeatherType(Enum):
    SUNNY = "Sunny"
    RAINY = "Rainy"
    CLOUDY = "Cloudy"
    SNOWY = "Snowy"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Return the weather for the given GPS coordinates."""
    pass
