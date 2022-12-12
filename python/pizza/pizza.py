import csv
from tabulate import tabulate
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")

        with open(sys.argv, "r") as file:
            csv = file.reader()
        print(tabulate(csv, headers="firstrow"))


    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main