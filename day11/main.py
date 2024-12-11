from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=11,
            year=2024
        ).replace('\n', '').split(' ')
    else:
        data = open('test').read().replace('\n', '').split(' ')

    data = list(filter(None, data))

    for step in range(25):
        next_inserts = []
        for index in range(len(data)):
            stone = data[index]
            if stone == '0':
                data[index] = '1'

            elif len(stone) % 2 == 0:
                data[index] = str(int(stone[len(stone) // 2:]))
                next_inserts.append((index + len(next_inserts), str(int(stone[:len(stone) // 2]))))
            else:
                data[index] = str(int(stone) * 2024)
        for insert in next_inserts:
            data.insert(insert[0], insert[1])

    if testing:
        print(len(data))
    else:
        submit(len(data))


if __name__ == '__main__':
    main(False)
