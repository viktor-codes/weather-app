from datetime import datetime
from typing import NamedTuple

from .gps_coordinates import Coordinates

Celsius = int


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Return the weather for the given GPS coordinates."""
    pass
