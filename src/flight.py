# Flight parameters/code

from rocketpy import Flight
from src import environment, rocket

test_flight = Flight(
  rocket=rocket.calisto, environment=environment.environment, rail_length=5.2, inclination=85, heading=0, verbose=True
)
