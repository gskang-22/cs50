import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2
            sys.exit("Too many command-line arguments")

        file = open(sys.argv[1], "r")
        

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()