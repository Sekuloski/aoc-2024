from collections import defaultdict
from aocd import get_data
from aocd.post import submit


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=5,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    answer = 0

    rules = defaultdict(list)
    line = 0
    while True:
        if not data[line]:
            line += 1
            break
        rule = data[line].split('|')
        line += 1
        rules[rule[0]].append(rule[1])
    
    correct_updates = []
    incorrect_updates = []
    for update in data[line:]:
        update_correct = True
        processed_pages = []
        for number in update.split(','):
            for rule_number in rules[number]:
                if rule_number in processed_pages:
                    update_correct = False
                    break
            if not update_correct:
                break
            processed_pages.append(number)
        if not update_correct and update:
            incorrect_updates.append(update)

    while True:
        everything_correct = True
        new_updates = []

        for incorrect_update in list(set(incorrect_updates)):
            update_correct = True
            processed_pages = {}
            numbers = incorrect_update.split(',')
            for number_index in range(len(numbers)):
                number = numbers[number_index]
                processed_pages[number] = number_index
                for rule_number in rules[number]:
                    if rule_number in processed_pages:
                        numbers[number_index] = rule_number
                        numbers[processed_pages[rule_number]] = number
                        everything_correct = False
                        update_correct = False
                        new_updates.append(','.join(numbers))
                        print(new_updates)
                        
                        break
                if not update_correct:
                    break
            if update_correct and incorrect_update:
                correct_updates.append(incorrect_update)

        if everything_correct:
            break
        incorrect_updates = new_updates

    print(list(set(correct_updates)))
    for update in correct_updates:
        numbers = update.split(',')
        answer += int(numbers[len(numbers) // 2])

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(False)
