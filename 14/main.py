from utils.get_input import download_input, open_input


def read_input():
    download_input()
    return open_input()


def do_steps(grid, lowest_y, step):
    sand_x = 500
    sand_y = 0

    sand_moves = True
    while sand_moves:
        if sand_y + 1 > lowest_y and step == 1:
            return grid, False
        elif safe_key(grid, 500, 0, step, lowest_y) != '.' and step == 2:  # For step 2, stop if clogged
            return grid, False
        if safe_key(grid, sand_x, sand_y + 1, step, lowest_y) == '.':
            sand_x, sand_y = sand_x, sand_y + 1
        elif safe_key(grid, sand_x - 1, sand_y + 1, step, lowest_y) == '.':
            sand_x, sand_y = sand_x - 1, sand_y + 1
        elif safe_key(grid, sand_x + 1, sand_y + 1, step, lowest_y) == '.':
            sand_x, sand_y = sand_x + 1, sand_y + 1
        else:
            grid[(sand_x, sand_y)] = 'o'
            sand_moves = False
    return grid, True


def safe_key(grid, x, y, step, lowest_y):
    if (x, y) in grid.keys():
        return grid[(x, y)]
    elif step == 2 and y == lowest_y + 2:
        return '#'
    return '.'


def create_grid(inputs):
    grid = {}
    for row in inputs:
        row = row.split(" -> ")
        row = [c.split(',') for c in row]
        for index in range(len(row) - 1):
            grid = set_grid(row[index], row[index + 1], grid)
    return grid


def set_grid(point1, point2, grid):
    x_diff = int(point1[0]) - int(point2[0])
    y_diff = int(point1[1]) - int(point2[1])
    grid[(int(point1[0]), int(point1[1]))] = '#'
    for x in range(abs(x_diff)):
        grid[(x + min(int(point1[0]), int(point2[0])), int(point1[1]))] = '#'
    for y in range(abs(y_diff)):
        grid[(int(point1[0]), y + min(int(point1[1]), int(point2[1])))] = '#'
    grid[(int(point2[0]), int(point2[1]))] = '#'
    return grid


def calc_final_value(step):
    inputs = read_input()
    grid = create_grid(inputs)
    lowest_y = 0
    for (x, y) in grid.keys():
        if y > lowest_y:
            lowest_y = y
    final_grid = None
    busy = True
    while busy:
        final_grid, busy = do_steps(grid, lowest_y, step)
    from collections import Counter
    print(f"Step {step}: {Counter(list(final_grid.values()))}")


calc_final_value(1)
calc_final_value(2)
