import numpy as np


class PrioritySet:
    def __init__(self):
        self.matrice = []

    def validate(self):
        assert len(self.matrice) > 0
        n = len(self.matrice)
        for i in range(len(self.matrice)):
            assert len(self.matrice[i]) == n
            if i == 0:
                continue
            for j, val in enumerate(self.matrice[i][1:]):
                self.matrice[i][j + 1] = float(val)

    def get_comparison_matrix_np(self):
        comparison_matrix = []
        for row in self.matrice[1:]:
            comparison_matrix.append(row[1:])
        comparison_matrix = np.array(comparison_matrix)

        return comparison_matrix


class Weights:
    def __init__(self, priority_set: PrioritySet):
        self.attrs = []
        self.weights = []

        for attr in priority_set.matrice[0][1:]:
            self.attrs.append(attr)
            self.weights.append(0.0)
