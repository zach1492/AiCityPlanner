import random

GRID_SIZE = 5

EMPTY = 0
ROAD = 1
HOUSE = 2
OFFICE = 3
FACTORY = 4
APARTMENT = 5
PARK = 6

TILES = {
    0: "E",  # Empty
    1: "R",  # Road
    2: "H",  # House
    3: "O",  # Office
    4: "F",  # Factory
    5: "A",  # Apartment
    6: "P"   # Park
}

def print_board_state(grid, state):
    print("State:", state)
    print()
    for x in range(GRID_SIZE):
        row = []
        for y in range(GRID_SIZE):
            row.append(TILES[grid[x][y]])
        print(" ".join(row))

def is_adjacent_to_road(grid, x, y):
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if grid[nx][ny] == ROAD:
                return True
    return False

def valid_build(grid, x, y, building, money):
    if grid[x][y] != EMPTY:
        return False

    costs = {ROAD:1, HOUSE:2, OFFICE:5, FACTORY:3, APARTMENT:5, PARK:2}
    if money < costs[building]:
        return False

    return is_adjacent_to_road(grid, x, y)

def apply_action(grid, state, action):
    x, y, building = action

    if not valid_build(grid, x, y, building, state["money"]):
        return

    costs = {ROAD:1, HOUSE:2, OFFICE:5, FACTORY:3, APARTMENT:5, PARK:2}
    state["money"] -= costs[building]
    grid[x][y] = building

def update_resources(grid, state, apartments_age):
    money_gain = 0
    current_pop = 0

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            tile = grid[x][y]

            if tile == HOUSE:
                current_pop += 1

            elif tile == OFFICE:
                money_gain += 3

            elif tile == FACTORY:
                money_gain += 3
                current_pop -= 1

            elif tile == APARTMENT:
                current_pop += 3               
                #if (x, y) not in apartments_age:
                    #apartments_age[(x, y)] = 0
                #apartments_age[(x, y)] += 1
                #current_pop += apartments_age[(x, y)]

            elif tile == PARK:
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        if grid[nx][ny] == HOUSE:
                            current_pop += 1

    state["money"] += money_gain
    state["population"] = current_pop
