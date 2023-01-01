from utils.get_input import download_input, open_input


def read_input():
    download_input()
    return [[char for char in line] for line in open_input()]


class Shape:
    location = False

    def __init__(self, shape):
        if shape > 4:
            shape = 0
        self.last_shape = shape
        match shape:
            case 0:
                self.height = 1
                self.width = 4
                self.grid = [(0, 0), (1, 0), (2, 0), (3, 0)]
            case 1:
                self.height = 3
                self.width = 3
                self.grid = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
            case 2:
                self.height = 3
                self.width = 3
                self.grid = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
            case 3:
                self.height = 4
                self.width = 1
                self.grid = [(0, 0), (0, 1), (0, 2), (0, 3)]
            case 4:
                self.height = 2
                self.width = 2
                self.grid = [(0, 0), (1, 0), (0, 1), (1, 1)]


def move_one_step(push: chr, grid, shape, counter, grid_size):
    # Get start location of shape based on grid and height
    if not shape.location:
        shape.location = 2, len(grid) + 3
    # Update location based on push [only if possible]
    if push == '<':
        shape.location = push_left(grid, shape)
    elif push == '>':
        shape.location = push_right(grid, shape)
    # Check if shape has not yet reached other character or bottom
    stopped = check_stopped(grid, shape)
    if not stopped:
        # Move down one step
        shape.location = shape.location[0], shape.location[1] - 1
    # Get next shape when old shape stopped, add old shape to grid
    else:
        counter += 1
        (x_loc, y_loc) = shape.location
        for x, y in shape.grid:
            if not y + y_loc in grid.keys():
                grid[y + y_loc] = [(x + x_loc)]
                grid_size += 1
            else:
                grid[y + y_loc].append(x + x_loc)
        shape = Shape(shape.last_shape + 1)
    return grid, shape, counter, grid_size


def check_stopped(grid, shape) -> bool:
    (x_loc, y_loc) = shape.location
    if y_loc <= 0:
        return True
    for (x, y) in shape.grid:
        if y + y_loc - 1 not in grid.keys():
            continue
        if x + x_loc not in grid[y + y_loc - 1]:
            continue
        return True
    return False


def push_left(grid, shape):
    (x_loc, y_loc) = shape.location
    if x_loc - 1 < 0:
        return shape.location
    for (x, y) in shape.grid:
        if y + y_loc not in grid.keys():
            continue
        if x - 1 + x_loc not in grid[y + y_loc]:
            continue
        return shape.location
    return x_loc - 1, y_loc


def push_right(grid, shape):
    (x_loc, y_loc) = shape.location
    if x_loc + shape.width > 6:
        return shape.location
    for (x, y) in shape.grid:
        if y + y_loc not in grid.keys():
            continue
        if x + 1 + x_loc not in grid[y + y_loc]:
            continue
        return shape.location
    return x_loc + 1, y_loc


def calc_final_value():
    inputs = read_input()[0]
    i = 0
    grid = {}  # Of the form {0: [row], 1: [row]}   where row = [char, char] (dots are not shown)
    shape = Shape(0)
    counter = 0
    grid_size = 0
    repeating_grid_size = 0
    repeating_counter = 0
    first_loop = False
    second_loop = False
    simple_loop = False
    while i < len(inputs):
        if not second_loop:
            grid, shape, counter, grid_size = move_one_step(inputs[i], grid, shape, counter, grid_size)

            if counter == 2022 and not shape.location:  # Part 1
                print("Part 1: " + str(grid_size))

            # Part 2
            if counter == 1000000000000:  # Part 1
                print("Part 2: " + str(grid_size))
                break
            i += 1
            if i == len(inputs) and first_loop and not simple_loop:
                i = 0
                repeating_grid_size = grid_size - repeating_grid_size
                repeating_counter = counter - repeating_counter
                second_loop = True
            elif i == len(inputs):
                i = 0
                first_loop = True
                repeating_grid_size = grid_size
                repeating_counter = counter
        else:
            if counter < 1000000000000:
                times = (1000000000000 - counter) // repeating_counter
                counter += repeating_counter * times
                grid_size += repeating_grid_size * times
            first_loop = False
            second_loop = False
            simple_loop = True


calc_final_value()
