import csv
import sys

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too many command-line arguments")

        with open(sys.argv[1], "r") as file1, open(sys.argv[2], "w") as file2:
            for row in file1:
                

    except FileNotFoundError:
        sys.exit(f"could not read{argv[1]}")

if __name__ == "__main__":
    main()