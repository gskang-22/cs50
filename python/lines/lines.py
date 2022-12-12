import sys

def main():
    count = 0
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[-3:] != ".py":
            sys.exit("Not a Python file")

        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.lstrip() == "":
                    continue
                else:
                    count += 1
        print(count)


    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()