from datetime import datetime
from typing import NamedTuple

from enum import Enum

from .gps_coordinates import Coordinates

Celsius = int


class WeatherType(Enum) -> None:
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
    """Requests weather data from an weatherapi.com and returns it."""
    return Weather(
				temperature=20,
				weather_type=WeatherType.SUNNY,
				sunrise=datetime.now(),
				sunset=datetime.now(),
				city="London",
		)
    
