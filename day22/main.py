from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=22,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(map(int, filter(None, data)))
    print(data)
    answer = 0
    for number in data:
        secret_number = number
        for _ in range(2000):
            secret_number = ((secret_number * 64) ^ secret_number) % 16777216
            secret_number = ((secret_number // 32) ^ secret_number) % 16777216
            secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
        answer += secret_number

    print(answer)
    if not testing:
        submit(answer, day=22, year=2024)


if __name__ == '__main__':
    main(False)
