from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if testing:
        data = get_data(
            day=1,
            year=2023
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    print(data)
    answer = 0

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(True)