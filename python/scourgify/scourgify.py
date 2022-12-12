import csv
import sys

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too many command-line arguments")

        with open(sys.argv[1], "r") as file1, open(sys.argv[2], "w") as file2:
            csv1 = csv.reader(file1)
            for row in csv1:
                full_name = row[0]
                if full_name == "name":
                    continue

                temp = []
                last, name = full_name.split(",")
                


    except FileNotFoundError:
        sys.exit(f"could not read{argv[1]}")

if __name__ == "__main__":
    main()