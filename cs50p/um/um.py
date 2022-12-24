import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(list)


if __name__ == "__main__":
    main()