from aocd import get_data
from aocd.post import submit


def main(testing: bool = False, part: int = 1):
    if not testing:
        data = get_data(
            day=1,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    left_list = []
    right_list = []
    answer = 0
    for line in data:
        numbers = line.split(' ')
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[-1]))

    if part == 1:
        while left_list and right_list:
            minimum_left = min(left_list)
            left_list.remove(minimum_left)
            minimum_right = min(right_list)
            right_list.remove(minimum_right)
       
            answer += abs(minimum_left - minimum_right)
    elif part == 2:
        for number in left_list:
            answer += number * right_list.count(number)

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False, 2)
