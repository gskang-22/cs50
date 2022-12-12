import csv
import sys

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        with open(sys.argv[1], "r") as file1, open(sys.argv[2], "w") as file2:
            csv1 = csv.reader(file1)
            csv2 = csv.writer(file2)

            csv2.writerow(["first", "last", "house"])

            for row in csv1:
                full_name = row[0]
                house = row[1]
                if full_name == "name":
                    continue

                temp = []
                last, first = full_name.split(",")

                temp.append(first.strip())
                temp.append(last.strip())
                temp.append(house)

                csv2.writerow(temp)


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()