from utils.get_input import download_input, open_input
from dataclasses import dataclass
import re

cube_size = 0


@dataclass
class Player:
    location = (0, 0)
    facing = 0  # 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

    def __init__(self, location, facing):
        self.location = location
        self.facing = facing


def read_input():
    download_input()
    lines = open_input()
    grid_lines = lines[:-1]
    todos = lines[-1]
    return [{c: x for c, x in enumerate(line) if x != ' '} for line in grid_lines], todos


def move(grid, todos, player):
    for todo in todos:
        match todo:
            case 'R':
                player.facing = (player.facing + 1) % 4
                continue
            case 'L':
                player.facing = (player.facing - 1) % 4
                continue
            case '':
                continue
        steps = int(todo)
        for i in range(steps):
            x, y = player.location
            match player.facing:
                case 0:
                    player.location = move_right(grid, x, y)
                case 1:
                    player.location = move_down(grid, x, y)
                case 2:
                    player.location = move_left(grid, x, y)
                case 3:
                    player.location = move_up(grid, x, y)
    return player


def move_right(grid, x, y):
    if x + 1 in grid[y].keys():
        if grid[y][x + 1] == '.':
            return x + 1, y
        return x, y
    n_x, n_y = get_neighbor(x, y, 0)
    if grid[n_y][n_x] == '.':
        return n_x, n_y
    return x, y


def move_down(grid, x, y):
    if y + 1 < len(grid):
        if x in grid[y + 1].keys():
            if grid[y + 1][x] == '.':
                return x, y + 1
            return x, y
    n_x, n_y = get_neighbor(x, y, 1)
    if grid[n_y][n_x] == '.':
        return n_x, n_y
    return x, y


def move_left(grid, x, y):
    if x - 1 in grid[y].keys():
        if grid[y][x - 1] == '.':
            return x - 1, y
        return x, y
    n_x, n_y = get_neighbor(x, y, 2)
    if grid[n_y][n_x] == '.':
        return n_x, n_y
    return x, y


def move_up(grid, x, y):
    if y - 1 >= 0:
        if x in grid[y - 1].keys():
            if grid[y - 1][x] == '.':
                return x, y - 1
            return x, y
    n_x, n_y = get_neighbor(x, y, 3)
    if grid[n_y][n_x] == '.':
        return n_x, n_y
    return x, y


def get_neighbor(x: int, y: int, facing: int):
    """
    Args:
        x (int): X coordinate player wants to go to
        y (int): Y coordinate player wants to go to
        facing (int): right, down, left, up | 0, 1, 2, 3

    Returns:
        tuple[int, int]: x, y | New location of player on the appropriate side of the cube
                              | Returns input x, y when the new square is blocked
    """
    global cube_size
    if y == 199 and facing == 1:
        return x + 100, 0
    if y >= 150:
        # Map right side to y = 149
        if x == 49 and facing == 0:
            return y - 100, 149
        # Left side to upper line of top-left side
        if x == 0 and facing == 2:
            return y - 50, 0
    if y == 149 and facing == 1:
        return 49, x + 100
    if y == 100 and facing == 3 and x <= 49:
        return 50, x + 50
    if y >= 100:
        if x == 99 and facing == 0:
            return 149, 149 - y
        if x == 0 and facing == 2:
            return 50, 149 - y
    if y >= 50:
        if x == 50 and facing == 2:
            return y - 50, 100
        if x == 99 and facing == 0:
            return y + 50, 49
    if y == 49 and facing == 1:
        return 99, x - 50
    if y == 0 and facing == 3:
        if x < 100:
            return 0, x + 100
        if x >= 100:
            return x - 100, 199
    if y <= 49:
        if x == 50 and facing == 2:
            return 0, 149 - y
        if x == 149 and facing == 0:
            return 99, 149 - y
    print(x, y, facing)
    return x, y


def calc_final_value():
    grid, todos = read_input()
    global cube_size
    cube_size = min([len(line) for line in grid])
    todos = re.split(r"(\d+)", todos)
    location = [x for x in grid[0].keys()][0]
    player = Player((location, 0), 0)

    player = move(grid, todos, player)
    x, y = player.location
    print(1000 * (y + 1) + 4 * (x + 1) + player.facing)


calc_final_value()
