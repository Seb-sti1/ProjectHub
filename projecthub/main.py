from .parsers import parse_cmd

def main():
    args = parse_cmd()

    match args.cmd:
        case "utils":
            print("Hello, World!" if args.hello else "Not hello world!")
        case _:
            print("Please use a valid subcommand.")
