from aocd import get_data
from aocd.post import submit
from itertools import product
from collections import deque

def generate_operator_combinations(operators, num_numbers):
    num_operator_slots = num_numbers - 1
    operator_combinations = list(product(operators, repeat=num_operator_slots))
    results = ["".join(comb) for comb in operator_combinations]

    return results


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=7,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))

    answer = 0
    for line in data:
        line_data = line.split(':')
        expected = int(line_data[0])
        numbers = list(map(int, line_data[1].removeprefix(' ').removesuffix(' ').split(' ')))
        operators = ['*', '+', '|']

        combinations = generate_operator_combinations(operators, len(numbers))
        for combo in combinations:
            q = deque()
            for number in numbers: 
                q.append(number)
            result = 0
            for operator in combo:
                if operator == '|':
                    result = int(f'{q.popleft()}{q.popleft()}')

                else:
                    result = eval(f'{q.popleft()}{operator}{q.popleft()}')
                q.appendleft(result)
            
            if result == expected:
                answer += expected
                break

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
