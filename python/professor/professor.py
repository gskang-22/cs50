import random


def main():
    while True:
        try:
            count = 0
            level = get_level()

            for i in range(10):
                try:
                    x = generate_integer(level)
                    y = generate_integer(level)
                    answer = input(f"{x} + {y} = ")

                    while True:
                        if answer == str(x + y):
                            count += 1
                            break
                        else:
                            print("EEE")

        except ValueError:
            continue



def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            continue


def generate_integer(level):
    if level == "1":
        return random.randint(1,9)
    elif level == "2":
        return random.randint(10, 99)
    elif level == "3":
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()