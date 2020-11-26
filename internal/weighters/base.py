from abc import abstractmethod

from internal.data_structures import PrioritySet, Weights


class WeighterBase:
    def __init__(self, priority_set: PrioritySet) -> None:
        self.priority_set = priority_set

    @abstractmethod
    def weight(self) -> Weights:
        pass
