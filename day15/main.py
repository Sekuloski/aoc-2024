from typing import Any

from aocd import get_data
from aocd.post import submit
from sympy import prime_valuation


def print_state(walls, obstacles, robot, data):
    for i in range(len(data)):
        line_to_print = ''
        for y in range(len(data[i])):
            if (i, y) in walls:
                line_to_print += '#'
            elif (i, y) in obstacles:
                line_to_print += 'O'
            elif (i, y) == robot:
                line_to_print += '@'
            else:
                line_to_print += '.'
        print(line_to_print)

class Obstacle:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def move(self, obstacles: dict[tuple[int, int], Any], walls: list[tuple[int, int]], x, y):
        new_position = self.y + y, self.x + x
        print(new_position)
        if new_position in obstacles:
            result = obstacles[new_position].move(obstacles, walls, x, y)
            if result:
                obstacles[new_position] = self
                del obstacles[(self.y, self.x)]
                self.x += x
                self.y += y

            return result

        elif new_position in walls:
            return False

        else:
            obstacles[new_position] = self
            del obstacles[(self.y, self.x)]
            self.x += x
            self.y += y
            return True


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=15,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)
    answer = 0

    index = 0
    moves = []
    walls = []
    obstacles = {}
    robot = (0, 0)
    for i in range(len(data)):
        line = data[i]
        if '#' in line:
            for y in range(len(line)):
                c = line[y]
                if c == '#':
                    walls.append((i, y))
                if c == 'O':
                    obstacles[(i, y)] = Obstacle(y, i)
                if c == '@':
                    robot = (i, y)
        else:
            moves.extend(list(line))

    print_state(walls, obstacles, robot, data)
    for move in moves:
        print(f'Moving {move}')
        x = 0
        y = 0
        match move:
            case '>':
                x = 1
            case '<':
                x = -1
            case '^':
                y = -1
            case _:
                y = 1
        new_position = robot[0] + y, robot[1] + x
        print(new_position)
        if new_position in obstacles:
            if obstacles[new_position].move(obstacles, walls, x, y):
                robot = new_position
        elif new_position not in walls:
            robot = new_position
        # print_state(walls, obstacles, robot, data)

    answer = sum([obstacle[0] * 100 + obstacle[1] for obstacle in obstacles.keys()])
    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
