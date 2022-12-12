import requests
import sys

def main():
    try:
        if len(sys.argv) < 2:
            print("Missing command-line argument")
        n = float(sys.argv[1])

    except requests.RequestException:
        ...
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()