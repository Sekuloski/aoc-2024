from heapq import heappop, heappush

from aocd import get_data
from aocd.post import submit


def dijkstra(grid):
    visited = set()
    priority_queue = [(0, 0, 0)]
    paths = []

    while priority_queue:
        distance, y, x = heappop(priority_queue)

        if y == x == len(grid) - 1:
            return distance

        if (y, x) in visited:
            continue

        visited.add((y, x))

        for new_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y = y + new_direction[1]
            new_x = x + new_direction[0]
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[new_y]) and grid[new_y][new_x] != '#':
                heappush(priority_queue, (distance + 1, new_y, new_x))
                # paths.append({(y, x): (new_y, new_x, 1)})

    # return paths


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=18,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    obstacles = [tuple(map(int, x.split(','))) for x in data[:1024]]
    positions = []
    for i in range(71):
        positions.append([])
        for y in range(71):
            if (y, i) in obstacles:
                positions[i].append('#')
            else:
                positions[i].append('.')

    answer = dijkstra(positions)

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)