import random

GRID_SIZE = 5

EMPTY = 0
ROAD = 1
HOUSE = 2
OFFICE = 3
FACTORY = 4
APARTMENT = 5
PARK = 6

grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

grid[2][2] = ROAD#add in road in the middle

apartments_age = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

state = {
    "money": 10,
    "population": 0,
    "generation": 0
}



def print_board_state():
    print("State:", state)
    print()

    for x in range(GRID_SIZE):
        row = []
        for y in range(GRID_SIZE):
            row.append(TILES[grid[x][y]])
        print(" ".join(row))

TILES = {
    0: "E",  # Empty
    1: "R",  # Road
    2: "H",  # House
    3: "F",  # Factory
    4: "P",  # Park
    5: "O",  # Office
    6: "A"   # Apartment
}
def is_adjacent_to_road(grid, x, y):
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if grid[nx][ny] == ROAD:
                return True
    return False

def valid_build(grid, x, y, building, money):
    if grid[x][y] != EMPTY:
        return False

    costs = {ROAD:1, HOUSE:2, OFFICE:5, FACTORY:3, APARTMENT:5, PARK:2}
    if money < costs[building]:
        return False

    if building == ROAD:
        return is_adjacent_to_road(grid, x, y)

    return is_adjacent_to_road(grid, x, y)

def apply_action(grid, state, action):
    x, y, building = action

    if not valid_build(grid, x, y, building, state["money"]):
        return 

    costs = {ROAD:1, HOUSE:2, OFFICE:5, FACTORY:3, APARTMENT:5, PARK:2}
    state["money"] -= costs[building]
    grid[x][y] = building

def update_resources(grid, state, apartments_age):
    money_gain = 5
    current_Pop = 0

    for x in range(5):
        for y in range(5):
            tile = grid[x][y]

            if tile == HOUSE:
                money_gain += 1
                current_Pop += 1

            elif tile == OFFICE:
                money_gain += 3

            elif tile == FACTORY:
                money_gain += 3
                current_Pop -= 1

            elif tile == APARTMENT:
                apartments_age[(x,y)] += 1
                current_Pop += apartments_age[(x,y)]

            elif tile == PARK:
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if grid[nx][ny] == HOUSE:
                            current_Pop += 1

    state["money"] += money_gain
    state["population"] = current_Pop
    
def random_action():
    return (
        random.randint(0,4),
        random.randint(0,4),
        random.randint(1,6)
    )

for turn in range(200):
    action = random_action()
    apply_action(grid, state, action)
    update_resources(grid, state, apartments_age)
    print_board_state()
