import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'^.*src="(https?://(www\.)?youtube\.com/embed/[\w]+).*', s)
    


if __name__ == "__main__":
    main()