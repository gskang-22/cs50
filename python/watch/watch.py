import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'^.* src="(https?://(www\.)?youtube\.com/embed/.*)".*)
    print(url)


if __name__ == "__main__":
    main()