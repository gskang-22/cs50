import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    group = re.search("^([0-9:]+) ([A-Z]+) to ([0-9:]+) ([A-Z]+)$", s.strip())
    time1, at1, time2, at2 = group.groups()
    time1 = check(time1, at1)
    time2 = check(time2, at2)
    return f"{time1} to {time2}"


def check(time, at):
    if at == "AM":
        if ":" in time:
            a, b = time.split(":")
            if int(a) > 12:
                raise ValueError
            return f"{int(a):{'0'}{'2'}}:{b}"
        else:
            if int(time) > 12:
                raise ValueError
            return f"{int(time):{'0'}{'2'}}:00"

    elif at == "PM":
        if ":" in time:
            a, b = time.split(":")
            if int(a) > 12:
                raise ValueError
            return f"{(int(a) + 12):{'0'}{'2'}}:{b}"
        else:
            if int(time) > 12:
                raise ValueError
            return f"{(int(time) + 12):{'0'}{'2'}}:00"


if __name__ == "__main__":
    main()