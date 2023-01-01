from utils.get_input import download_input, open_input_raw
import operator
from dataclasses import dataclass

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}


def read_input():
    download_input()
    return open_input_raw()


@dataclass
class Monkey:
    items: list[int]
    operation: list[str]
    test: int
    monkey1: int
    monkey2: int


def throw_items(monkey: Monkey, monkeys: dict, inspect_count: list[int], key, div):
    """
    Args:
        monkey (list): List of: Monkey's worry values for each item, Operation, Test, Monkey1 [Test True], Monkey2
        monkeys (dict): All monkeys in a dictionary
        inspect_count (list): List of the number of times each monkey has inspected an item
        key (int): Which monkey is this?
        div (int): Greatest common denominator, modulo each worry value by this to keep values small
    """
    for item in monkey.items:
        val1 = item
        val2 = item
        if monkey.operation[2] != "old":
            val2 = int(monkey.operation[2])
        op = ops[monkey.operation[1]]
        new_item = op(val1, val2) % div
        if new_item % monkey.test == 0:
            to_monkey = monkey.monkey1
        else:
            to_monkey = monkey.monkey2

        monkeys[to_monkey].items.append(new_item)
        inspect_count[key] += 1
    monkey.items = []
    return inspect_count


def convert_input(inputs):
    monkeys = {}
    inputs = [inp.split('\n') for inp in inputs.split("Monkey ")]
    for monkey_list in inputs:
        if not monkey_list[0]:
            continue
        monkey = Monkey([int(item) for item in monkey_list[1].split("Starting items: ")[1].split(", ")],
                        monkey_list[2].split("Operation: new = ")[1].split(' '),
                        int(monkey_list[3].split("Test: divisible by ")[1]),
                        int(monkey_list[4].split("If true: throw to monkey ")[1]),
                        int(monkey_list[5].split("If false: throw to monkey ")[1]))
        monkeys[int(monkey_list[0].replace(":", ""))] = monkey
    return monkeys, len(monkeys) * [0]


def get_greatest_denominator(monkeys):
    from functools import reduce
    divs = [m.test for m in monkeys.values()]
    return reduce((lambda x, y: x * y), divs)


def calc_final_value():
    inputs = read_input()
    monkeys, inspect_count = convert_input(inputs)
    div = get_greatest_denominator(monkeys)
    for i in range(10000):
        for key, monkey in monkeys.items():
            inspect_count = throw_items(monkey, monkeys, inspect_count, key, div)
    sorted_inspect_counts = sorted(inspect_count)
    final_value = sorted_inspect_counts[-1] * sorted_inspect_counts[-2]
    print(final_value)


calc_final_value()
