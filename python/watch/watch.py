import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    rul = re.search(r'^.* src=")


...


if __name__ == "__main__":
    main()