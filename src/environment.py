# Environment paramters/code

from rocketpy import Environment
import datetime


def create_environment(cfg):
    # UGent campus Sterre
    environment = Environment(
        latitude=51.0229823,
        longitude=3.7103475,
        elevation=20,
    )

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    environment.set_date(
        (tomorrow.year, tomorrow.month, tomorrow.day, 12), timezone="America/Denver"
    )  # Tomorrow's date in year, month, day, hour UTC format

    environment.set_atmospheric_model(type="Forecast", file="GFS")

    environment.all_info()

    return environment
