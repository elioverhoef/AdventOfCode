from utils.get_input import download_input, open_input


def read_input():
    download_input()
    return open_input()


def calc_stuff(val):
    return val


def calc_final_value():
    inputs = read_input()
    final_value = None
    for val in inputs:
        print(val)
        final_value = calc_stuff(val)
    print(final_value)


calc_final_value()
