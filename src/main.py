import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

from rocketpy import Environment, Flight, Function, Rocket, SolidMotor

plt.style.use("seaborn-v0_8-dark-palette")

parameters = {
    # Mass Details
    "rocket_mass": (18.998, 0.010),  # Rocket dry mass: 20.846 kg
    # propulsion details
    "motor_structure_mass": (1.848, 0.1),
    "burn_time": (3.433, 0.1),
    "nozzle_radius": (0.02475, 0.001),
    "throat_radius": (0.01075, 0.001),
    "grain_separation": (0.003, 0.001),
    "grain_density": (1519.708, 30),
    "grain_outer_radius": (0.033, 0.001),
    "grain_initial_inner_radius": (0.015, 0.002),
    "grain_initial_height": (0.12, 0.001),
    "grains_center_of_mass_position": (-0.35, 0.100),
    "nozzle_position": (0, 0.100),
    "motor_position": (3.391, 0.100),
    # aerodynamic details
    "center_of_mass_without_motor": (1.3, 0.100),
    "drag_coefficient": (0.44, 0.1),
    "inertia_i": (73.316, 0.3 * 73.316),
    "inertia_z": (0.15982, 0.3 * 0.15982),
    "radius": (0.1015, 0.001),
    "power_off_drag": (1, 0.033),
    "power_on_drag": (1, 0.033),
    # nose cone
    "nose_length": (0.610, 0.001),
    "nose_radius": (0.1015, 0.001),
    "nose_position": (0, 0.100),
    # fins
    "fin_span": (0.165, 0.001),
    "fin_root_chord": (0.152, 0.001),
    "fin_tip_chord": (0.0762, 0.001),
    "fin_sweep_angle": (13, 0.5),
    "fin_position": (3.050, 0.100),
    # transitions
    "transition_top_radius": (0.1015, 0.010),
    "transition_bottom_radius": (0.0775, 0.010),
    "transition_length": (0.127, 0.010),
    "transition_position": (1.2, 0.010),
    # launch and environment details
    "wind_direction": (0, 3),
    "wind_speed": (1, 0.30),
    "inclination": (90, 1),
    "heading": (181, 3),
    "rail_length": (3.353, 0.001),
    # parachute details
    "cd_s_drogue": (1.5 * np.pi * (24 * 25.4 / 1000) * (24 * 25.4 / 1000) / 4, 0.1),
    "cd_s_main": (2.2 * np.pi * (120 * 25.4 / 1000) * (120 * 25.4 / 1000) / 4, 0.1),
    "lag_rec": (1, 0.5),
}
