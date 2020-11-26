from internal.data_structures import Weights
from internal.weighters.base import WeighterBase
from prettytable import PrettyTable


class LeastSquaresWeighter(WeighterBase):
    ALPHA = -0.001
    MAX_ITERATIONS = 10000
    EPS = 1e-3

    def weight(self) -> Weights:
        weights = Weights(self.priority_set)

        LAMBDA = 100

        for _ in range(self.MAX_ITERATIONS):
            w_gradient, l_gradient = self._calculate_gradient(weights.weights, LAMBDA)
            weights, LAMBDA = self._calculate_new_weights((weights.weights, w_gradient), (LAMBDA, l_gradient))
            print(f"weights: {weights.weights}, Lambda: {LAMBDA}")
            print(f"weights_g: {w_gradient}, Lambda_g: {l_gradient}")
            print("------------------------------------------------------")

        return weights

    def _calculate_gradient(self, weights, l):
        w_gradient = [0.0] * len(weights)
        l_gradient = sum(weights) - 1

        # t = PrettyTable()
        # for row in self.priority_set.matrice:
        #     t.add_row(row)

        # print(t.get_string(header=False, border=True))

        for k in range(len(weights)):
            g = 0
            for i in range(len(weights)):
                # print(f"G{g} - I{i} - K{k}")
                # print(f"\t pm{self.priority_set.matrice[i + 1][k + 1]} - wk{weights[k]} - wi{weights[i]}")
                g += self.priority_set.matrice[i + 1][k + 1] * (self.priority_set.matrice[i + 1][k + 1] * weights[k] - weights[i])

            for j in range(len(weights)):
                g -= self.priority_set.matrice[k + 1][j + 1] * weights[j] - weights[k]

            g = 2 * g + l

            w_gradient[k] = g

        return w_gradient, l_gradient

    def _calculate_new_weights(self, w_g, l_g):
        weights = Weights(self.priority_set)
        LAMBDA = l_g[0] + self.ALPHA * l_g[1]

        for i in range(len(weights.weights)):
            weights.weights[i] = w_g[0][i] + self.ALPHA * w_g[1][i]

        return weights, LAMBDA
