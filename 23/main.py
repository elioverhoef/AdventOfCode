from utils.get_input import download_input, open_input


def read_input():
    download_input()
    return {c_r: [c for c, i in enumerate(x) if i == "#"] for c_r, x in enumerate(open_input())}


def calc_stuff(grid, order):
    going_to = {}
    # First half of the round
    for row_count, chars in grid.items():
        for char in chars:
            if check_round(char, row_count, grid):
                continue
            going_to = propose(char, row_count, going_to, order, grid)

    for location, from_locs in going_to.items():
        if len(from_locs) > 1:
            continue
        grid = move_to(location, from_locs[0], grid)
    return grid


def move_to(location, from_loc, grid):
    y, x = from_loc
    new_y, new_x = location
    grid[y].remove(x)
    if new_y in grid.keys():
        grid[new_y].append(new_x)
    else:
        grid[new_y] = [new_x]
    return grid


def check_round(char, row, inputs):
    if row - 1 in inputs.keys():
        if char - 1 in inputs[row - 1] or char in inputs[row - 1] or char + 1 in inputs[row - 1]:
            return False
    if char - 1 in inputs[row] or char + 1 in inputs[row]:
        return False
    if row + 1 in inputs.keys():
        if char - 1 in inputs[row + 1] or char in inputs[row + 1] or char + 1 in inputs[row + 1]:
            return False
    return True


def propose(char, row, going_to, order, inputs):
    for s in order:
        match s:
            case 'n':
                if row - 1 in inputs.keys():
                    if char - 1 not in inputs[row - 1] and char not in inputs[row - 1] and char + 1 not in inputs[
                        row - 1]:
                        if (row - 1, char) in going_to.keys():
                            going_to[(row - 1, char)].append((row, char))
                        else:
                            going_to[(row - 1, char)] = [(row, char)]
                        return going_to
                else:
                    if (row - 1, char) in going_to.keys():
                        going_to[(row - 1, char)].append((row, char))
                    else:
                        going_to[(row - 1, char)] = [(row, char)]
                    return going_to

            case 's':
                if row + 1 in inputs.keys():
                    if char - 1 not in inputs[row + 1] and char not in inputs[row + 1] and char + 1 not in inputs[
                        row + 1]:
                        if (row + 1, char) in going_to.keys():
                            going_to[(row + 1, char)].append((row, char))
                        else:
                            going_to[(row + 1, char)] = [(row, char)]
                        return going_to
                else:
                    if (row + 1, char) in going_to.keys():
                        going_to[(row + 1, char)].append((row, char))
                    else:
                        going_to[(row + 1, char)] = [(row, char)]
                    return going_to

            case 'w':
                if char - 1 not in inputs[row]:
                    if row - 1 in inputs.keys():
                        if char - 1 in inputs[row - 1]:
                            continue
                    if row + 1 in inputs.keys():
                        if char - 1 in inputs[row + 1]:
                            continue
                    if (row, char - 1) in going_to.keys():
                        going_to[(row, char - 1)].append((row, char))
                    else:
                        going_to[(row, char - 1)] = [(row, char)]
                    return going_to
            case 'e':
                if char + 1 not in inputs[row]:
                    if row - 1 in inputs.keys():
                        if char + 1 in inputs[row - 1]:
                            continue
                    if row + 1 in inputs.keys():
                        if char + 1 in inputs[row + 1]:
                            continue
                    if (row, char + 1) in going_to.keys():
                        going_to[(row, char + 1)].append((row, char))
                    else:
                        going_to[(row, char + 1)] = [(row, char)]
                    return going_to
    return going_to


def calc_final_value():
    grid = read_input()
    order = ['n', 's', 'w', 'e']
    # part_1(grid, order)
    part_2(grid, order)


def part_2(grid, order):
    i = 0
    temp_grid = 0
    while str(grid.items()) != temp_grid:
        temp_grid = str(grid.items())
        grid = calc_stuff(grid, order)
        order.append(order.pop(0))
        i += 1
    print(i)


def part_1(grid, order):
    for _ in range(10):
        grid = calc_stuff(grid, order)
        order.append(order.pop(0))
    y_min = x_min = 9999999999999
    y_max = x_max = 0
    for r_count, row in grid.items():
        if row:
            if r_count < y_min:
                y_min = r_count
            if r_count > y_max:
                y_max = r_count
            for x in row:
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
    count = sum([len(x) for x in list(grid.values())])
    print((y_max - y_min + 1) * (x_max - x_min + 1) - count)


calc_final_value()
