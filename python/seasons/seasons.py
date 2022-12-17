from datetime import date, timedelta
import inflect
import sys


def main():
    print(convert(input("Date of Birth: ")))



def convert(s):
    date_today = date.today()
    try:
        a, b, c = s.strip().split("-")
        if not isdigit(a) and not isdigit(b) and not isdigit(c):
            raise ValueError

        if int(b) > 12 or int(c) > 31:
            raise ValueError

        date_birth = datetime.date(a, b, c)

        time = date_today - date_birth

        if time.days < 0:
            raise ValueError

    except:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()