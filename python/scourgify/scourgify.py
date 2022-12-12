import csv
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")

    with open(sys.argv[1], "r") as file1, open(sys.argv[2], "r") as file2:
        

if __name__ == "__main__":
    main()