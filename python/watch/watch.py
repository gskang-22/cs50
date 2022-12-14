import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'^.*src="(https?://(www\.)?youtube\.com/embed/[\w]+).*', s)
    shorten = re.sub("embed/", "", url.group(1))
    shorten = re.sub("youtube.com", "youtu.be", shorten)
    shorten = re.sub(")
    return shorten


if __name__ == "__main__":
    main()