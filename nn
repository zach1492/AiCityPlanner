import numpy as np

GRID_SIZE = 5
NUM_BUILDINGS = 6
NUM_ACTIONS = GRID_SIZE * GRID_SIZE * NUM_BUILDINGS 

class NeuralNet:
    def __init__(self):
        self.W1 = np.random.randn(28, 32)
        self.W2 = np.random.randn(32, NUM_ACTIONS)

    def forward(self, x):
        x = np.tanh(x @ self.W1)
        return x @ self.W2


def encode(grid, state):
    flat = [cell for row in grid for cell in row]
    return np.array(flat + [
        state["money"],
        state["population"],
        state["generation"]
    ])


def get_action(nn, grid, state, valid_build):
    output = nn.forward(encode(grid, state))

    best = None
    best_score = -1e9

    for i in range(NUM_ACTIONS):
        tile = i // 6
        building = (i % 6) + 1
        x, y = tile // 5, tile % 5

        if valid_build(grid, x, y, building, state["money"]):
            if output[i] > best_score:
                best_score = output[i]
                best = (x, y, building)

    return best
