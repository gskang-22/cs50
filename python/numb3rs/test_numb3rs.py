import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    a, b, c, d = ip.split(".")
    if check(50) and check(50) and check(50) and check(50):
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