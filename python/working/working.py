import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        group = re.search("^([0-9:]+) ([A-Z]+) to ([0-9:]+) ([A-Z]+)$", s.strip())
        time1, at1, time2, at2 = group.groups()
        time1 = check(time1, at1)
        time2 = check(time2, at2)



def check(time, at):
    if at == "AM":
        if ":" in time:
            a, b = at.split(":")
            return f"{a:2f}:{b}"
        else:
            return f"{at:2f}:00"

    elif at == "PM":
        if ":" in time:
            a, b = at.split(":")
            return f"{(int(a) + 12):2f}:{b}"
        else:
            f"{(int(at) + 12):2f}:00"


if __name__ == "__main__":
    main()