import numpy as np

GRID_SIZE = 5
NUM_BUILDINGS = 6
NUM_ACTIONS = GRID_SIZE * GRID_SIZE * NUM_BUILDINGS

INPUT_SIZE = GRID_SIZE * GRID_SIZE + 3  

class NeuralNet:
    def __init__(self):
        self.W1 = np.random.randn(INPUT_SIZE, 32)
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
    ], dtype=float)


BUILDING_IDS = [ROAD, HOUSE, OFFICE, FACTORY, APARTMENT, PARK] = [1, 2, 3, 4, 5, 6]

def get_action(nn, grid, state, valid_build):
    output = nn.forward(encode(grid, state))

    best = None
    best_score = -1e9

    for i in range(NUM_ACTIONS):
        tile = i // NUM_BUILDINGS
        building = BUILDING_IDS[i % NUM_BUILDINGS]
        x, y = tile // GRID_SIZE, tile % GRID_SIZE

        if valid_build(grid, x, y, building, state["money"]):
            if output[i] > best_score:
                best_score = output[i]
                best = (x, y, building)

    return best
