import argparse

from .core import Bifrons


class BifronsCLI:
    def execute(self):
        parser = argparse.ArgumentParser(description="Bifrons - CLI")
        parser.add_argument("--title", required=True, help="Título da PR/commit")
        args = parser.parse_args()

        try:
            Bifrons().execute(args.title)
            return 0
        except ValueError as e:
            print(f"Erro: {e}")
            return 1
