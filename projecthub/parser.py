from typing import Optional, Literal
from argparse import ArgumentParser
from pydantic import BaseModel, Field

Command = Literal["utils"]

class Arguments(BaseModel):
    cmd: Optional[Command] = Field(
        description="Name of the command invoked."
    )
    # `hello` property is created only when cmd == utils...


def parse_args(raw_args: Optional[list[str]] = None) -> Arguments:
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

    # add all the sub parsers:
    sub_parsers = parser.add_subparsers(dest="cmd")
    utils_parser = sub_parsers.add_parser("utils")
    setup_utils_parser(utils_parser)

    args = parser.parse_args(raw_args)
    return Arguments(**vars(args))


def setup_utils_parser(parser: ArgumentParser) -> None:
    """Example: Setup a dummy "utils" sub-parser."""
    parser.add_argument("--hello", action="store_true")
