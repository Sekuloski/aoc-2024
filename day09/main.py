from sys import exc_info
from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    data = open('test').read().strip()
    data = list(map(int, list(filter(None, list(data)))))
    answer = 0
 
    block = True
    block_id = 0
    drive = []
    for i in range(len(data)):
        if block:
            drive.append(f'{block_id} * {data[i]}')
            block_id += 1
        else:
            drive.append(f'. * {data[i]}')
        block = not block
    
    working_id = int(drive[-1].split(' ')[0])
    working_position = len(drive) - 1
    while working_id > 0:
        while True:
            try:
                if working_id == int(drive[working_position].split(' ')[0]):
                    break
            except Exception:
                pass

            working_position -= 1
    
        working_count = int(drive[working_position].split(' ')[-1])
        counter = 0
        while True:
            if counter >= working_position:
                break

            if '.' in drive[counter]:
                free_space = int(drive[counter].split(' ')[-1])
                if free_space >= working_count:
                    free_space -= working_count
                    drive[counter] = f'. * {free_space}'
                    drive[working_position] = f'. * {working_count}'
                    drive.insert(counter, f'{working_id} * {working_count}')
                    break
            counter += 1

        working_id -= 1

    final_drive = []
    for entry in drive:
        entry_id = entry.split(' ')[0]
        count = entry.split(' ')[-1]
        for _ in range(int(count)):
            final_drive.append(entry_id)
    print(''.join(final_drive))

    for i in range(len(final_drive)):
        try:
            answer += i * int(final_drive[i])
        except Exception:
            pass

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
