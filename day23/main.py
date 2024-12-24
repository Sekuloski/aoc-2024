from collections import defaultdict
from copy import copy

from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=23,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    connections: list[list[str]] = []
    computers = []

    for line in data:
        connections.append(sorted(line.split('-')))
        computers.extend(line.split('-'))

    computers = list(set(computers))
    original_connections = copy(connections)

    print(computers, connections)
    connection_found = True
    while True:
        if not connection_found:
            break

        connection_found = False
        for connection in connections:
            for new_computer in computers:
                if new_computer in connection:
                    continue

                add_computer = True
                for current_computer in connection:
                    if sorted([new_computer, current_computer]) not in original_connections:
                        add_computer = False
                        break

                if add_computer:
                    connection.append(new_computer)
                    connection_found = True

    connections.sort(key=len, reverse=True)
    answer = ','.join(sorted(connections[0]))
    print(answer)
    if not testing:
        submit(answer, day=23, year=2024)


if __name__ == '__main__':
    main(False)
