from utils.get_input import download_input, open_input
import numpy as np


def read_input():
    download_input()
    return open_input()


def get_surrounding_trees(trees) -> int:
    visible_trees = 0
    first_time = True
    for row in trees:
        visible_trees += 2
        if first_time:
            first_time = False
            visible_trees += 2 * len(row) - 4
    return visible_trees


def get_inner_trees(trees) -> int:
    visible_trees = 0
    for count_row, row in enumerate(trees):
        for count_col, tree in enumerate(row):
            if 0 < count_row < len(trees) - 1 and 0 < count_col < len(row) - 1:
                visible_trees += check_higher(int(tree), count_row, count_col, trees)
    return visible_trees


def check_higher(tree: int, count_row: int, count_col: int, trees):
    if check_row(tree, count_row, count_col, trees):
        return 1
    elif check_col(tree, count_row, count_col, trees):
        return 1
    return 0


def check_row(tree_size: int, tree_row_index: int, tree_column_index: int, trees: list[str]) -> bool:
    tree_row = trees[tree_row_index]
    visible = True
    for count, other_tree in enumerate(tree_row):
        other_tree = int(other_tree)
        # Check left of tree
        if count < tree_column_index:
            if other_tree >= tree_size:
                visible = False
        if count == tree_column_index:
            if visible:
                return True
            visible = True
        # Check right of tree
        if count > tree_column_index:
            if other_tree >= tree_size:
                visible = False
    return visible


def check_col(tree_size: int, tree_row_index: int, tree_column_index: int, trees: list[str]) -> bool:
    trees = np.array(trees).T.tolist()
    tree_col = trees[tree_column_index]
    visible = True
    for count, other_tree in enumerate(tree_col):
        other_tree = int(other_tree)
        # Check left of tree
        if count < tree_row_index:
            if other_tree >= tree_size:
                visible = False
        if count == tree_row_index:
            if visible:
                return True
            visible = True
        # Check right of tree
        if count > tree_row_index:
            if other_tree >= tree_size:
                visible = False
    return visible


def get_visible_trees(trees):
    tree_count = 0
    tree_count += get_surrounding_trees(trees)
    tree_count += get_inner_trees(trees)
    return tree_count


# Part 2
def get_scenic_score(tree_size: int, row_ix: int, col_ix: int, trees: list[list[int]]) -> int:
    top = get_top(tree_size, row_ix, col_ix, trees) + 1
    left = get_left(tree_size, row_ix, col_ix, trees) + 1
    bottom = get_bottom(tree_size, row_ix, col_ix, trees) + 1
    right = get_right(tree_size, row_ix, col_ix, trees) + 1
    if row_ix == 3 and col_ix == 2:
        print(top, left, bottom, right)
    return top*left*bottom*right


def get_top(tree_size: int, row_ix: int, col_ix: int, trees: list[list[int]]) -> int:
    if row_ix == 0:
        return 0
    count = 0
    for count, i in enumerate(range(row_ix)[::-1]):
        other_height = trees[i][col_ix]
        if int(other_height) >= tree_size:
            return count
    return count


def get_left(tree_size: int, row_ix: int, col_ix: int, trees: list[list[int]]) -> int:
    if col_ix == 0:
        return 0
    count = 0
    for count, i in enumerate(range(col_ix)[::-1]):
        other_height = trees[row_ix][i]
        if int(other_height) >= tree_size:
            return count
    return count


def get_bottom(tree_size: int, row_ix: int, col_ix: int, trees: list[list[int]]) -> int:
    if row_ix == len(trees) - 1:
        return 0
    count = 0
    for count, i in enumerate(range(len(trees) - row_ix - 1)):
        other_height = trees[i + row_ix + 1][col_ix]
        if int(other_height) >= tree_size:
            return count
    return count


def get_right(tree_size: int, row_ix: int, col_ix: int, trees: list[list[int]]) -> int:
    if col_ix == len(trees[row_ix]) - 1:
        return 0
    count = 0
    for count, i in enumerate(range(len(trees) - 1 - col_ix)):
        other_height = trees[row_ix][i + col_ix + 1]
        if int(other_height) >= tree_size:
            return count
    return count


def get_scenic_scores(trees: list[list[list[int]]]):
    scenic_scores = []
    for row_ix, row in enumerate(trees):
        for col_ix, tree in enumerate(row):
            scenic_scores.append(get_scenic_score(int(tree), row_ix, col_ix, trees))
    return scenic_scores


def calc_final_value():
    inputs = read_input()
    # visible_trees = get_visible_trees(inputs)
    scenic_scores = get_scenic_scores(inputs)
    print(scenic_scores)
    print(max(scenic_scores))


calc_final_value()
