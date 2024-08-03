# Motor parameters/code

from rocketpy import SolidMotor


def get_motor(cfg):
    Pro75M1670 = SolidMotor(
        thrust_source="../data/motors/Cesaroni_8187M1545-P.eng",
        dry_mass=2.9655,
        dry_inertia=(0.292, 0.292, 0.0021),
        center_of_dry_mass_position=0.543,
        grains_center_of_mass_position=0.558,
        burn_time=5.29,
        grain_number=6,
        grain_separation=0.005,
        grain_density=1815,
        grain_outer_radius=0.03766,
        grain_initial_inner_radius=0.015,
        grain_initial_height=0.171,
        nozzle_radius=0.033,
        throat_radius=0.011,
        interpolation_method="linear",
        nozzle_position=0,
        coordinate_system_orientation="nozzle_to_combustion_chamber", )

    return Pro75M1670
