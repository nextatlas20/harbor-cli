"""Harbor CLI entry point."""

import argparse


def build_parser():
    parser = argparse.ArgumentParser(prog="harbor")
    parser.add_argument("--profile", default="default")
    parser.add_argument("--retry", type=int, default=3)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    print(f"harbor profile={args.profile} retry={args.retry}")


if __name__ == "__main__":
    main()
