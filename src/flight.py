# Flight parameters/code

from rocketpy import Flight
from src import environment, rocket


def create_flight(cfg_file):
    """
    Arguments:

    Returns:

    """

    calisto = rocket.create_rocket(cfg_file)
    envir = environment.create_environment(cfg_file)

    test_flight = Flight(rocket=calisto, environment=envir, rail_length=5.2, inclination=84, heading=0, verbose=True)

    return test_flight
