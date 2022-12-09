while True:
    a = input("Fraction: ")
    x, y = a.split("/")


    try:
        x = int(x)
        y = int(y)

        if x > y or y == 0:
            continue

        fraction = round((float(x) / y), 2) * 100
        if fraction > 99:
            print("F")
        elif fraction < 1:
            print("E")
        else:
            print(f"{int(fraction)}%")
        break
    except ZeroDivisionError:
        continue

    except ValueError:
        continue