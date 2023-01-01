from utils.get_input import download_input, open_input
from math import ceil


def read_input():
    download_input()
    return open_input()


def current_board(tails_count):
    return [(0, 0) for _ in range(1 + tails_count)]


def move(board, inputs):
    inputs = [x.split(' ') for x in inputs]
    positions = {(0, 0)}
    for x in inputs:
        x[1] = int(x[1])
        if x[0] == 'R':
            board, positions = make_move(board, x[1], 1, 0, positions)
        elif x[0] == 'L':
            board, positions = make_move(board, x[1], -1, 0, positions)
        elif x[0] == 'U':
            board, positions = make_move(board, x[1], 0, 1, positions)
        elif x[0] == 'D':
            board, positions = make_move(board, x[1], 0, -1, positions)
    return positions


def make_move(board, steps, x, y, positions):
    for i in range(steps):
        h_x, h_y = board[0]
        board[0] = h_x + x, h_y + y
        for t in range(len(board) - 1):
            board[t + 1], positions = update_tail(board[t], board[t + 1], positions, t == len(board) - 2)
    return board, positions


def update_tail(head, tail, positions, last_one):
    h_x, h_y = head
    t_x, t_y = tail
    offset_x = h_x - t_x
    offset_y = h_y - t_y
    if 2 > offset_x > -2 and 2 > offset_y > -2:
        return tail, positions
    bool1 = offset_x > 1 or offset_x < -1
    bool2 = offset_y > 1 or offset_y < -1
    if bool1 and bool2:
        t_x += int(offset_x/2)
        t_y += int(offset_y/2)
    elif bool1:
        t_x += int(offset_x/2)
        t_y += offset_y
    elif bool2:
        t_x += offset_x
        t_y += int(offset_y/2)
    if last_one:
        positions.add((t_x, t_y))
    return (t_x, t_y), positions


def tail_positions(inputs):
    board = current_board(9)
    positions = move(board, inputs)
    return positions


def calc_final_value():
    import time
    t1_start = time.perf_counter()

    inputs = read_input()
    positions = tail_positions(inputs)
    print(sorted(positions))
    print(len(positions))
    t1_stop = time.perf_counter()

    print("Elapsed time during the whole program in seconds:",
          t1_stop - t1_start)


calc_final_value()
