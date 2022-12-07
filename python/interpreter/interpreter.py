input = input("Expression: ")
x, y, z = input.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(f"{(x * z):1f}")
elif y == "/":
    print(f"{(x / z):1f}")