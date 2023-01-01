def calc_values(inputs, count):
    new = []
    for i, n in enumerate(inputs):
        new.append((n, i))
    for _ in range(count):
        for i, n in enumerate(inputs):
            switch((n, i), new)
    return list(map(lambda x: x[0], new))


def switch(x, outputs):
    i = outputs.index(x)
    val, _ = outputs.pop(i)
    new = (i + val) % len(outputs)
    if new == 0:
        outputs.append(x)
        return
    outputs.insert(new, x)


def calc_final_value():
    with open('input.txt') as f:
        inputs = list(map(str.strip, f.readlines()))
    # Part 1
    inputs = list(map(int, inputs))
    switched = calc_values(inputs, 1)
    final_value1 = sum(switched[(i + switched.index(0)) % len(switched)] for i in (1000, 2000, 3000))
    print("Part 1: " + str(final_value1))

    # Part 2
    inputs = list(map(lambda x: x * 811589153, inputs))
    switched = calc_values(inputs, 10)
    final_value2 = sum(switched[(i + switched.index(0)) % len(switched)] for i in (1000, 2000, 3000))
    print("Part 2: " + str(final_value2))

calc_final_value()
