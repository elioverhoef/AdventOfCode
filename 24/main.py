walls = set()
init_blizzards = set()
for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line):
        if c == '#':
            walls.add((x - 1, y - 1))
        if c == '>':
            init_blizzards.add((x - 1, y - 1, +1, 0))
        if c == '<':
            init_blizzards.add((x - 1, y - 1, -1, 0))
        if c == '^':
            init_blizzards.add((x - 1, y - 1, 0, -1))
        if c == 'v':
            init_blizzards.add((x - 1, y - 1, 0, +1))
X = max(x for x, y in walls)
Y = max(y for x, y in walls)
print(f"maze size: {X}x{Y}, {len(walls)} walls, {len(init_blizzards)} blizzards")
walls |= {(x, -2) for x in range(-1, 3)}
walls |= {(x, Y + 1) for x in range(X - 3, X + 2)}
start = (0, -1)
stop = (X - 1, Y)

steps = 0
player_locations = {start}
goals = [stop, start, stop]
while goals:
    steps += 1
    blizzards = {((px + steps * dx) % X, (py + steps * dy) % Y) for px, py, dx, dy in init_blizzards}
    all_player_locations = {(px + dx, py + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)] for px, py in player_locations}
    player_locations = all_player_locations - blizzards - walls
    if goals[0] in player_locations:
        print(steps)
        player_locations = {goals.pop(0)}
