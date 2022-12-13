import sys
import os

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        root, ext = os.path.splitext(sys.argv[1])

if __name__ == "__main__":
    main()