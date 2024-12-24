from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=1,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)
    answer = 0

    print(answer)
    if not testing:
        submit(answer)


if __name__ == '__main__':
    main(True)
