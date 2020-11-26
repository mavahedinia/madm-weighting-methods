import csv
from abc import ABC

from prettytable import PrettyTable

from internal.data_structures import PrioritySet, Weights


class ExporterBase(ABC):
    def __init__(self) -> None:
        pass

    def export(self, weights: Weights):
        pass


class CLIExporter(ExporterBase):
    def export(self, weights: Weights):
        table = PrettyTable()

        table.add_row(weights.attrs)
        table.add_row(weights.weights)

        print(table.get_string(header=False, border=True))


class CSVExporter(ExporterBase):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def export(self, weights: Weights):
        with open(self.file_name, mode="w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow(weights.attrs)
            csv_writer.writerow(weights.weights)
