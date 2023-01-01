from utils.get_input import download_input, open_input_raw
import ast
from itertools import zip_longest


def read_input():
    download_input()
    return [i.split('\n') for i in open_input_raw().split('\n\n')]


def right_order(list1, list2) -> int:
    if isinstance(compare_lists(list1, list2), bool):
        if compare_lists(list1, list2):
            return 1
        elif not compare_lists(list1, list2):
            return -1
    else:
        return 0


def compare_lists(list1, list2):
    for item1, item2 in zip_longest(list1, list2):
        # print(item1, item2)
        if isinstance(item1, int) and isinstance(item2, int):
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        elif isinstance(item1, (int, list)) and item2 is None:
            return False
        elif item1 is None and isinstance(item2, (int, list)):
            return True
        elif isinstance(item1, list) and isinstance(item2, list):
            if isinstance(compare_lists(item1, item2), bool):
                return compare_lists(item1, item2)
        elif isinstance(item1, list) and isinstance(item2, int):
            if isinstance(compare_lists(item1, [item2]), bool):
                return compare_lists(item1, [item2])
        elif isinstance(item1, int) and isinstance(item2, list):
            if isinstance(compare_lists([item1], item2), bool):
                return compare_lists([item1], item2)
    return None


def calc_final_value():
    inputs = read_input()
    final_value = 0
    for index, block in enumerate(inputs):
        if right_order(ast.literal_eval(block[0]), ast.literal_eval(block[1])) == 1:
            final_value += index + 1
    new_inputs = []
    for block in inputs:
        list1 = ast.literal_eval(block[0])
        list2 = ast.literal_eval(block[1])
        new_inputs.append(list1)
        new_inputs.append(list2)
    new_inputs.append([[2]])
    new_inputs.append([[6]])
    from functools import cmp_to_key
    outputs = sorted(new_inputs, key=cmp_to_key(right_order), reverse=True)
    final_value_2 = 1
    for c, o in enumerate(outputs):
        if o == [[2]]:
            final_value_2 *= (c + 1)
        if o == [[6]]:
            final_value_2 *= (c + 1)
    print("Part 1: " + str(final_value))
    print("Part 2: " + str(final_value_2))


calc_final_value()
