import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall("\b(um)", s, re.IGNORECASE)
    print(list)


if __name__ == "__main__":
    main()