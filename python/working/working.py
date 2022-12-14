import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        time = re.search("^(0-9:)+[a-zA-Z ]+(0-9:).*$")


...


if __name__ == "__main__":
    main()