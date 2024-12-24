from copy import copy
from heapq import heappop, heappush

from aocd import get_data
from aocd.post import submit


def dijkstra(grid, start):
    visited = set()
    priority_queue = [(0, start[0], start[1])]
    paths = {}

    while priority_queue:
        distance, y, x = heappop(priority_queue)

        if grid[y][x] == 'E':
            return distance

        visited.add((y, x))

        for new_direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_y = y + new_direction[1]
            new_x = x + new_direction[0]
            if (new_y, new_x) not in visited:
                if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[new_y]) and grid[new_y][new_x] != '#':
                    heappush(priority_queue, (distance + 1, new_y, new_x))
                    paths[(new_y, new_x)] = (y, x)


def check_obstacle(grid, y, x):
    if 0 <= y - 1 and y + 1 < len(grid):
        if grid[y - 1][x] == '.' and grid[y + 1][x] == '.':
            return True
    if 0 <= x - 1 and x + 1 < len(grid[0]):
        if grid[y][x - 1] == '.' and grid[y][x + 1] == '.':
            return True


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=20,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data.pop()
    data.pop(0)
    for i in range(len(data)):
        data[i] = data[i][1:-1]
    data = list(reversed(list(filter(None, data))))

    S = None
    obstacles = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                S = (i, j)
            elif data[i][j] == '#' and check_obstacle(data, i, j):
                obstacles.append((i, j))

    maximum = dijkstra(data, S)
    answer = 0
    count = 0
    for obstacle in obstacles:
        count += 1
        new_data = copy(data)
        new_data[obstacle[0]] = new_data[obstacle[0]][:obstacle[1]] + '.' + new_data[obstacle[0]][obstacle[1] + 1:]
        result = dijkstra(new_data, S)
        if maximum - result >= 100:
            answer += 1

    print(answer)
    if not testing:
        submit(answer)


if __name__ == '__main__':
    main(False)
