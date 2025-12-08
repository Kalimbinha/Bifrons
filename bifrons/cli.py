import argparse

from core import process

def main():
    parser = argparse.ArgumentParser(description="VersioneerX - SemVer CLI")
    parser.add_argument("--title", required=True, help="Título da PR/commit")
    args = parser.parse_args()

    process(args.title)
