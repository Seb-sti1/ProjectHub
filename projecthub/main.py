import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hello", required=False)
    args = parser.parse_args()

    if args.hello is not None:
        print("Hello, World!")
    else:
        print("Not Hello, World!")
