from aocd import get_data
from aocd.post import submit
import re


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=3,
            year=2024
        )
    else:
        data = open('test').read()

    answer = 0
    enabled = True
    for match in re.findall(r"(mul\([0-9]+,[0-9]+\))|(don't\(\))|(do\(\))", data):
        match: str
        mul, dont, do = match
        if not mul and not dont and not do:
            continue
        if dont:
            enabled = False
        elif do:
            enabled = True
        elif mul and enabled:
            numbers = mul.split('(')[-1][:-1].split(',')
            answer += int(numbers[0]) * int(numbers[1])

    if testing:
        print(answer)
    else:
        print(answer)
        submit(answer)


if __name__ == '__main__':
    main(False)
