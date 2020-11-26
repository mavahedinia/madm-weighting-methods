import numpy as np
from internal.data_structures import Weights
from internal.weighters.base import WeighterBase
from scipy.optimize import minimize


class LeastSquaresWeighter(WeighterBase):
    def weight(self) -> Weights:
        weights = Weights(self.priority_set)

        initial_guess = [1.0 / len(weights.attrs)] * len(weights.attrs)

        weights.weights = minimize(
            self._cost,
            initial_guess,
            args=(self._get_comparison_matrix_np(),),
            method="SLSQP",
            bounds=[(0.0, 1e10)] * len(weights.attrs),
            constraints={"type": "eq", "fun": lambda x: sum(x) - 1},
        ).x
        return weights

    def _get_comparison_matrix_np(self):
        comparison_matrix = []
        for row in self.priority_set.matrice[1:]:
            comparison_matrix.append(row[1:])
        comparison_matrix = np.array(comparison_matrix)

        return comparison_matrix

    @staticmethod
    def _cost(theta, *args):
        return sum(np.power(args[0].dot(theta) - theta, 2))
