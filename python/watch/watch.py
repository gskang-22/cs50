import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    rul = re.search(r'^.* src="https?://(www\.)?youtube\.com/(?:embed/).*")


...


if __name__ == "__main__":
    main()