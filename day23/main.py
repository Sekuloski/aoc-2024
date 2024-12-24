from collections import defaultdict

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
    connections: dict[str, list[str]] = defaultdict(list)
    for line in data:
        comps = line.split('-')

        connections[comps[0]].append(comps[1])
        if comps[0] not in connections[comps[0]]:
            connections[comps[0]].append(comps[0])

        connections[comps[1]].append(comps[0])
        if comps[1] not in connections[comps[1]]:
            connections[comps[1]].append(comps[1])

    three_conns: set[tuple[str, ...]] = set()
    for item, connection in connections.items():
        for comp in connection:
            comp_connections: list[str] = connections[comp]
            items = set(list(set(connection).intersection(comp_connections)))
            for c in items:
                final = tuple(set(sorted((item, comp, c))))
                if len(final) == 3:
                    three_conns.add(final)

    print(connections)
    print(three_conns)
    answer = [x for x in three_conns if any([y for y in x if str(y).startswith('t')])]

    print(len(answer), answer)
    if not testing:
        submit(len(answer), day=23, year=2024)


if __name__ == '__main__':
    main(False)
