import argparse

from internal.exporter import CLIExporter, CSVExporter
from internal.loader import CSVInputLoader
from internal.weighters import *

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file-name", help="Input file", required=True)
parser.add_argument("-m", "--method", help="Weighting method", required=True)
parser.add_argument("-o", "--output", help="Output File Path")


def get_weighter(weighter_name) -> WeighterBase:
    weighter = {
        "least-squares": LeastSquaresWeighter,
        "eigen-vector": EigenvectorWeighter,
    }

    if weighter_name not in weighter:
        raise Exception("Invalid solving method.")

    return weighter[weighter_name]


if __name__ == "__main__":
    args = parser.parse_args()
    priority_set = CSVInputLoader(file_name=args.file_name).load()

    weighter_class = get_weighter(args.method)
    weighter_instance = weighter_class(priority_set=priority_set)
    weights = weighter_instance.weight()

    if args.output is not None:
        exporter = CSVExporter(file_name=args.output)
    else:
        exporter = CLIExporter()

    exporter.export(weights)
