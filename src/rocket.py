# Rocket parameters/code

from rocketpy import Rocket
from src.motor import Pro75M1670
import yaml

with open('./cfg/design1.yaml', 'r') as yaml_file:
    rocket_data = yaml.safe_load(yaml_file)

# Create Rocket object
calisto = Rocket(
    radius=rocket_data['rocket']['radius'],
    mass=rocket_data['rocket']['mass'],
    inertia=tuple(rocket_data['rocket']['inertia']),
    center_of_mass_without_motor=rocket_data['rocket']['center_of_mass_without_motor'],
    power_off_drag="./data/calisto/powerOffDragCurve.csv",
    power_on_drag="./data/calisto/powerOnDragCurve.csv",
    coordinate_system_orientation="tail_to_nose",
)

# Set rail buttons
buttons = calisto.set_rail_buttons(
    upper_button_position=rocket_data['buttons']['upper_button_position'],
    lower_button_position=rocket_data['buttons']['lower_button_position'],
    angular_position=rocket_data['buttons']['angular_position'],
)

# Add motor
calisto.add_motor(Pro75M1670, rocket_data['motor']['position'])

# Add nose
nose = calisto.add_nose(
    length=rocket_data['nose']['length'],
    kind=rocket_data['nose']['kind'],
    position=rocket_data['nose']['position'],
)

# Add fins
fins = calisto.add_trapezoidal_fins(
    n=rocket_data['fins']['n'],
    root_chord=rocket_data['fins']['root_chord'],
    tip_chord=rocket_data['fins']['tip_chord'],
    span=rocket_data['fins']['span'],
    cant_angle=rocket_data['fins']['cant_angle'],
    position=rocket_data['fins']['position'],
)

# Add tail
tail = calisto.add_tail(
    top_radius=rocket_data['tail']['top_radius'],
    bottom_radius=rocket_data['tail']['bottom_radius'],
    length=rocket_data['tail']['length'],
    position=rocket_data['tail']['position'],
)

main = calisto.add_parachute(
    name="main",
    cd_s=10.0,
    trigger=800,  # ejection altitude in meters
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

drogue = calisto.add_parachute(
    name="drogue",
    cd_s=1.0,
    trigger="apogee",  # ejection at apogee
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)
