from utils.get_input import load_input

directories = {"": {"files": [], "dirs": []}}
current_dir = ""


def handle_input(cmd):
    global current_dir
    cmd = cmd.split(' ')
    if cmd[0] != '$':
        if current_dir not in directories.keys():
            directories[current_dir] = {"files": [], "dirs": []}
        if cmd[0] == "dir":
            directories[current_dir]["dirs"].append(cmd[1])
        else:
            directories[current_dir]["files"].append((cmd[1], int(cmd[0])))
        return
    if cmd[1] != "cd":
        return
    match cmd[2]:
        case '/':
            current_dir = ""
        case "..":
            current_dir = current_dir.rstrip(current_dir.split('/')[-1]).rstrip("/")
        case _:
            current_dir += f"/{cmd[2]}"


def dir_size(f: str) -> int:
    final_size = sum([size for (_, size) in directories[f]["files"]])
    return final_size + sum([dir_size(f"{f}/{_dir}") for _dir in directories[f]["dirs"]])


def dir_sizes():
    return [dir_size(f) for f in directories.keys()]


def big_folders():
    return [size for size in dir_sizes() if size >= dir_size("") - 40000000]


load_input()
for val in open("input.txt").read().split("\n"):
    handle_input(val)
print(sum([s for s in dir_sizes() if s <= 100000]))  # 1
print(min(big_folders()))  # 2
