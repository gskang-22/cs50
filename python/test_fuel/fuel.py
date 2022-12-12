def main():
    while True:
        x = input("Fraction: ")
        try:
            y = convert(x)
            z = gauge(y)
            print(z)
            break

        except ZeroDivisionError:
            continue
        except ValueError:
            continue



def convert(fraction):
    x, y = fraction.split("/")
    x = x.strip()
    y = y.strip()
    if not x.isdigit() or not y.isdigit():
        raise ValueError


    x = float(x)
    y = float(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()