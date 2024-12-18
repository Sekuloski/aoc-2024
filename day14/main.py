import math
from collections import defaultdict
from itertools import groupby
from operator import itemgetter

from aocd import get_data
from aocd.post import submit


MAX_X = 101
MAX_Y = 103


class Robot:
    def __init__(self, start_x, start_y, x_v, x_y):
        self.x = start_x
        self.y = start_y
        self.x_v = x_v
        self.y_v = x_y

    def move(self):
        self.x += self.x_v
        self.y += self.y_v

        if self.x >= MAX_X - 1:
            self.x = self.x % MAX_X

        elif self.x < 0:
            self.x = MAX_X + self.x

        if self.y >= MAX_Y - 1:
            self.y = self.y % MAX_Y

        elif self.y < 0:
            self.y = MAX_Y + self.y

    def quadrant(self) -> int | None:
        w_mid = MAX_X // 2
        h_mid = MAX_Y // 2

        if self.x < w_mid and self.y < h_mid:
            return 0
        elif self.x > w_mid and self.y < h_mid:
            return 1
        elif self.x < w_mid and self.y > h_mid:
            return 2
        elif self.x > w_mid and self.y > h_mid:
            return 3

        return None


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=14,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)

    robots = []
    for entry in data:
        p, v = entry.split(' ')
        start_x, start_y = p.split('=')[1].split(',')
        x_v, y_v = v.split('=')[1].split(',')
        robots.append(Robot(int(start_x), int(start_y), int(x_v), int(y_v)))

    neighbors_counter = []
    max_neighbors = 0
    for _ in range(10000):
        current_positions = []
        for robot in robots:
            robot.move()
            current_positions.append((robot.x, robot.y))
        neighbors = 0
        for x, y in current_positions:
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (x2, y2) in current_positions:
                    neighbors += 1

        neighbors_counter.append(neighbors)
        if neighbors > max_neighbors:
            max_neighbors = neighbors
            for x in range(100):
                for y in range(101):
                    if (x, y) in current_positions:
                        print("*", end="")
                    else:
                        print(".", end="")
                print("")

    quadrants = [0, 0, 0, 0]

    for robot in robots:
        quadrant = robot.quadrant()
        if quadrant is not None:
            quadrants[quadrant] += 1

    answer = math.prod(quadrants)
    answer = neighbors_counter.index(max(neighbors_counter)) + 1
    if testing:
        print(answer)
    else:
        print(answer)
        submit(answer)


if __name__ == '__main__':
    main(False)
