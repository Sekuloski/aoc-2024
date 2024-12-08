from collections import defaultdict
from aocd import get_data
from aocd.post import submit
import itertools


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=8,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)
    answer = 0
    items = defaultdict(list)
    max_x = len(data[0])
    max_y = len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            items[data[i][j]].append((i, j))

    del items['.']
    antennas = []
    for item, locations in items.items():
        combinations = list(itertools.combinations(locations, 2))
        for combo in combinations:
            location_1 = combo[0]
            location_2 = combo[1]
            diff_x = abs(location_2[1] - location_1[1])
            diff_y = abs(location_2[0] - location_1[0])
            n = 0
            while True:
                if location_1[0] < location_2[0]:
                    if location_1[1] < location_2[1]:
                        antenna_1 = (location_1[0] - diff_y * n, location_1[1] - diff_x * n)
                        antenna_2 = (location_2[0] + diff_y * n, location_2[1] + diff_x * n)
                    else:
                        antenna_1 = (location_1[0] - diff_y * n, location_1[1] + diff_x * n)
                        antenna_2 = (location_2[0] + diff_y * n, location_2[1] - diff_x * n)
                else:
                    if location_1[1] < location_2[1]:
                        antenna_1 = (location_1[0] + diff_y * n, location_1[1] - diff_x * n)
                        antenna_2 = (location_2[0] - diff_y * n, location_2[1] + diff_x * n)
                    else:
                        antenna_1 = (location_1[0] + diff_y * n, location_1[1] + diff_x * n)
                        antenna_2 = (location_2[0] - diff_y * n, location_2[1] - diff_x * n)

                n += 1
                flag = 0
                if 0 <= antenna_1[0] < max_y and 0 <= antenna_1[1] < max_x:
                    antennas.append(antenna_1)
                else:
                    flag += 1
                if 0 <= antenna_2[0] < max_y and 0 <= antenna_2[1] < max_x:
                    antennas.append(antenna_2)
                else:
                    flag += 1

                if flag == 2:
                    break

    if testing:
        print(len(list(set(antennas))))
        print(antennas)
    else:
        submit(len(list(set(antennas))))
    

if __name__ == '__main__':
    main(False)
