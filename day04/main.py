from aocd import get_data
from aocd.post import submit


def check_xmas(data, i, j):
    total = 0
    print(data[i][j], i, j)
    # Left
    try:
        if data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
            if j-3 >= 0:
                total += 1
                print('Found Left')
    except Exception:
        pass

    # Right
    try:
        if data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
            total += 1
            print('Found Right')

    except Exception:
        pass
    # Up
    try:
        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
            if i-3 >= 0:
                total += 1
                print('Found Up')

    except Exception:
        pass
    # Down
    try:
        if data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
            total += 1
            print('Found Down')

    except Exception:
        pass

    # Left Up
    try:
        if data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
            if i-3 >= 0 and j-3 >= 0:
                total += 1

    except Exception:
        pass
    # Rigth Up
    try:
        if data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
            if i-3 >= 0:
                total += 1
                print('Found Right Up')

    except Exception:
        pass
    # Right Down
    try:
        if data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
            total += 1
            print('Found Right Down')

    except Exception:
        pass
    # Left Down
    try:
        if data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
            if j-3 >= 0:
                total += 1
            print('Found Left Down')

    except Exception:
        pass
    return total


def check_x_mas(data, i, j):
    if i == 0 or j == 0 or i == len(data) - 1 or j == len(data[0]) - 1:
        return 0
    
    total = 0
    if (data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S') or data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M':
        total += 1

    if (data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S') or data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M':
        total += 1
    
    if (data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S') or data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M':
        total += 1
    
    if (data[i+1][j+1] == 'M' and data[i-1][j-1] == 'S') or data[i+1][j+1] == 'S' and data[i-1][j-1] == 'M':
        total += 1

    if total == 4:
        return 1
    return 0


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=4,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    answer = 0
    if not data[-1]:
        data.pop()
    for i in range(len(data)):
        print(data[i])
        for j in range(len(data[i])):
            if data[i][j] == 'A':
                answer += check_x_mas(data, i, j)
        print(f'Found {answer} xmases')

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
