import csv
from tabulate import tabulate
import sys

def main():
    table = []
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")

        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))


    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()