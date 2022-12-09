a = input("Fraction: ")
x, y = a.split("/")
x = float(x)
y = float(y)

try:
    fraction = (x / y) * 100
    print(f"{int(fraction)}%")
except:
