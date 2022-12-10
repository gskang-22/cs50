import random


def main():
    try:



def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            continue


def generate_integer(level):
    if level == "1":
        return random.randint(1,10)


if __name__ == "__main__":
    main()