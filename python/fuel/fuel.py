while True:
    a = input("Fraction: ")
    x, y = a.split("/")


    try:
        x = float(x)
        y = float(y)

        if x > y or y == 0:
            continue

        fraction = round((x / y), 2) * 100
        if fraction > 99:
            print("F")
        else:
            print(f"{int(fraction)}%")
    except ZeroDivisionError:
        print("E")

    except ValueError:
        continue