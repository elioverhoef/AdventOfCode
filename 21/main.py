from utils.get_input import download_input, open_input
import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "=": operator.eq}


def read_input():
    download_input()
    lines = [line.split(": ") for line in open_input()]
    dict = {}
    for line in lines:
        dict[line[0]] = line[1]
    return dict


def get_value(dict, monkey):
    val = dict[monkey]
    if len(val.split(' ')) == 1:
        return int(val)
    operation = val.split(' ')
    m1 = operation[0]
    oper = ops[operation[1]]
    m2 = operation[2]
    if operation[1] == '=':
        dict["humn"] = str(int(dict["humn"]) + 3453748215000)

        while int(get_value(dict, m1)) != int(get_value(dict, m2)):
            dict["humn"] = str(int(dict["humn"]) + 1)
            if int(get_value(dict, m1)) % 50 == 0:
                print(int(get_value(dict, m1)) - int(get_value(dict, m2)))
        return dict["humn"]
    return int(oper(int(get_value(dict, m1)), int(get_value(dict, m2))))


def calc_final_value():
    inputs = read_input()
    final_value = get_value(inputs, "root")
    print(final_value)


calc_final_value()
