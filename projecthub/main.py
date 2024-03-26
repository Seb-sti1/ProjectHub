import argparse
from .commands import config as cmd_config


def main():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(dest="cmd")
    cmd_config.setup_parser(sub_parsers.add_parser("config"))
    args = parser.parse_args()

    match args.cmd:
        case "config":
            cmd_config.exec_cmd(args)
