# TODO
from cs50 import get_int

while True:
    x = get_int("Height: ")
    if x > 0 and x < 9:
        break

for i in range(0, x):
    for j in range(1, x - i):
        print(' ', end='')
    for k in range(0, i + 1):
        print('#', end='')
    print('')
