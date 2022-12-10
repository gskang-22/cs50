import random

while True:
    level = input("Level: ")
    if not level .isdigit():
        continue
    if int(level) <= 0:
        continue

x = random.random(1, int(level))