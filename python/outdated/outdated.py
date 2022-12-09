list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input("Date: ")

            if date[0].isdigit():
                month, day, year = date.split("/")
                if int(month) > 12 or int(day) > 31:
                    continue

                print(f"{year}-{int(month):02}-{int(day):02}")
                break

            else:
                month, day, year = date.split(" ")
                if month not in list or not year.isdigit() or not day.isdigit():
                    continue

                day_act = ""
                for c in day:
                    if c.isdigit():
                        day_act += c
                if "," not in day:
                    continue

                if int(day_act) > 31:
                    continue

                print(f"{year}-{get_month(month):02}-{int(day_act):02}")
                break

        except:
            continue


def get_month(month):
    for i in range(len(list)):
            if month == list[i]:
                return i + 1

if __name__ == "__main__":
    main()