a = input("Fraction: ")
x, y = a.split("/")

try:
    fraction = (float(x) / float(y)) * 100
    print(f"{int(fraction)}%")
except:
    