from aocd import get_data
from aocd.post import submit


def check_level(numbers, i, increasing):
    if int(numbers[i]) > int(numbers[i + 1]) and increasing:
        return 1
    if int(numbers[i]) < int(numbers[i + 1]) and not increasing:
        return 1
    if int(numbers[i]) == int(numbers[i + 1]):
        return 1
    if abs(int(numbers[i]) - int(numbers[i + 1])) > 3:
        return 1
    return 0

def test_line(line):
    numbers = line.split(' ')
    problems = 0
    increasing = int(numbers[0]) - int(numbers[1]) < 0
    for i in range(len(numbers) - 1):
        problems += check_level(numbers, i, increasing)

    if problems > 0:
        problems = 0
        new_numbers = numbers[:-1]
        increasing = int(new_numbers[0]) - int(new_numbers[1]) < 0
        for j in range(len(new_numbers) - 1):
            problems += check_level(new_numbers, j, increasing)
        if problems > 0:
            for i in range(len(numbers) - 1):
                problems = 0
                new_numbers = numbers[:i] + numbers[i + 1:]
                increasing = int(new_numbers[0]) - int(new_numbers[1]) < 0
                for j in range(len(new_numbers) - 1):
                    problems += check_level(new_numbers, j, increasing)
                if problems == 0:
                    return 0
        else:
            return 0
    else:
        return 0

    return problems

def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=2,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    print(data)
    answer = 0
    for line in data:
        problems = test_line(line)
        if problems == 0:
            answer += 1


    if testing:
        print(answer)
    else:
        print(answer)
        # submit(answer)


if __name__ == '__main__':
    main(False)