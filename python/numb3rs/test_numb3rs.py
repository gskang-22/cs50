import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    a, b, c, d = ip.split(".")
    if check(a) and check(b) and check(c) and check(d):
        return True
    else:
        return False


def check(n):
    if int(n) < 0:
        return False
    elif int(n) > 255:
        return False
    else:
        return True


if __name__ == "__main__":
    main()