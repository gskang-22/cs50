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
            return 
        else:

    elif at == "PM":
        if ":" in time:

        else:



if __name__ == "__main__":
    main()