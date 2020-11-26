import numpy as np
from internal.data_structures import Weights
from internal.weighters.base import WeighterBase


class EigenvectorWeighter(WeighterBase):
    def weight(self) -> Weights:
        weights = Weights(self.priority_set)
        eig = np.linalg.eig(self.priority_set.get_comparison_matrix_np())
        max_landa = max(eig[0][eig[0] == eig[0].real].real)
        weights_np = eig[1][eig[0] == max_landa].real
        weights.weights = weights_np[0]
        return weights
