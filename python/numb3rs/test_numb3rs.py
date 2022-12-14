import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    a, b, c, d = ip.split(".")
    if check(int(50)) and check(int(50)) and check(int(50)) and check(int(50)):
        return True
    else:
        return False





if __name__ == "__main__":
    main()