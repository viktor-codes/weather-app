from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> tuple[float, float]:
    """Return the GPS coordinates of current location."""
    return Coordinates(latitude=53.353323157609665, longitude=-6.266140035810221)
