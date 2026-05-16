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

## Process

To start making the game I made a basic game script that controls the rules of the city game; valid placements, costs, resource collection etc

Then I added in the genetic algorithm to start off the AI 

I really wanted to use a neural network in this project so I added one in to the AI

After this I tweaked the AI and city rules to try and get some more interesting results

## What I Learned

 ### Neural Networks
 
At the start of this project, I didn’t fully appreciate that a neural network was not a very suitable solution for this problem, so its behaviour ended up being closer to a random number generator than an actual AI

### Importance of adding in new agents each generation

When I was making the genetic algorithm, it kept getting stuck at moderately good outcomes. To get past this, I increased the number of new agents added each generation so that if all the elite trials became stuck around one strategy, a new agent could potentially discover a better one

### Balancing Exploration and Optimization

I learned that genetic algorithms need a balance between improving the best existing solutions and exploring entirely new ones. If there isn’t enough variation between generations, the algorithm can converge too early and become trapped in local optima rather than discovering better long-term strategies.

## How it could be improved

 • I think if I could take away the 5 by 5 grid in some way so the AI only had to pick the building this would work a lot better for the nn as it would only have 1 choice

• Implementing a rules-based system could be interesting. I wonder if I could get a higher score with rules rather than a genetic algorithm

 • I reckon performance would improve if I cached repeated computations instead or recalculating them every time

 ## To run the project locally:

Clone the repository to your machine

Then run the command above
