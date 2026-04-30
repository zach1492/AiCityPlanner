import random
import numpy as np
from game import *
from nn import NeuralNet, get_action

POP_SIZE = 30

def evaluate(nn):
    grid = [[0]*5 for _ in range(5)]
    grid[2][2] = ROAD

    state = {"money":10, "population":0, "generation":0}
    apartments_age = {}

    for t in range(50):
        state["generation"] = t

        action = get_action(nn, grid, state, valid_build)
        if action:
            apply_action(grid, state, action)

        update_resources(grid, state, apartments_age)

    return state["population"]


population = [NeuralNet() for _ in range(POP_SIZE)]

for gen in range(100):
    scores = [(evaluate(nn), nn) for nn in population]
    scores.sort(key=lambda x: x[0], reverse=True)

    print("Gen", gen, "Best:", scores[0][0])
    top = [nn for _, nn in scores[:10]]

    new_pop = top.copy()

    while len(new_pop) < POP_SIZE:
        parent = random.choice(top)
        child = NeuralNet()
        child.W1 = parent.W1 + np.random.randn(*parent.W1.shape) * 0.1
        child.W2 = parent.W2 + np.random.randn(*parent.W2.shape) * 0.1
        new_pop.append(child)

    population = new_pop
