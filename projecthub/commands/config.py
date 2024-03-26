"""Implement the `config` command logic"""
from argparse import ArgumentParser, Namespace

from projecthub.config import Config, Settings


def setup_parser(parser: ArgumentParser) -> None:
    """Setup the config parser"""
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-e", "--edit", nargs=2, metavar=("FIELD", "VALUE"),
        help="Add the field and the desired value."
    )
    group.add_argument(
        "--show", metavar="FIELD",
        help="Show the value of the given field."
    )
    group.add_argument(
        "--list-env-var", action="store_true", default=False,
        help="Display the settings configured via environment variables."
    )
    group.add_argument(
        "-ls", "--list", action="store_true", default=False,
        help="Display the configuration."
    )


def exec_cmd(args: Namespace) -> None:
    """Execute the config command depending on the arguments."""
    if args.edit is not None:
        setattr(Config, *args.edit)
        args.show = args.edit[0]  # not saved to disk for now we print it instead

    if args.show is not None:
        return print(">", getattr(Config, args.show))

    if args.list:
        return print(Config.model_dump_json(indent=4))

    if args.list_env_var:
        return print(Settings.model_dump_json(indent=4))
