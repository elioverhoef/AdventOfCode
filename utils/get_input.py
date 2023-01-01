import requests
import os


def get_text(day: str):
    url = f"https://adventofcode.com/2022/day/{day}/input"
    r = requests.get(url, headers={'Cookie': 'session=53616c7465645f5f9875628ccf4e3b96a371f3a23cfb6d86a9504662a9955b'
                                             'fba58778ad40a9a8c31d610fc53ae7648f41c50e0f5ed68632ae4ef0161dde0167'})
    return r.content


def download_input():
    day = os.getcwd().split('\\')[-1]
    if not os.path.exists("input.txt"):
        with open("input.txt", "wb") as f:
            print("Created input.txt :D")
            f.write(get_text(day))
    elif os.path.getsize("input.txt") == 0:
        print("input.txt was empty, now filled :D")
        with open("input.txt", "wb") as f:
            f.write(get_text(day))


def open_input():
    lines = [line for line in open("input.txt").read().split("\n") if line]
    return lines


def open_input_raw():
    lines = open("input.txt").read()
    return lines
