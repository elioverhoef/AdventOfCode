from utils.get_input import download_input, open_input
import numpy as np
import scipy.ndimage as ni


def read_input():
    download_input()
    return open_input()


def calc_stuff(cubes):
    surface_count = 0
    dimensions = cubes.max(axis=0)
    spaces = np.zeros(dimensions + 1)
    transposed_cubes = cubes.T
    xs, ys, zs = transposed_cubes
    spaces[xs, ys, zs] = 1

    # Fill "holes" in 3D space with True (rocks), such that only outer surface of these rocks is seen as surface_area
    spaces = ni.binary_fill_holes(spaces)

    # Get indices of true values in spaces
    cubes = set(zip(*np.where(spaces)))
    for x, y, z in cubes:
        for i, j, k in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            neighbor = (x + i, y + j, z + k)
            if neighbor not in cubes:
                surface_count += 1
                # Old approach
                # if enclosed(neighbor, cubes):
                #     surface_count -= 1
    return surface_count


def calc_final_value():
    cubes = np.array([[int(x) for x in i.split(',')] for i in read_input()])
    surface_area = calc_stuff(cubes)
    print(surface_area)


calc_final_value()
