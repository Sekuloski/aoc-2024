from collections import defaultdict

from aocd import get_data
from aocd.post import submit


def get_count(stone, n, i, entries):
    if stone in entries[i]:
        return entries[i][stone]

    if i >= n:
        return 1

    if stone == '0':
        count = get_count('1', n, i + 1, entries)
        entries[i][stone] = count

    elif len(stone) % 2 == 0:
        count = get_count(str(int(stone[len(stone) // 2:])), n, i + 1, entries)
        count += get_count(str(int(stone[:len(stone) // 2])), n, i + 1, entries)
        entries[i][stone] = count

    else:
        count = get_count(str(int(stone) * 2024), n, i + 1, entries)
        entries[i][stone] = count

    return count


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=11,
            year=2024
        ).replace('\n', '').split(' ')
    else:
        data = open('test').read().replace('\n', '').split(' ')

    data = list(filter(None, data))

    steps = 26
    entries = defaultdict(dict)
    for index in range(len(data)):
        stone = data[index]
        get_count(stone, steps, 1, entries)

    if testing:
        print(sum(entries[1].values()))
    else:
        submit(sum(entries[1].values()))


if __name__ == '__main__':
    main(False)
