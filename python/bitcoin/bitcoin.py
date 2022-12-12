import requests
import sys

def main():
    try:
        if len(sys.argv) < 2:
            print("Missing command-line argument")
        n = float(sys.argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r.json()

        print(f"${amount:,.4f}")

    except requests.RequestException:
        ...
    except ValueError:
        sys.exit("Command-line argument is not a number")

if __name__ == "__main__":
    main()