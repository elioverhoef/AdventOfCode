from utils.get_input import download_input, open_input


def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    download_input()
    pairs = []
    for line in open_input():
        sx, sy, bx, by = [
            int(x.split('=')[1].rstrip(',:'))
            for x in line.split()
            if '=' in x
        ]
        pairs.append(((sx, sy), (bx, by)))
    return pairs


def get_impossible_locations(pairs: list[tuple[tuple[int, int], tuple[int, int]]], y: int) -> \
        list[tuple[int, int]]:
    ranges = []
    for (sx, sy), (bx, by) in pairs:
        distance_to_beacon = abs(sx - bx) + abs(sy - by)
        sensor_distance_to_y = abs(sy - y)
        if sensor_distance_to_y > distance_to_beacon:
            continue
        num_of_hash_left_and_right = distance_to_beacon - sensor_distance_to_y
        ranges.append((sx - num_of_hash_left_and_right,
                       sx + num_of_hash_left_and_right))
    return merge_ranges(ranges)


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()
    merged = [(max(ranges[0][0], 0), min(ranges[0][1], 4000000))]
    for new_left, new_right in ranges[1:]:
        new_left = max(new_left, 0)
        new_right = min(new_right, 4000000)
        previous_left, previous_right = merged[-1]
        if new_right <= previous_right:  # New range part of previous range
            pass
        elif new_left == previous_left:  # New range includes previous range
            merged[-1] = (new_left, new_right)
        elif new_left < previous_right + 2:  # New range is now merged with previous range, 1+ elements overlapped
            merged[-1] = (previous_left, new_right)
        else:  # ranges do not overlap
            merged.append((new_left, new_right))
    return merged


def count_impossible_row(pairs: list[tuple[tuple[int, int], tuple[int, int]]], y: int) -> int:
    impossible_ranges = get_impossible_locations(pairs, y)
    impossible_count = 0
    beacons_on_line_y = {bx for _, (bx, by) in pairs if by == y}
    # Filtering the beacons from the impossible locations
    for left, right in impossible_ranges:
        beacons_in_impossible_range = len([b for b in beacons_on_line_y if left <= b <= right])
        impossible_count += right - left - beacons_in_impossible_range + 1  # Add one since right location is included
    return impossible_count


def find_distress_location(pairs: list[tuple[tuple[int, int], tuple[int, int]]], minimum: int, maximum: int):
    for y in range(0, 4000001)[::-1]:
        impossible_ranges = get_impossible_locations(pairs, y)
        for left, right in impossible_ranges:
            if right == minimum and left == maximum:
                break
            if right < maximum:
                return maximum * (right + 1) + y
            if left > minimum:
                return maximum * (left - 1) + y
            break


def calc_final_value():
    pairs = read_input()
    # print("Part 1:", count_impossible_row(pairs, 2000000))
    print("Part 2:", find_distress_location(pairs, 0, 4_000_000))


calc_final_value()
