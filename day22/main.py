from collections import defaultdict

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
    final_sequence_map = defaultdict(int)
    for number in data:
        sequence_map = {}
        secret_number = number
        previous_one = secret_number % 10
        sequence = []

        for _ in range(2000):
            secret_number = ((secret_number * 64) ^ secret_number) % 16777216
            secret_number = ((secret_number // 32) ^ secret_number) % 16777216
            secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
            one = secret_number % 10
            sequence.append(one - previous_one)
            previous_one = one

            if len(sequence) == 5:
                sequence.pop(0)
                if str(sequence) not in sequence_map:
                    sequence_map[str(sequence)] = one

        for sequence, value in sequence_map.items():
            final_sequence_map[sequence] += value

    answer = max({v: k for k, v in sorted(final_sequence_map.items(), key=lambda item: item[1], reverse=True)})
    if not testing:
        submit(answer, day=22, year=2024)


if __name__ == '__main__':
    main(False)
