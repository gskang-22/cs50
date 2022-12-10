import random

while True:
    level = input("Level: ")
    if not level.isdigit():
        continue
    if int(level) <= 0:
        continue
    break

while True:
    x = random.randint(1, int(level))

    guess = input("Guess: ")
    if not guess.isdigit():
        continue
    if int(guess) <= 0:
        continue


    if int(guess) < x:
        print("Too small!")
    elif int(guess) > x:
        print("Too large!")
    elif int(guess) == x:
        print("Just right!")
        break