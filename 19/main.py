from utils.get_input import download_input, open_input
import re


def read_input():
    download_input()
    return open_input()


max_geodes = 0


def bfs(search_space):
    current_depth = 0
    best_geodes = 0
    while True:
        new_space = set()
        for node in search_space:
            blueprint, ores, robots = node
            ore, clay, obsidian, geode = ores
            if current_depth == 32:
                best_geodes = max(best_geodes, geode)
            elif current_depth == 33:
                return best_geodes
            for y in generate_options(blueprint, ores, robots):
                new_space.add(y)
        search_space = new_space
        current_depth += 1


def generate_options(blueprint, ores, robots):
    options = set()
    number, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = blueprint
    ore, clay, obsidian, geode = ores
    ore_robots, clay_robots, obsidian_robots, geode_robots = robots

    new_ore = ore + ore_robots
    new_clay = clay + clay_robots
    new_obsidian = obsidian + obsidian_robots
    new_geode = geode + geode_robots

    if ore >= geode_ore and obsidian >= geode_obsidian:
        options.add((
            blueprint,
            (new_ore - geode_ore, new_clay, new_obsidian - geode_obsidian, new_geode),
            (ore_robots, clay_robots, obsidian_robots, geode_robots + 1)
        ))
    else:
        if ore >= ore_ore and ore_robots < max(clay_ore, obsidian_ore, geode_ore):
            options.add((
                blueprint,
                (new_ore - ore_ore, new_clay, new_obsidian, new_geode),
                (ore_robots + 1, clay_robots, obsidian_robots, geode_robots)
            ))
        if ore >= clay_ore and clay_robots < obsidian_clay:
            options.add((
                blueprint,
                (new_ore - clay_ore, new_clay, new_obsidian, new_geode),
                (ore_robots, clay_robots + 1, obsidian_robots, geode_robots)
            ))
        if ore >= obsidian_ore and clay >= obsidian_clay and obsidian_robots < geode_obsidian:
            options.add((
                blueprint,
                (new_ore - obsidian_ore, new_clay - obsidian_clay, new_obsidian, new_geode),
                (ore_robots, clay_robots, obsidian_robots + 1, geode_robots)
            ))

        # Default - do nothing
        elif ore <= max(ore_ore, clay_ore, obsidian_ore, geode_ore) and (clay <= obsidian_clay or
                                                                         obsidian <= geode_obsidian):
            options.add((
                blueprint,
                (new_ore, new_clay, new_obsidian, new_geode),
                (ore_robots, clay_robots, obsidian_robots, geode_robots)
            ))
    return options


def calc_quality(blueprint, ores, robots):
    # options = generate_options(blueprint, ores, robots)
    number, _, _, _, _, _, _ = blueprint
    final_geodes = bfs({(blueprint, ores, robots)})
    return final_geodes


def get_blueprints(inputs):
    res = []
    for i in inputs:
        x = re.findall(r"\d+", i)
        res.append(tuple([int(d) for d in x]))
    return res


def calc_final_value():
    inputs = read_input()
    blueprints = get_blueprints(inputs)
    final_value = 1
    for blueprint in blueprints:
        ore = 0
        clay = 0
        obsidian = 0
        geode = 0

        ore_robots = 1
        clay_robots = 0
        obsidian_robots = 0
        geode_robots = 0
        final_value *= calc_quality(blueprint, (ore, clay, obsidian, geode),
                                    (ore_robots, clay_robots, obsidian_robots, geode_robots))
        print(final_value)


calc_final_value()
