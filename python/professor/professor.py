import random


def main():
    while True:
        try:
            count = 0
            level = get_level()

            for i in range(10):
                x = generate_integer(level)
                y = generate_integer(level)
                times = 0

                for i in range(3):
                    answer = input(f"{x} + {y} = ")

                    if answer == str(x + y):
                        count += 1
                        break
                    else:
                        print("EEE")
                        times += 1

                    if times == 3:
                        print(f"{x} + {y} = {x + y}")

            print(f"Score: {count}")
            break

        except ValueError:
            continue

        except EOFError:
            break





def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            continue


def generate_integer(level):
    if level == "1":
        return random.randint(0,9)
    elif level == "2":
        return random.randint(10, 99)
    elif level == "3":
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()