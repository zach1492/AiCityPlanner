# AI City Planner

This project is an AI that uses a genetic algorithm paried with a Neural Network is tasked with maximising the citys population within 10 turns. The AI has the choice of placing several types of buildings on a 5 by 5 grid that start with a road in the middle. 

The choice of buildings are
 1. Road - Cost 1 - Buildings are required to be placed next to a road
 2. House - Cost 1 - Houses provides 1 population
 3. Office - Cost 6 - Offices provides 3 money money per turn
 4. Factory - Cost 3 - Factory provides 3 money money per turn but - 1 population
 5. Apartment - Cost 5 - Apartment provides 1 population per turn
 6. Park - Cost 2 - Provides 1 pop per adjacent House and Apartment

The script runs multiple agents over multiple generations and selects the best ones for the next generation and recombines them together and mutates them a bit, new ones are also added in for diversity.

## Technologies
 • Python
 • Terminal

## Features
 • Runs the algorithm and out puts the best city for each generation

 ## Commands
 ```console
python3 train.py
```
