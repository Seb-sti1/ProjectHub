"""Parsers module -- It is in charge of parsing the command using the various subparsers."""
from typing import Callable, Optional
from pathlib import Path
import importlib
from argparse import ArgumentParser, Namespace


# each file with the convention `[cmd_name].py` contains parsing utilities for the given command
COMMANDS = [
    path.stem for path in Path(__file__).parent.resolve().glob("*.py")
    if path.stem != "__init__"
]


class UnknownCommand(Exception):
    """Raised when the command provided doesn't exists."""
    def __init__(self, cmd: str) -> None:
        super().__init__()
        self.cmd = cmd

    def __str__(self) -> str:
        if self.cmd:
            return f"{self.cmd} is not a valid command."
        return "please use "


def _parser_factory(cmd: str) -> Callable[[ArgumentParser], None]:
    module = importlib.import_module(f"projecthub.parsers.{cmd}")
    return getattr(module, "setup_parser")


def parse_cmd(raw_args: Optional[list[str]] = None) -> Namespace:
    """Parse the arguments from the command line.

    Args:
        raw_args (list[str], optional): If given, parse the supplied arguments
            instead of using the arguments from the command line.
            example: ["--foo", "bar"]. The default (None) is equivalent to `sys.argv[1:]`. 

    Returns:
        Namespace: The parsed arguments.
    """
    # create the global parser
    parser = ArgumentParser(
        prog="projecthub",
        description="Manage all your projects on your Unix machine!",
        epilog=(
            "If you want to contribute, you can find our github here: "
            "https://github.com/Seb-sti1/ProjectHub"
        )
    )

    sub_parsers = parser.add_subparsers(dest="cmd", metavar="CMD", help="The desired command.")

    # Add all available commands as a subparser
    for cmd in COMMANDS:
        sub_parser = sub_parsers.add_parser(cmd)
        _parser_factory(cmd)(sub_parser)

    return parser.parse_args(raw_args)
