# TODO

import cs50


def find_change(change, value, count):
    count += change // value
    change = change % value
    return (change, count)


while True:
    change = cs50.get_float('Change owed: ') * 100
    if change > 0:
        break
count = 0
(change, count) = find_change(change, 25, count)
(change, count) = find_change(change, 10, count)
(change, count) = find_change(change, 5, count)
(change, count) = find_change(change, 1, count)
count = int(count)
print(f'{count}')