import argparse
from . import Config, Settings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hello", required=False)
    args = parser.parse_args()

    print("Settings:", Settings)
    print("Config:", Config)

    if args.hello is not None:
        print("Hello, World!")
    else:
        print("Not Hello, World!")
