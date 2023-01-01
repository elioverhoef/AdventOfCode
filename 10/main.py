from utils.get_input import download_input, open_input


def read_input():
    download_input()
    return open_input()


def calc_stuff(x, line, cycle, temp, count) -> tuple[int, int, int]:
    cmd = line.split(' ')
    if cmd[0] == "noop":
        return x, cycle + 1, 0
    if cmd[0] == "addx":
        return x, cycle + 1, int(cmd[1])


def draw_me(x: int, cycle: int, drawing) -> str:
    pixel = cycle - 1  # Pixel starts at 0, first cycle will be 1
    if pixel % 40 == 0:
        drawing += '\n'
    if x - 1 <= pixel % 40 <= x + 1:
        drawing += '#'
        return drawing
    drawing += '.'
    return drawing


def calc_final_value():
    inputs = read_input()
    x = 1
    cycle = 0
    temp = 0
    total = 0
    drawing = ""

    for count, line in enumerate(inputs):
        x, cycle, temp = calc_stuff(x, line, cycle, temp, count)
        drawing = draw_me(x, cycle, drawing)
        if cycle == 20 or (cycle - 20) % 40 == 0:
            total += (x * cycle)
        if temp:
            cycle += 1
            drawing = draw_me(x, cycle, drawing)
            if cycle == 20 or (cycle - 20) % 40 == 0:
                total += (x * cycle)
            x += temp
            temp = 0
        # if free:
        #     print(x, cycle, count + 1, temp)

    # print(total)
    print(drawing)


calc_final_value()
