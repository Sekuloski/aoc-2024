from aocd import get_data
from aocd.post import submit
from multiprocessing import Pool

def update_direction(direction) -> tuple[int, int]:
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    else:
        return (-1, 0)
    

def check_obstacle(i, j, starting_point, obstacles, max_x, max_y):
    if (i, j) in obstacles or starting_point == (i, j):
        return 0
    positions_visited = []
    current_position = starting_point
    new_obstacles = obstacles.copy()
    new_obstacles.append((i, j))
    direction: tuple[int, int] = (-1, 0)
    while True:
        if current_position[0] < 0 or current_position[1] < 0 or current_position[0] > max_y or current_position[1] > max_x:
            return 0
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if next_position in new_obstacles:
            direction = update_direction(direction)
        else:
            current_position = next_position
        if (current_position, direction) in positions_visited:
            return 1
        else:
            if current_position != starting_point:
                positions_visited.append((current_position, direction))


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=6,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')
    
    data = list(filter(None, data))
    answer = 0
    max_x = len(data[0]) - 1
    max_y = len(data) - 1

    obstacles = []
    positions_visited = []
    starting_point = (0, 0)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                obstacles.append((i, j))
            elif data[i][j] == '^':
                starting_point = (i, j)
    
    args = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            args.append((i, j, starting_point, obstacles, max_x, max_y))
    with Pool(5) as p:
        answer = sum(p.starmap(check_obstacle, args))
    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
