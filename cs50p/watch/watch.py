import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        url = re.search(r'^.*src="https?://(?:www\.)?youtube\.com/embed/([\w]+).*', s)
        return "https://youtu.be/" + url.group(1)
    except:
        return None


if __name__ == "__main__":
    main()