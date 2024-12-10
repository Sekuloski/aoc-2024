from aocd import get_data
from aocd.post import submit


def check_position(step, i, j, data):
    positions = []
    step = str(step)
    if i + 1 < len(data) and data[i+1][j] == step:
        positions.append((i+1, j))

    if i - 1 >= 0 and data[i-1][j] == step:
        positions.append((i-1, j))

    if j + 1 < len(data[i]) and data[i][j+1] == step:
        positions.append((i, j+1))

    if j - 1 >= 0 and data[i][j-1] == step:
        positions.append((i, j-1))

    return positions


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=10,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)
    answer = 0
    hikes = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '0':
                hikes[(i, j)] = {0: [(i, j)]}

    for trail in hikes:
        for i in range(1, 10):
            routes = hikes[trail][i - 1]
            hikes[trail][i] = []
            for route in routes:
                hikes[trail][i].extend(check_position(i, route[0], route[1], data))

    for trail, values in hikes.items():
        # Part 1
        # answer += len(set(values[9]))
        answer += len(values[9])

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(True)
