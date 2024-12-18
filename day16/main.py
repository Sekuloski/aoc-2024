import itertools
from copy import copy
from heapq import heappush, heappop
from aocd import get_data
from aocd.post import submit


def dijkstra(grid, maximum: int = 0):
    visited = set()
    priority_queue = [(0, 1, 1, (1, 0))]
    paths = []

    while priority_queue:
        distance, y, x, prev_direction = heappop(priority_queue)
        if maximum != 0 and distance > maximum:
            continue

        if grid[y][x] == 'E':
            if maximum == 0:
                return distance
            else:
                if distance > maximum:
                    continue

        if (y, x, prev_direction) in visited:
            continue

        visited.add((y, x, prev_direction))

        new_y = y + prev_direction[1]
        new_x = x + prev_direction[0]
        if 0 <= new_y < len(grid) - 1 and 0 <= new_x < len(grid[new_y]) - 1 and grid[new_y][new_x] != '#':
            heappush(priority_queue, (distance + 1, new_y, new_x, prev_direction))
            if (new_y, new_x) != (1, 1):
                paths.append({(y, x): (new_y, new_x, 1)})

        for new_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y = y + new_direction[1]
            new_x = x + new_direction[0]
            if new_direction != prev_direction and new_direction != (-prev_direction[0], -prev_direction[1]):
                if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[new_y]) and grid[new_y][new_x] != '#':
                    heappush(priority_queue, (distance + 1 + 1000, new_y, new_x, new_direction))
                    paths.append({(y, x): (new_y, new_x, 1001)})

    return paths


def find_path(path, paths, maximum, y, x, distance, nodes: list, visited=[]):
    if (y, x, distance, path) in visited:
        return

    next_items = list(set([
        (
            list(path.keys())[0][0],
            list(path.keys())[0][1],
            list(path.values())[0][2]
        ) for path in paths if list(path.values())[0] == (y, x, 1) or list(path.values())[0] == (y, x, 1001)
    ]))
    for item in next_items:
        if (item[0], item[1]) in path or distance + item[2] > maximum:
            continue

        new_path = copy(path)
        new_path.append((item[0], item[1]))

        if new_path in visited:
            continue

        if distance + item[2] == maximum and item[0] == 1 and item[1] == 1:
            nodes.append(new_path)
            return True

        find_path(new_path, paths, maximum, item[0], item[1], distance + item[2], nodes, visited)

    visited.append((y, x, distance, path))

def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=16,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(reversed(list(filter(None, data))))
    print('Finding shortest path...')
    answer = dijkstra(data)
    print('Shortest distance:', answer)
    nodes = []
    if answer:
        print('Finding all paths...')
        paths = dijkstra(data, answer)
        print('Finding nodes...')
        find_path([(len(data) - 2, len(data[0]) - 2)], paths, answer, len(data) - 2, len(data[0]) - 2, 0, nodes)

    answer = len(set(list(itertools.chain(*nodes))))
    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(True)
