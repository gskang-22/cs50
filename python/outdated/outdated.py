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

while True:
    date = input("Date: ")

    if date[0].isdigit():
        month, day, year = date.split("/")
        if month > 12 or day > 31:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    else:
        month, day, year = date.split(" ")
        if month not in list:
            continue

        for c in day:
            if not c.isdigit():
                