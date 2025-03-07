#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path

from snakebids.app import SnakeBidsApp
from snakebids.cli import add_dynamic_args


def get_parser() -> ArgumentParser:
    """Exposes parser for sphinx doc generation, working directory is the docs dir."""
    app = SnakeBidsApp(".", skip_parse_args=True)
    add_dynamic_args(app.parser, app.config["parse_args"], app.config["pybids_inputs"])
    return app.parser


def main() -> None:
    app = SnakeBidsApp(Path(__file__).parent.absolute())
    app.run_snakemake()


if __name__ == "__main__":
    main()
