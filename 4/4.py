def read_input():
    txt = open("input.txt").read().split("\n")
    return txt


def calc_overlap(first, second):
    first1 = int(first.split('-')[0])
    first2 = int(first.split('-')[1])
    second1 = int(second.split('-')[0])
    second2 = int(second.split('-')[1])
    range1 = set(range(first1, first2 + 1))
    range2 = set(range(second1, second2 + 1))
    intersect = range1.intersection(range2)
    if intersect:
        return 1
    else:
        return 0


def calc_final_value():
    inputs = read_input()
    firsts = [inp.split(',')[0] for inp in inputs]
    seconds = [inp.split(',')[1] for inp in inputs]
    final_value = 0
    for first, second in zip(firsts, seconds):
        print(first)
        print(second)
        final_value += calc_overlap(first, second)
    print(final_value)


calc_final_value()
