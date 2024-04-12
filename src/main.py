import flight
import argparse

def add_dict_to_argparser(parser, default_dict):
    for k, v in default_dict.items():
        v_type = type(v)
        if v is None:
            v_type = str
        elif isinstance(v, bool):
            v_type = str2bool
        parser.add_argument(f"--{k}", default=v, type=v_type)


def args_to_dict(args, keys):
    return {k: getattr(args, k) for k in keys}

parser = argparse.ArgumentParser()
defaults = {"cfg": './cfg/design.yaml'}
add_dict_to_argparser(parser, defaults)


# Current test-simulation from: https://docs.rocketpy.org/en/latest/#running-your-first-simulation
if __name__ == "__main__":
    args = args_to_dict(parser.parse_args(), defaults.keys())

    test_flight = flight.create_flight(cfg_file=args["cfg"])
    
    test_flight.info()
    test_flight.all_info()
