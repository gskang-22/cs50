import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall("\bum\b", s, re.IGNORECASE)


...


if __name__ == "__main__":
    main()