from aocd import get_data
from aocd.post import submit
from sympy import symbols, Eq, solve


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=13,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    print(data)
    answer = 0

    a, b = symbols('x y')
    data = list(reversed(data))
    while True:
        try:
            button_a = data.pop()
            button_b = data.pop()
            prize = data.pop()

            button_a_x = int(button_a.split(' ')[2].split('+')[1][:-1])
            button_a_y = int(button_a.split(' ')[3].split('+')[1])
            button_b_x = int(button_b.split(' ')[2].split('+')[1][:-1])
            button_b_y = int(button_b.split(' ')[3].split('+')[1])
            prize_x = int(prize.split(' ')[1].split('=')[1][:-1]) + 10000000000000
            prize_y = int(prize.split(' ')[2].split('=')[1]) + 10000000000000
            eq1 = Eq(a * button_a_x + b * button_b_x, prize_x)
            eq2 = Eq(a * button_a_y + b * button_b_y, prize_y)
            solution = solve((eq1, eq2), (a, b))
            if '/' not in str(solution[a]) and '/' not in str(solution[b]):
                answer += solution[a] * 3 + solution[b]
        except Exception:
            break

    if testing:
        print(answer)
    else:
        print(answer)
        # submit(answer)


if __name__ == '__main__':
    main(False)
