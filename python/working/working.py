import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        group = re.search("^([0-9:]+) ([A-Z]+) to ([0-9:]+) ([A-Z]+)$", s.strip())
        time1, at1, time2, at2 = group.groups()
        if at1 == "AM":
            time1 =
            


...


if __name__ == "__main__":
    main()