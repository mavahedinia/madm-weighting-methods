import csv
from abc import ABC, abstractmethod

from internal.data_structures import PrioritySet


class InputLoader(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def load(self) -> PrioritySet:
        pass


class CSVInputLoader(InputLoader):
    def __init__(self, file_name: str, *args, **kwargs):
        self.file_name = file_name
        super().__init__(*args, **kwargs)

    def load(self) -> PrioritySet:
        priority_set = PrioritySet()
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                priority_set.matrice.append(row)
        priority_set.validate()
        return priority_set


class CSVExtraInputLoader:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def load(self):
        extra_input = []
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                extra_input.append(row)

        return extra_input
