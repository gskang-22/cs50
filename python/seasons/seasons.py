from datetime import date
import inflect


def main():
    print(convert(input("Date of Birth: ")))



def convert(s):
    date_today = date.today()
    try:
        a, b, c = s.strip().split("-")
        if not isdigit(a) and not isdigit(b) and not isdigit(c):
            raise ValueError

        if 


if __name__ == "__main__":
    main()