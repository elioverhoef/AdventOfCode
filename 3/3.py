def read_input():
    txt = open("input.txt").read().split("\n")
    return txt


def calc_stuff(val: list):
    overlap = set(val[0]).intersection(set(val[1]))
    overlap = overlap.intersection(set(val[2]))
    c: chr = overlap.pop()
    print(c)
    if c.islower():
        final = ord(c) - 96
        print(final)
        return final
    else:
        final = ord(c) - 38
        print(final)
        return final


def calc_final_value():
    inputs = read_input()
    three_inputs = []
    final_value = 0
    counter = 0
    ls = []
    for val in inputs:
        if counter < 3:
            ls.append(val)
            counter += 1
        else:
            three_inputs.append(ls)
            ls = [val]
            counter = 1
    for val in three_inputs:
        print(val)
        final_value += calc_stuff(val)
    print(final_value)


calc_final_value()

# small letters have priority over LARGE letters, following alphabet
# for each rucksack, take priority of overlapping letters
