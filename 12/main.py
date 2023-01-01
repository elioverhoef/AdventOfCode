from utils.get_input import download_input, open_input


def graph_dict(width, height):
    graph = dict()
    for x in range(width):
        for y in range(height):
            temp_list = []
            temp_list = conditional_append(temp_list, x - 1, y, width, height)
            temp_list = conditional_append(temp_list, x + 1, y, width, height)
            temp_list = conditional_append(temp_list, x, y - 1, width, height)
            temp_list = conditional_append(temp_list, x, y + 1, width, height)
            graph[(x, y)] = temp_list
    return graph


def conditional_append(temp_list, neigh_x, neigh_y, width, height):
    if 0 <= neigh_x < width and 0 <= neigh_y < height:
        temp_list.append((neigh_x, neigh_y))
    return temp_list


def read_input():
    download_input()
    return open_input()


def move(elevations, graph):
    # Find location S and E
    start = end = (-1, -1)
    for c_line, line in enumerate(elevations):
        for c_node, node in enumerate(line):
            if node == 'S':
                start = (c_node, c_line)
            elif node == 'E':
                end = (c_node, c_line)
    print(start, end)
    # Find the shortest path between S and E
    return shortest_path(graph, start, end, elevations)


def move_part_2(elevations, graph):
    # Find location S and E
    end = (-1, -1)
    start_nodes = []
    for c_line, line in enumerate(elevations):
        for c_node, node in enumerate(line):
            if node == 'E':
                end = (c_node, c_line)
            elif node == 'a' or node == 'S':
                start_nodes.append((c_node, c_line))
    shortest_paths = []
    for start in start_nodes:
        print(start, end)
        # Find the shortest path between S and E
        shortest_paths.append(shortest_path(graph, start, end, elevations))
    return shortest_paths


def get_num(node, elevations):
    x, y = node
    c = elevations[y][x]
    if c == 'S':
        return ord('a')
    if c == 'E':
        return ord('z')
    return ord(c)


def shortest_path(graph, start, end, elevations):
    path_list = [[start]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start}
    if start == end:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end in next_nodes and get_num(end, elevations) - get_num(last_node, elevations) < 2:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node not in previous_nodes and get_num(next_node, elevations) - get_num(last_node, elevations) < 2:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def calc_final_value():
    elevations = [[*line] for line in read_input()]
    graph = graph_dict(len(elevations[0]), len(elevations))
    # path = move(elevations, graph)
    paths = move_part_2(elevations, graph)
    path = min([len(path) for path in paths if len(path) > 0])
    print(path - 1)


calc_final_value()
