while True
    a = input("Fraction: ")
    x, y = a.split("/")

    if not x.isdigit() or not y.isdigit():
        continue

    x = float(x)
    y = float(y)
    if x > y or y = 0:
        continue

    try:
        fraction = (x / y) * 100
        print(f"{int(fraction)}%")
    except:
        