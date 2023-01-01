from utils.get_input import download_input, open_input


def read_input():
    download_input()
    valve_list = [line.replace("Valve ", "").replace("has flow rate=", "").replace(" tunnels lead to valves", "")
                  .replace(",", "").replace(" tunnel leads to valve", "").replace(";", "").split(" ")
                  for line in open_input()]
    for v in valve_list:
        v[1] = int(v[1])
    valves = {item[0]: {"flow": item[1], "tunnels": item[2:], "paths": {}} for item in valve_list}
    return valves


def bfs(search_space, goal, valves):
    current_depth = 1
    while True:
        new_space = set()
        for x in search_space:
            if x == goal:
                return current_depth
            for y in valves[x]['tunnels']:
                new_space.add(y)
        search_space = new_space
        current_depth += 1


def create_paths(valves, keys):
    for k in keys + ['AA']:
        for k2 in keys:
            if k2 == k:
                continue
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2, valves)
    return valves


def get_pressure(opened, total_pressure, current_room, minutes_to_go, valves):
    global best
    if total_pressure > best:  # Update best when released pressure is at a new high in current_room
        best = total_pressure

    if minutes_to_go <= 0:  # Stop when minutes_to_go becomes 0 or less
        return

    if current_room not in opened:  # Open valve in current room, increasing pressure by min_to_go * flow
        get_pressure(opened.union([current_room]), total_pressure + valves[current_room]['flow'] * minutes_to_go,
                     current_room, minutes_to_go - 1, valves)
    else:  # Valve has been opened in this room, move to all other rooms and try from there
        for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
            get_pressure(opened, total_pressure, k, minutes_to_go - valves[current_room]['paths'][k], valves)


def part_2(opened, total_pressure, current_room, minutes_to_go, elephants_turn, valves):
    global best
    if total_pressure > best:
        best = total_pressure

    if minutes_to_go <= 0:
        return

    # Hacky speed boost
    if minutes_to_go < 15 and total_pressure < 1100 or minutes_to_go < 20 and total_pressure < 700:
        return

    if current_room not in opened:
        open_room(opened, total_pressure, current_room, minutes_to_go, elephants_turn, valves)
    else:  # Valve has been opened in this room, move to all other rooms and try from there
        other_rooms = valves[current_room]['paths']
        for room in [room for room in other_rooms if room not in opened]:
            part_2(opened, total_pressure, room, minutes_to_go - other_rooms[room], elephants_turn, valves)
            # Subtract distance to room from minutes, as each movement takes one minute.


def open_room(opened, total_pressure, current_room, minutes_to_go, elephants_turn, valves):
    # Do a move: open the valve in the current room, increasing the total pressure
    part_2(opened.union([current_room]), total_pressure + valves[current_room]['flow'] * minutes_to_go,
           current_room, minutes_to_go - 1, elephants_turn, valves)
    # Initiate the elephant's move from the initial room
    if not elephants_turn:
        part_2(opened.union([current_room]), total_pressure + valves[current_room]['flow'] * minutes_to_go, 'AA',
               25, True, valves)


best = 0


def calc_final_value():
    global best
    valves = read_input()
    keys = [x for x in list(valves.keys()) if valves[x]['flow'] > 0]
    valves = create_paths(valves, keys)  # Add paths from each valve to all other valves with a flow greater than 0

    get_pressure({'AA'}, 0, 'AA', 29, valves)
    print("Part 1: " + str(best))

    best = 0
    part_2({'AA'}, 0, 'AA', 25, False, valves)
    print("Part 2: " + str(best))


calc_final_value()
