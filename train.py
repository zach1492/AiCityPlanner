import random
import numpy as np
from game import *
from nn import NeuralNet, get_action

POP_SIZE = 30
MUTATION_RATE = 0.3 
ELITE_SIZE = 10
RANDOM_INJECT = 0.1      

def evaluate(nn):
    grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
    grid[2][2] = ROAD

    state = {"money": 10, "population": 0, "turn": 0}
    apartments_age = {}

    for t in range(100):
        state["generation"] = t

        action = get_action(nn, grid, state, valid_build)
        if action:
            apply_action(grid, state, action)

        update_resources(grid, state, apartments_age)

    return state["population"], grid, state


population = [NeuralNet() for _ in range(POP_SIZE)]

for gen in range(100):
    results = [evaluate(nn) for nn in population]
    scores = [(r[0], nn, r[1], r[2]) for nn, r in zip(population, results)]

    scores.sort(key=lambda x: x[0], reverse=True)

    best_score, best_nn, best_grid, best_state = scores[0]

    print("\nGen", gen, "Best:", best_score)
    print_board_state(best_grid, best_state)

    top = [nn for _, nn, _, _ in scores[:ELITE_SIZE]]

    new_pop = []

    for nn in top:
        clone = NeuralNet()
        clone.W1 = nn.W1.copy()
        clone.W2 = nn.W2.copy()
        new_pop.append(clone)

    while len(new_pop) < POP_SIZE:
        if random.random() < RANDOM_INJECT:
            new_pop.append(NeuralNet())
        else:
            parent = random.choice(top)
            child = NeuralNet()
            child.W1 = parent.W1 + np.random.randn(*parent.W1.shape) * MUTATION_RATE
            child.W2 = parent.W2 + np.random.randn(*parent.W2.shape) * MUTATION_RATE
            new_pop.append(child)

    population = new_pop
