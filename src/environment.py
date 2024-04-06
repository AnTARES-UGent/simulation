# Environment paramters/code

from rocketpy import Environment
import datetime

environment = Environment(
    latitude=32.990254,
    longitude=-106.974998,
    elevation=1400,
)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

environment.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12), timezone="America/Denver"
)  # Tomorrow's date in year, month, day, hour UTC format

environment.set_atmospheric_model(type='standard_atmosphere')
