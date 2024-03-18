from . import parse_args

def main():
    args = parse_args()

    match args.cmd:
        case "utils":
            print("Hello, World!" if args.hello else "Not hello world!")
        case _:
            print("Please use a valid subcommand.")
