def read_input():
    lines = open("input.txt").read().split("\n\n")
    boxes = [line.replace('[', '').replace(']', '').replace("    ", " ").split(' ') for line in
             lines[0].split('\n')][::-1]
    boxes = transform_boxes(boxes)
    moves = lines[1].replace("move ", '').replace(" from ", ' ').replace(" to ", ' ').split('\n')
    moves = [[int(move_num) - 1 for move_num in move.split(' ')] for move in moves]
    return boxes, moves


def transform_boxes(boxes):
    print(boxes)
    max_size = int([num for num in boxes[0] if num][-1])
    new_boxes = max_size * ['']
    boxes = boxes[1:]
    for line in boxes:
        for count, box in enumerate(line):
            new_boxes[count] = new_boxes[count] + box
    return new_boxes


def move_from_to(from_loc: int, to_loc: int, box_count: int, boxes: list[str]):
    if boxes[from_loc]:
        boxes[to_loc] += boxes[from_loc][-box_count:]
        boxes[from_loc] = boxes[from_loc][:-box_count]
    return boxes


def get_code(boxes, moves):
    print(boxes)
    print(moves)
    for move in moves:
        move_count = move[0]
        boxes = move_from_to(move[1], move[2], move[0] + 1, boxes)
    return ''.join([stack[-1] for stack in boxes if stack])


def calc_final_value():
    boxes, moves = read_input()
    final_value = get_code(boxes, moves)
    print(final_value)
    print(final_value == "MCD")


calc_final_value()
