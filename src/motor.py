# Motor parameters/code

from rocketpy import SolidMotor


def get_motor(cfg):
    Pro75M1670 = SolidMotor(
        thrust_source="../data/motors/Cesaroni_7312M4770-P.eng",
        dry_mass=2.924,
        dry_inertia=(0.249, 0.249, 0.351),
        center_of_dry_mass_position=0.317,
        grains_center_of_mass_position=0.274,
        burn_time=1.617,
        grain_number=3,
        grain_separation=0.005,
        grain_density=1815,
        grain_outer_radius=0.033,
        grain_initial_inner_radius=0.015,
        grain_initial_height=0.12,
        nozzle_radius=0.033,
        throat_radius=0.011,
        interpolation_method="linear",
        nozzle_position=0,
        coordinate_system_orientation="nozzle_to_combustion_chamber", )

    return Pro75M1670
