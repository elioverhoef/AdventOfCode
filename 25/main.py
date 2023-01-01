from utils.get_input import download_input, open_input

snafu = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2
}
decimal = {
    0: '0',
    1: '1',
    2: '2',
    3: '=',
    4: '-',
    5: '0'
}


def read_input():
    download_input()
    return open_input()


def to_snafu(dec_value):
    snafu_list = []
    next_dig = 0
    while dec_value > 0:
        val = dec_value % 5 + next_dig
        snafu_list.append(decimal[val])
        dec_value = dec_value // 5
        next_dig = 0
        if val > 2:
            next_dig = 1
    return ''.join(snafu_list[::-1])


def calc_final_value():
    inputs = read_input()
    dec_value = 0
    for row in inputs:
        for c, char in enumerate(row[::-1]):
            dec_value += snafu[char] * 5 ** c
    print("Decimal:", dec_value)
    print("Snafu:", to_snafu(dec_value))


calc_final_value()
