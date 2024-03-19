"""Utils command -- A dummy command"""
from argparse import ArgumentParser

def setup_parser(parser: ArgumentParser) -> None:
    """Example: Setup a dummy "utils" sub-parser."""
    parser.add_argument("--hello", action="store_true")
