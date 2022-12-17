from datetime import date, timedelta
import inflect
import sys


def main():
    print(convert(input("Date of Birth: ")))



def convert(s):
    date_today = date.today()
    p = inflect.engine()
    try:
        a, b, c = s.strip().split("-")
        if not a.isdigit() and not b.isdigit() and not c.isdigit():
            raise ValueError

        if int(b) > 12 or int(c) > 31:
            raise ValueError

        date_birth = date(int(a), int(b), int(c))

        time = date_today - date_birth

        if time.days < 0:
            raise ValueError

        time_in_min = round((time.days * 24 * 60) + (time.seconds / 60.0))
        string = (f"{p.number_to_words(time_in_min)} minutes").capitalize()
        return string.replace("and ", "")

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()